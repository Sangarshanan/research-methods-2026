"""
Download ISMIR proceedings
"""

import os
import time
import requests
import re
import pymupdf4llm
import pymupdf
from urllib.parse import urljoin
from docx import Document
from bs4 import BeautifulSoup


YEARS = range(2021, 2027)
BASE_DIR = "dataset"
OUTPUT_FORMAT = "md"
SAVE_PDF = True

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ISMIR-Proceedings-Converter/2.2)"
}

def sanitize_filename(name: str, max_len: int = 120) -> str:
    """Clean string to create a safe filesystem filename."""
    clean = re.sub(r'[\\/*?:"<>|\n\r\t]+', " ", name)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:max_len].strip()

def extract_paper_title(a_tag) -> str:
    """Extract the cleanest possible paper title from the anchor tag or its container."""
    link_text = a_tag.get_text(" ", strip=True)
    if link_text and not re.search(r"^(download|pdf|paper|link|\[pdf\])$", link_text, re.I) and len(link_text) > 5:
        return link_text

    if a_tag.parent:
        parent_text = a_tag.parent.get_text(" ", strip=True)
        cleaned = re.sub(r"(\[?\bDownload\s*PDF\b\]?|\bDownload\b|\bPDF\b)", "", parent_text, flags=re.I).strip()
        cleaned = re.sub(r"^[\s\-–—:|]+|[\s\-–—:|]+$", "", cleaned).strip()
        if len(cleaned) > 5:
            return cleaned

    return ""

def get_existing_files_by_ext(folder: str, ext: str) -> dict:
    """
    Scan the directory for already-saved files with the given extension (.pdf or .md).
    Cleans up untitled '000001.ext' files if '000001_Title.ext' is present.
    """
    existing = {}
    if not os.path.exists(folder):
        return existing

    pattern = re.compile(rf"^(?:ismir\d{{4}}_paper_)?(\d{{6}})(?:_(.+))?\.{re.escape(ext)}$", re.I)
    for fname in os.listdir(folder):
        match = pattern.match(fname)
        if match:
            paper_id, title_part = match.group(1), match.group(2)
            full_path = os.path.join(folder, fname)

            if paper_id in existing:
                prev_path, prev_has_title = existing[paper_id]
                if title_part and not prev_has_title:
                    os.remove(prev_path)
                    print(f"  [CLEAN] Removed untitled duplicate: {os.path.basename(prev_path)}")
                    existing[paper_id] = (full_path, True)
                elif not title_part and prev_has_title:
                    os.remove(full_path)
                    print(f"  [CLEAN] Removed untitled duplicate: {fname}")
            else:
                existing[paper_id] = (full_path, bool(title_part))

    return existing

def save_clean_pdf_and_doc(
    pdf_bytes: bytes,
    pdf_filepath: str,
    doc_filepath: str,
    metadata: dict,
    fmt: str,
    need_pdf: bool,
    need_doc: bool
) -> tuple[bool, bool]:
    """
    Rebuilds the PDF and extracts text
    """
    saved_pdf = False
    saved_doc = False

    if not pdf_bytes.startswith(b"%PDF"):
        print(f"  [INVALID] Stream for {metadata.get('paper_id')} is not a valid PDF header.")
        return False, False

    try:
        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as doc:
            # 1. Save cleanly rebuilt binary PDF (repairs PyPDF2 xref tables)
            if need_pdf:
                doc.save(pdf_filepath, garbage=4, deflate=True)
                saved_pdf = True

            # 2. Extract Markdown and save document
            if need_doc:
                md_text = pymupdf4llm.to_markdown(doc, show_progress=False)
                md_text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", md_text)

                if fmt == "md":
                    paper_id = metadata.get("paper_id", "")
                    year = metadata.get("year", "")
                    raw_title = metadata.get("title", "")
                    escaped_title = raw_title.replace("\\", "\\\\").replace('"', '\\"')
                    source_url = metadata.get("url", "")

                    frontmatter = (
                        "---\n"
                        f'paper_id: "{paper_id}"\n'
                        f"year: {year}\n"
                        f'title: "{escaped_title}"\n'
                        f'source_url: "{source_url}"\n'
                        "---\n\n"
                    )
                    with open(doc_filepath, "w", encoding="utf-8") as f:
                        f.write(frontmatter + md_text)
                    saved_doc = True

                elif fmt == "docx":
                    if Document is None:
                        raise RuntimeError("python-docx is not installed. Run: pip install python-docx")
                    word_doc = Document()
                    if metadata.get("title"):
                        word_doc.add_heading(metadata["title"], level=0)
                    word_doc.add_paragraph(
                        f"Year: {metadata.get('year')} | ID: {metadata.get('paper_id')} | URL: {metadata.get('url')}"
                    )
                    for block in md_text.split("\n\n"):
                        clean_block = block.strip()
                        if not clean_block:
                            continue
                        if clean_block.startswith("#"):
                            level = min(len(clean_block) - len(clean_block.lstrip("#")), 4)
                            word_doc.add_heading(clean_block.lstrip("# ").strip(), level=level)
                        else:
                            word_doc.add_paragraph(clean_block)
                    word_doc.save(doc_filepath)
                    saved_doc = True

    except Exception as e:
        print(f"  [PROC ERR] Failed processing {metadata.get('paper_id')}: {e}")

    return saved_pdf, saved_doc

def process_paper(
    url: str,
    base_name: str,
    pdf_dir: str,
    doc_dir: str,
    metadata: dict,
    fmt: str,
    existing_pdfs: dict,
    existing_docs: dict,
    session: requests.Session
) -> bool:
    """Manages downloading, deduplicating, repairing PDFs, and converting to Markdown/DOCX."""
    stem = metadata["paper_id"]
    has_title = bool(metadata.get("title") and metadata["title"] != stem)
    pdf_filepath = os.path.join(pdf_dir, f"{base_name}.pdf")
    doc_filepath = os.path.join(doc_dir, f"{base_name}.{fmt}")

    # Rename untitled existing files if we now have a title
    if stem in existing_pdfs:
        old_pdf_path, pdf_had_title = existing_pdfs[stem]
        if not pdf_had_title and has_title and old_pdf_path != pdf_filepath:
            os.rename(old_pdf_path, pdf_filepath)
            existing_pdfs[stem] = (pdf_filepath, True)
        else:
            pdf_filepath = old_pdf_path

    if stem in existing_docs:
        old_doc_path, doc_had_title = existing_docs[stem]
        if not doc_had_title and has_title and old_doc_path != doc_filepath:
            os.rename(old_doc_path, doc_filepath)
            existing_docs[stem] = (doc_filepath, True)
        else:
            doc_filepath = old_doc_path

    need_pdf = SAVE_PDF and (stem not in existing_pdfs)
    need_doc = stem not in existing_docs

    if not need_pdf and not need_doc:
        print(f"  [SKIP] Already have PDF and {fmt.upper()} for {stem}")
        return True

    pdf_bytes = None

    # Reuse local PDF if already downloaded
    if not need_pdf and os.path.exists(pdf_filepath):
        try:
            with open(pdf_filepath, "rb") as f:
                pdf_bytes = f.read()
        except OSError:
            pdf_bytes = None

    # Download raw binary bytes from server
    if pdf_bytes is None:
        try:
            with session.get(url, headers=HEADERS, timeout=30) as r:
                if r.status_code == 200 and r.content.startswith(b"%PDF"):
                    pdf_bytes = r.content
                    time.sleep(0.5)
                else:
                    return False
        except requests.RequestException as e:
            print(f"  [NET ERR] Failed {url}: {e}")
            return False

    saved_pdf, saved_doc = save_clean_pdf_and_doc(
        pdf_bytes, pdf_filepath, doc_filepath, metadata, fmt, need_pdf, need_doc
    )

    if saved_pdf:
        existing_pdfs[stem] = (pdf_filepath, has_title)
        print(f"  [OK PDF] Saved clean PDF: {os.path.basename(pdf_filepath)}")
    if saved_doc:
        existing_docs[stem] = (doc_filepath, has_title)
        print(f"  [OK {fmt.upper()}]  Saved {fmt.upper()}: {os.path.basename(doc_filepath)}")

    return saved_pdf or saved_doc

def scrape_conference_page(year: int, pdf_dir: str, doc_dir: str, fmt: str, session: requests.Session) -> int:
    """Scrape unique paper PDFs from ismir.net/conferences/ismir-YYYY/"""
    index_url = f"https://ismir.net/conferences/ismir-{year}/"
    print(f"\n--- Checking {index_url} ---")

    try:
        resp = session.get(index_url, headers=HEADERS, timeout=20)
        if resp.status_code != 200:
            print(f"Index page for {year} returned HTTP {resp.status_code}.")
            return 0
    except requests.RequestException as e:
        print(f"Could not reach {index_url}: {e}")
        return 0

    soup = BeautifulSoup(resp.text, "html.parser")

    pdf_entries = {}
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href.lower().endswith(".pdf"):
            continue

        full_url = urljoin(index_url, href)
        orig_name = os.path.basename(full_url)

        if "Proceedings_ISMIR" in orig_name:
            continue

        candidate_title = extract_paper_title(a)
        if full_url not in pdf_entries or len(candidate_title) > len(pdf_entries[full_url]):
            pdf_entries[full_url] = candidate_title

    existing_pdfs = get_existing_files_by_ext(pdf_dir, "pdf")
    existing_docs = get_existing_files_by_ext(doc_dir, fmt)
    count = 0

    for full_url, title in pdf_entries.items():
        orig_name = os.path.basename(full_url)
        stem = os.path.splitext(orig_name)[0]

        base_name = f"{stem}_{sanitize_filename(title)}" if title else stem
        metadata = {
            "paper_id": stem,
            "year": year,
            "title": title or stem,
            "url": full_url
        }

        if process_paper(full_url, base_name, pdf_dir, doc_dir, metadata, fmt, existing_pdfs, existing_docs, session):
            count += 1

    return count

def probe_archive_sequentially(year: int, pdf_dir: str, doc_dir: str, fmt: str, session: requests.Session) -> int:
    """Fallback method for direct archive probing if index page isn't available."""
    print(f"Running sequential archive probe for ISMIR {year}...")
    existing_pdfs = get_existing_files_by_ext(pdf_dir, "pdf")
    existing_docs = get_existing_files_by_ext(doc_dir, fmt)
    consecutive_misses = 0
    paper_id = 1
    count = 0

    while consecutive_misses < 5 and paper_id <= 200:
        stem = f"{paper_id:06d}"
        url = f"https://archives.ismir.net/ismir{year}/paper/{stem}.pdf"
        metadata = {
            "paper_id": stem,
            "year": year,
            "title": "",
            "url": url
        }

        if process_paper(url, stem, pdf_dir, doc_dir, metadata, fmt, existing_pdfs, existing_docs, session):
            count += 1
            consecutive_misses = 0
        else:
            consecutive_misses += 1
            time.sleep(0.2)
        paper_id += 1

    return count

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    with requests.Session() as session:
        for year in YEARS:
            pdf_dir = os.path.join(BASE_DIR, str(year), "pdf")
            doc_dir = os.path.join(BASE_DIR, str(year), OUTPUT_FORMAT)
            os.makedirs(pdf_dir, exist_ok=True)
            os.makedirs(doc_dir, exist_ok=True)

            processed = scrape_conference_page(year, pdf_dir, doc_dir, OUTPUT_FORMAT, session)
            if processed == 0:
                processed = probe_archive_sequentially(year, pdf_dir, doc_dir, OUTPUT_FORMAT, session)

            print(f"Total unique papers processed for {year}: {processed}")

if __name__ == "__main__":
    main()