"""
ISMIR Dataset Parser & Analysis Module
Reads converted Markdown papers over the years and provides a structured
dictionary hierarchy: data[year][paper_id] = {'title': ..., 'metadata': ..., 'sections': ...}
"""

import csv
import os
import re
from typing import Any, Dict, List, Optional, Tuple

def normalize_section_key(name: str) -> str:
    """
    Normalizes a section heading to a clean lowercase underscore key:
    """
    clean = re.sub(r"^[0-9]+(?:\.[0-9]+)*\.?\s*", "", name).strip()
    clean = re.sub(r"[*_#]", "", clean).strip()
    clean = re.sub(r"[^\w\s-]", "", clean)
    clean = re.sub(r"[\s-]+", "_", clean).strip("_").lower()
    return clean or "unnamed_section"


class SectionDict(dict):
    """
    Dictionary for paper sections that supports normalized lookup and canonical aliases
    while maintaining 100% standard Python dictionary compatibility and JSON serializability.
    """

    CANONICAL_ALIASES = {
        "method": ["methods", "methodology", "model", "approach", "proposed_method", "proposed_approach"],
        "methods": ["methodology", "method", "model", "approach", "proposed_method", "proposed_approach"],
        "methodology": ["methods", "method", "model", "approach", "proposed_method", "proposed_approach"],
        "result": ["results", "experimental_results", "experiments", "evaluation", "results_and_discussion"],
        "results": ["experimental_results", "experiments", "evaluation", "result", "results_and_discussion"],
        "experiments": ["experimental_results", "results", "evaluation", "experimental_setup"],
        "conclusion": ["conclusions", "conclusion_and_future_work", "conclusions_and_future_work", "summary"],
        "conclusions": ["conclusion", "conclusion_and_future_work", "conclusions_and_future_work", "summary"],
        "acknowledgment": ["acknowledgments", "acknowledgements", "acknolwedgements"],
        "acknowledgments": ["acknowledgements", "acknowledgment", "acknolwedgements"],
        "acknowledgements": ["acknowledgments", "acknowledgment", "acknolwedgements"],
        "background": ["related_work", "prior_work", "literature_review"],
        "related_work": ["background", "prior_work", "literature_review"],
        "ethics": ["ethics_statement", "ethical_considerations", "ai_disclosure", "reproducibility"],
        "ethics_statement": ["ethics", "ethical_considerations", "ai_disclosure"],
        "reference": ["references", "bibliography"],
        "references": ["reference", "bibliography"],
        "dataset": ["datasets", "data", "corpus", "audio_data"],
        "datasets": ["dataset", "data", "corpus"],
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._raw_titles: Dict[str, str] = {}

    def set_raw_title(self, key: str, raw_title: str):
        """Record the original unmodified header text for a section."""
        self._raw_titles[key] = raw_title

    def get_raw_title(self, key: str) -> Optional[str]:
        """Get the original unmodified header text for a section."""
        return self._raw_titles.get(key)

    def __getitem__(self, key: str) -> str:
        # 1. Exact match
        if key in self:
            return super().__getitem__(key)

        # 2. Normalized key match (e.g. '1. INTRODUCTION' -> 'introduction')
        norm_key = normalize_section_key(str(key))
        if norm_key in self:
            return super().__getitem__(norm_key)

        # 3. Canonical alias match (e.g. 'methods' -> 'methodology')
        if norm_key in self.CANONICAL_ALIASES:
            for alias in self.CANONICAL_ALIASES[norm_key]:
                if alias in self:
                    return super().__getitem__(alias)

        # 4. Fuzzy / substring match
        for existing_key in self.keys():
            if norm_key == existing_key or norm_key in existing_key or existing_key in norm_key:
                return super().__getitem__(existing_key)

        raise KeyError(key)

    def get(self, key: str, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def has_section(self, key: str) -> bool:
        """Check if a section (or an alias for it) exists in this paper."""
        try:
            _ = self[key]
            return True
        except KeyError:
            return False

    def search(self, pattern: str, flags: int = re.IGNORECASE) -> Dict[str, List[str]]:
        """Search across all sections in this paper for a regex pattern or keyword."""
        matches = {}
        for section_name, content in self.items():
            found = re.findall(pattern, content, flags)
            if found:
                matches[section_name] = found
        return matches


# MARKDOWN & FRONTMATTER PARSING

def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter enclosed in --- at the start of a markdown file."""
    metadata = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2].lstrip()
            for line in fm_text.splitlines():
                line = line.strip()
                if not line or ":" not in line:
                    continue
                k, v = line.split(":", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if v.isdigit():
                    v = int(v)
                metadata[k] = v
    return metadata, body


def parse_paper_markdown(md_path: str) -> Dict[str, Any]:
    """
    Parse a single ISMIR paper Markdown file into structured sections and metadata.
    """
    with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
        raw_text = f.read()

    metadata, body = parse_frontmatter(raw_text)
    lines = body.splitlines()

    # Pattern to detect major academic paper sections
    major_section_re = re.compile(
        r"^#{1,4}\s+[*_]*("
        r"ABSTRACT|"
        r"\d+\.?\s+[A-Z0-9][A-Za-z0-9\s,\-–—:\'\"]+|"
        r"ACKNOWLEDG[M|N]ENTS?|"
        r"REFERENCES|"
        r"APPENDIX(?:ES)?|"
        r"ETHICS?\s*(?:STATEMENT|CONSIDERATIONS)?|"
        r"AI\s*DISCLOSURE|"
        r"REPRODUCIBILITY"
        r")[*_]*\s*$",
        re.IGNORECASE
    )

    found_sections = []
    for i, line in enumerate(lines):
        line_clean = line.strip()
        m = major_section_re.match(line_clean)
        if m:
            raw_title = m.group(1).strip()
            raw_title = re.sub(r"[*_#]", "", raw_title).strip()
            # Exclude numbered subsections (e.g. 3.1, 4.2.1) from cutting major sections
            if re.match(r"^\d+\.\d+", raw_title):
                continue
            found_sections.append((i, raw_title))

    sections = SectionDict()

    if found_sections:
        # Content before the first major section (Title, Authors, Affiliations)
        first_idx = found_sections[0][0]
        header_text = "\n".join(lines[:first_idx]).strip()
        if header_text:
            sections["header"] = header_text
            sections.set_raw_title("header", "Header / Title & Authors")

        # Slice sections between identified headers
        for idx, (line_idx, raw_title) in enumerate(found_sections):
            start_line = line_idx + 1
            end_line = found_sections[idx + 1][0] if idx + 1 < len(found_sections) else len(lines)
            content = "\n".join(lines[start_line:end_line]).strip()
            norm_key = normalize_section_key(raw_title)

            # Avoid overwriting if duplicate headings occur; append instead
            if norm_key in sections:
                sections[norm_key] = sections[norm_key] + "\n\n" + content
            else:
                sections[norm_key] = content
            sections.set_raw_title(norm_key, raw_title)
    else:
        # Fallback if no markdown headers detected
        sections["full_text"] = body.strip()
        sections.set_raw_title("full_text", "Full Document Text")

    # Paper title discovery
    title = metadata.get("title")
    if not title:
        for line in lines:
            if line.startswith("#"):
                title = re.sub(r"[*_#]", "", line).strip()
                break
    if not title:
        title = os.path.splitext(os.path.basename(md_path))[0]

    # Clean paper_id (preserving original string formatting with leading zeroes)
    raw_id = metadata.get("paper_id")
    if raw_id is not None:
        paper_id = f"{int(raw_id):06d}" if str(raw_id).isdigit() else str(raw_id)
    else:
        file_base = os.path.basename(md_path)
        id_match = re.match(r"^(\d{6})", file_base)
        paper_id = id_match.group(1) if id_match else file_base.split("_")[0].replace(".md", "")

    # Clean year
    year = metadata.get("year")
    if year is None:
        parent_dir = os.path.basename(os.path.dirname(os.path.abspath(md_path)))
        grandparent_dir = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(md_path))))
        if parent_dir.isdigit():
            year = int(parent_dir)
        elif grandparent_dir.isdigit():
            year = int(grandparent_dir)

    metadata["paper_id"] = paper_id
    metadata["year"] = year
    metadata["title"] = title
    metadata["file_path"] = os.path.abspath(md_path)

    return {
        "paper_id": paper_id,
        "year": year,
        "title": title,
        "metadata": metadata,
        "sections": sections,
        "full_text": body.strip(),
    }


# DATASET LOADER
def find_default_data_dir(candidates: Optional[List[str]] = None) -> str:
    """Find the root directory containing ISMIR papers ('dataset' or 'ISMIR_Papers')."""
    if candidates is None:
        candidates = ["dataset", "ISMIR_Papers"]

    for d in candidates:
        if os.path.exists(d) and os.path.isdir(d):
            return d
    return "dataset"


def load_ismir_dataset(
    data_dir: Optional[str] = None,
    years: Optional[List[int]] = None,
    verbose: bool = True,
) -> Dict[int, Dict[str, Dict[str, Any]]]:
    """
    Read the dataset of Markdown files over the years into a nested dictionary:
    """
    if data_dir is None:
        data_dir = find_default_data_dir()

    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory '{data_dir}' not found.")

    dataset: Dict[int, Dict[str, Dict[str, Any]]] = {}
    total_files = 0

    if verbose:
        print(f"Loading ISMIR Markdown dataset from: '{data_dir}'...")

    # Traverse directory structure
    for item in sorted(os.listdir(data_dir)):
        year_path = os.path.join(data_dir, item)
        if not os.path.isdir(year_path) or not item.isdigit():
            continue

        year = int(item)
        if years is not None and year not in years:
            continue

        dataset[year] = {}

        # Look in either <year>/md/ or <year>/ directly
        md_subdir = os.path.join(year_path, "md")
        search_dirs = [md_subdir] if os.path.exists(md_subdir) else [year_path]

        for sdir in search_dirs:
            for fname in sorted(os.listdir(sdir)):
                if not fname.endswith(".md"):
                    continue

                md_path = os.path.join(sdir, fname)
                try:
                    paper_data = parse_paper_markdown(md_path)
                    paper_id = paper_data["paper_id"]
                    dataset[year][paper_id] = paper_data
                    total_files += 1
                except Exception as e:
                    if verbose:
                        print(f"  [WARN] Failed parsing {md_path}: {e}")

        if verbose:
            print(f"  [Year {year}] Loaded {len(dataset[year])} papers.")

    if verbose:
        print(f"Total: {total_files} papers loaded across {len(dataset)} year(s).\n")

    return dataset


# DOWNSTREAM ANALYSIS HELPERS

def search_dataset(
    dataset: Dict[int, Dict[str, Dict[str, Any]]],
    query_regex: str,
    target_sections: Optional[List[str]] = None,
    flags: int = re.IGNORECASE,
) -> List[Dict[str, Any]]:
    """
    Search for a regex pattern or keyword (e.g. AI tool disclosures) across all papers.
    
    Args:
        dataset: The loaded dataset dictionary.
        query_regex: Regex pattern string (e.g. r'\b(chatgpt|copilot|llm|language model)\b').
        target_sections: Optional list of sections to restrict search to (e.g. ['acknowledgments', 'introduction']).
        flags: Regex compilation flags.
        
    Returns:
        List of match records:
        [{'year': 2021, 'paper_id': '000001', 'title': '...', 'section': 'acknowledgments', 'matches': [...]}, ...]
    """
    pattern = re.compile(query_regex, flags)
    results = []

    for year, papers in sorted(dataset.items()):
        for paper_id, paper in papers.items():
            sections = paper["sections"]
            search_items = (
                [(sec, sections[sec]) for sec in target_sections if sec in sections]
                if target_sections
                else sections.items()
            )

            for sec_name, content in search_items:
                matches = pattern.findall(content)
                if matches:
                    results.append({
                        "year": year,
                        "paper_id": paper_id,
                        "title": paper["title"],
                        "section": sec_name,
                        "raw_title": sections.get_raw_title(sec_name) or sec_name,
                        "matches": matches,
                        "snippet": extract_snippet(content, pattern),
                    })
    return results


def extract_snippet(text: str, pattern: re.Pattern, window: int = 140) -> str:
    """Extract a short text snippet around the first match of a pattern."""
    m = pattern.search(text)
    if not m:
        return ""
    start = max(0, m.start() - window)
    end = min(len(text), m.end() + window)
    snippet = text[start:end].replace("\n", " ").strip()
    return f"...{snippet}..."


def export_summary_csv(dataset: Dict[int, Dict[str, Dict[str, Any]]], csv_path: str):
    """Export a high-level CSV summary of all papers and their sections."""
    fieldnames = ["year", "paper_id", "title", "source_url", "section_count", "sections_available"]
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for year, papers in sorted(dataset.items()):
            for paper_id, p in sorted(papers.items()):
                writer.writerow({
                    "year": year,
                    "paper_id": paper_id,
                    "title": p["title"],
                    "source_url": p["metadata"].get("source_url", ""),
                    "section_count": len(p["sections"]),
                    "sections_available": ", ".join(p["sections"].keys()),
                })
    print(f"Exported summary CSV to: {csv_path}")
