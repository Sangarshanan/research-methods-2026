"""
disclosure_location.py — screening, disclosure gate and LOCATION coding of AI-use disclosures
MERE project (AI Tool Disclosure in Sound & Music Computing). Owner: location dimension.

Scope of THIS module (to avoid overlap with teammates):
    * decides WHICH paragraphs are AI-use disclosures (the shared "gate", rule in the codebook)
    * decides WHERE each disclosure sits (location)
    * exports a master list of verified disclosures with stable IDs (disclosure_id) that the
      tasks / specificity / statement-type coders attach their codes to.
    It does NOT code what the AI was used for, how specific the statement is, or its type.

Workflow (see notebook.ipynb):
    data   = load_ismir_dataset(...)                      # analyse_dataset.py (unchanged)
    report = coverage_report(data, EXPECTED_PAPERS)       # missing paper numbers per year
    hits   = screen_dataset(data)                         # candidate paragraphs + proposed location
    export_coding_workbook(hits, data, "location_coding.xlsx")
    ... coders fill in sheets 'to_code', 'recall_sample', 'reliability_10pct' ...
    kappa  = reliability("location_coding.xlsx")
    res    = summarise_verified("location_coding.xlsx", data)
    export_disclosure_list("location_coding.xlsx", "disclosures_master.xlsx")
"""

from __future__ import annotations

import random
import re
from itertools import combinations
from typing import Dict, List, Optional, Tuple

# ==============================================================================================
# 1. SETTINGS  (edit these, not the code below)
# ==============================================================================================

# Named AI tools / terms. Word boundaries matter: DeepL is not "deep learning", Claude is not a
# person called Claude, Perplexity AI is not the perplexity metric.
TOOL_TERMS: Dict[str, str] = {
    "ChatGPT":           r"\bchat\s?-?gpt\b",
    "GPT-n":             r"\bgpt-?\s?(3(\.5)?|4(o|\.\d)?|5)\b|\bgpt[- ]?4o\b",
    "OpenAI":            r"\bopenai\b",
    "Claude":            r"\bclaude\s?(\d(\.\d)?|sonnet|opus|haiku|code|ai)\b|\banthropic\b",
    "Gemini":            r"\bgemini\b",
    "Bard":              r"\bgoogle bard\b",
    "Copilot":           r"\b(github\s)?copilot\b",
    "Grammarly":         r"\bgrammarly\b",
    "DeepL":             r"\bdeepl\b(?!\w)",
    "Writing tools":     r"\b(quillbot|writefull|languagetool|perplexity(\.ai| ai)|cursor ai|notebooklm)\b",
    "LLM":               r"\bllms?\b|\blarge language models?\b",
    "Generative AI":     r"\bgen(erative)?\s?ai\b",
    "AI assistant/tool": r"\bai[- ](powered |based )?(writing )?(assistants?|tools?|chatbots?)\b|\bai-assisted\b",
}

# Generic wording used WITHOUT a tool name. Only screened inside the places where disclosures
# usually live (acknowledgments, ethics statement, dedicated statement, footnote, appendix),
# and only together with a writing / use / non-use cue (see screen_dataset).
GENERIC_AI_TERMS = (
    r"\b(ai|a\.i\.|artificial intelligence|language models?|machine translation|"
    r"translation (tool|software|service)s?|writing assistan\w+|chatbots?|"
    r"automated (writing|translation|proofreading))\b"
)

# Cues that the paragraph is about producing THIS paper (writing / editing / translating it).
WRITING_CUES = (
    r"\b(proof-?read\w*|grammar|grammatical|spell(ing)?[- ]?check\w*|polish(ing|ed)? (the |our )?"
    r"(text|writing|language|manuscript|paper|prose)|wording|phrasing|readability|"
    r"language (editing|improvement|correction|polishing)|(writing|editing) (assistance|assistant|support)|"
    r"rephras\w*|paraphras\w*|manuscript|(writ|draft|edit|prepar)\w* (of )?(this|the|our) (paper|article|text))\b"
)
# Cues that the authors THEMSELVES used something.
USE_CUES = (
    r"\b(we|the authors?|i)\s+(used|use|employed|employ|utili[sz]ed|leveraged|relied on|prompted|asked|queried)\b|"
    r"\b(was|were|is|are|has been|have been)\s+(used|employed|utili[sz]ed|generated|produced|written|translated|"
    r"annotated|summari[sz]ed|labell?ed|created|assisted|checked|refined|proofread|edited)\s+(by|with|using)\b|"
    r"\b(using|with the help of|with assistance from|assisted by|generated (by|with)|translated (by|with|using))\b"
)
# Explicit non-use statements.
NON_USE_CUES = (
    r"\b(no|not|did not use|didn't use|without (the )?(use|help|aid) of)\b[^.]{0,60}"
    r"\b(ai|llms?|chatgpt|generative|language models?|ai tools?)\b"
)
# Headings that ARE an AI-use statement.
DEDICATED_HEADING = (
    r"\b(ai|llms?|large language models?|gen(erative)?\s?ai|chatgpt)\b[^\n]{0,40}"
    r"\b(use|usage|disclosure|statement|declaration|assistance|policy)\b|"
    r"\b(use|usage|disclosure|declaration|statement) (of|on) (ai|llms?|large language|gen(erative)?\s?ai|ai tools)\b"
)

# Location codes (aligned with what venue policies prescribe: ACM -> methods/body,
# IEEE -> acknowledgments, NIME -> ethical statement, ISMIR 2026 -> methodology).
LOCATION_CODES = ["dedicated_statement", "ethics_statement", "acknowledgments",
                  "body_text", "footnote", "appendix"]

# Gate: why a paragraph is NOT a disclosure (only fill when is_disclosure = N).
EXCLUSION_REASONS = ["subject_of_study", "method_component", "third_party_use",
                     "link_or_citation_only", "funding_or_name", "general_discussion", "other"]

# Official paper counts, to check dataset coverage. Fill in what you know (None = unknown).
EXPECTED_PAPERS = {2021: 104, 2022: None, 2023: 103, 2024: None, 2025: None, 2026: None}

RECALL_SAMPLE_SIZE = 50          # random priority-0 rows coded to estimate what the screen misses
RELIABILITY_SHARE = 0.10         # share of coded rows (to_code + recall_sample) coded by all four coders
RELIABILITY_MIN = 20             # ...but never fewer than this (kappa is meaningless on a handful of rows)
CODER_NAMES = ["Hemanth", "Second_coder"]   # primary coder + one teammate for the reliability sample
RANDOM_SEED = 2026

# ==============================================================================================
# 2. SEGMENTING A PAPER INTO PARAGRAPHS WITH THEIR SECTION
# ==============================================================================================

_HEADING = re.compile(r"^\s*#{1,6}\s+(.*?)\s*$")
_SUBNUM = re.compile(r"^\s*\d+\.\d+")
_FOOTNOTE = re.compile(r"^\s*(>\s*)?(<sup>)?\d{1,2}(</sup>)?\s+(?!\d)\S")
_CAPTION = re.compile(r"^\s*(\*\*|_)?(figure|fig\.|table)\s*\d+", re.I)
_PICTURE = re.compile(r"<!--\s*(start|end) of picture text\s*-->", re.I)
_BODY_HEADINGS = re.compile(r"introduction|related|background|result|discussion|conclusion|"
                            r"future work|limitation", re.I)


def _clean_heading(text: str) -> str:
    return re.sub(r"[*_`#]", "", text).strip()


def _heading_family(heading: str) -> str:
    h = re.sub(r"^\s*[0-9]+\.?\s*", "", heading).lower()
    if re.search(r"^(references?|bibliography)\b", h):
        return "references"
    if re.search(r"acknowledg|acknolwedg|acknowlegd", h):
        return "acknowledgments"
    if re.search(DEDICATED_HEADING, h, re.I):
        return "dedicated_statement"
    if re.search(r"ethic", h):
        return "ethics_statement"
    if re.search(r"^(appendix|appendices|supplementary)", h):
        return "appendix"
    if re.search(r"^abstract\b", h):
        return "abstract"
    return "body_text"


def segment_paper(full_text: str) -> List[dict]:
    """Split a paper's Markdown into paragraphs, each tagged with its section."""
    paragraphs, buf = [], []
    major, sub, family = "", "", "header"
    seen_title = False

    def flush():
        text = " ".join(" ".join(buf).split())
        buf.clear()
        if text:
            paragraphs.append({"text": text, "section_heading": major or "(before first heading)",
                               "subsection_heading": sub, "section_family": family})

    for line in full_text.splitlines():
        m = _HEADING.match(line)
        if m:
            flush()
            head = _clean_heading(m.group(1))
            if not seen_title:                       # first '#' line is the paper title
                seen_title, major, family = True, "(title)", "header"
                continue
            if _SUBNUM.match(head):                  # 3.1 etc. keep the major section
                sub = head
                if re.search(DEDICATED_HEADING, head, re.I):
                    family = "dedicated_statement"
                continue
            fam = _heading_family(head)
            # unnumbered stray headings inside a body section (figure titles, names) stay put
            if fam == "body_text" and family != "header" and not re.match(r"^\s*\d", head) \
                    and not _BODY_HEADINGS.search(head):
                sub = head
                continue
            major, sub, family = head, "", fam
            continue
        if not line.strip():
            flush()
            continue
        buf.append(line)
    flush()
    return paragraphs


def _location_for(par: dict) -> str:
    """Map a paragraph to a location code."""
    text, fam = par["text"], par["section_family"]
    if fam not in ("references", "header") and _FOOTNOTE.match(text) and len(text) < 400 \
            and not _CAPTION.match(text):
        return "footnote"
    if fam == "abstract":
        return "body_text"
    return fam


def paper_sections(paper: dict) -> Dict[str, bool]:
    """Which disclosure-relevant sections this paper HAS (for availability-adjusted shares)."""
    fams = {p["section_family"] for p in segment_paper(paper.get("full_text", ""))}
    return {f"has_{f}": (f in fams) for f in ("acknowledgments", "ethics_statement",
                                              "dedicated_statement", "appendix")}


def paper_title(paper: dict) -> str:
    """Real title = first '#' heading (the 2025 files are all titled 'Download pdf')."""
    for line in paper.get("full_text", "").splitlines():
        m = _HEADING.match(line)
        if m:
            t = _clean_heading(m.group(1))
            if t:
                return t.title() if t.isupper() else t
    return paper.get("title", "")


# ==============================================================================================
# 3. COVERAGE CHECK
# ==============================================================================================

def coverage_report(data: Dict[int, Dict[str, dict]], expected: Optional[Dict[int, Optional[int]]] = None):
    """Per year: papers in the dataset, expected count, and paper numbers missing from the sequence."""
    expected = expected or EXPECTED_PAPERS
    rows = []
    for year, papers in sorted(data.items()):
        ids = sorted(int(p) for p in papers if str(p).isdigit())
        gaps = sorted(set(range(1, max(ids) + 1)) - set(ids)) if ids else []
        exp = expected.get(year)
        rows.append({"year": year, "papers_in_dataset": len(papers), "expected": exp,
                     "difference": (len(papers) - exp) if exp else None,
                     "missing_paper_numbers": ", ".join(f"{g:06d}" for g in gaps)})
    return rows


# ==============================================================================================
# 4. SCREENING
# ==============================================================================================

_TOOL_RES = {name: re.compile(rx, re.I) for name, rx in TOOL_TERMS.items()}
_GENERIC = re.compile(GENERIC_AI_TERMS, re.I)
_WRITING = re.compile(WRITING_CUES, re.I)
_USE = re.compile(USE_CUES, re.I)
_NON_USE = re.compile(NON_USE_CUES, re.I)
_DISCLOSURE_PLACES = ("acknowledgments", "ethics_statement", "dedicated_statement", "footnote", "appendix")

# Flags that make a row PROBABLY not a disclosure (shown to coders, never used to drop rows)
_FLAG_LINK = re.compile(r"^\s*>?\s*\d{0,2}\s*`?\s*https?://\S+`?\s*\.?\s*$|^\s*>?\s*\d{1,2}\s+`?https?://", re.I)
_FLAG_FUNDING = re.compile(r"\b(fund\w*|grant|supported by|financ\w*|project|programme|program|"
                           r"centre|center|institute|foundation|council|scheme)\b", re.I)
_FLAG_CITE = re.compile(r"\bet al\.|\[\d+(?:\s*[,–-]\s*\d+)*\]")


def _near(pattern: re.Pattern, text: str, spans, window: int = 90) -> bool:
    for m in pattern.finditer(text):
        for (s0, e0) in spans:
            if m.start() <= e0 + window and s0 <= m.end() + window:
                return True
    return False


def _flags(text: str, location: str, spans) -> List[str]:
    out = []
    if _FLAG_LINK.search(text) and len(text) < 200:
        out.append("link_only")
    if location == "acknowledgments" and _FLAG_FUNDING.search(text) and not _USE.search(text):
        out.append("funding_or_name")
    # citation within 40 characters of the tool mention, and no first-person use near it
    if spans and _near(_FLAG_CITE, text, spans, window=40) and not _near(_USE, text, spans, window=60):
        out.append("likely_third_party")
    return out


def _priority(text: str, location: str, spans) -> Tuple[str, int]:
    """Cue summary + priority (3 = most likely a disclosure)."""
    writing = _near(_WRITING, text, spans)
    use = _near(_USE, text, spans, window=60)
    non_use = bool(_NON_USE.search(text))
    in_place = location in _DISCLOSURE_PLACES
    if writing:
        return "writing_cue", 3
    if non_use and in_place:
        return "non_use_cue", 3
    if in_place:
        return "in_disclosure_place", 2
    if use:
        return "use_cue", 1
    return "mention_only", 0


def screen_dataset(data: Dict[int, Dict[str, dict]]) -> List[dict]:
    """One record per candidate paragraph (named tool anywhere, or generic AI wording plus a cue
    inside a disclosure place). References, title/author block and licence notes are excluded."""
    hits = []
    for year, papers in sorted(data.items()):
        for pid, paper in sorted(papers.items()):
            title = paper_title(paper)
            for i, par in enumerate(segment_paper(paper.get("full_text", ""))):
                if par["section_family"] in ("references", "header"):
                    continue
                text = par["text"]
                if re.match(r"^\s*-?\s*\[\d+\]", text):
                    continue
                if re.search(r"^\s*>?\s*©|licensed under a creative commons", text, re.I):
                    continue
                location = _location_for(par)
                spans, terms = [], []
                for name, rx in _TOOL_RES.items():
                    found = [(m.start(), m.end()) for m in rx.finditer(text)]
                    if found:
                        terms.append(name)
                        spans.extend(found)
                route = "named_tool"
                if not terms:
                    if location not in _DISCLOSURE_PLACES:
                        continue
                    g = [(m.start(), m.end()) for m in _GENERIC.finditer(text)]
                    if not g:
                        continue
                    if not (_near(_WRITING, text, g) or _near(_USE, text, g, 60) or _NON_USE.search(text)):
                        continue
                    spans, terms, route = g, ["generic AI wording"], "generic_wording"
                cue, score = _priority(text, location, spans)
                hits.append({
                    "hit_id": f"{year}-{pid}-p{i:03d}",          # stable across re-runs
                    "year": year, "paper_id": pid, "title": title,
                    "source_url": paper.get("metadata", {}).get("source_url", ""),
                    "paragraph_no": i,
                    "location_auto": location,
                    "section_heading": par["section_heading"],
                    "subsection_heading": par["subsection_heading"],
                    "matched_terms": ", ".join(terms),
                    "screen_route": route,
                    "cue": cue,
                    "priority": score,
                    "auto_flags": ", ".join(_flags(text, location, spans)),
                    "text": text[:3000],
                })
    return hits


def paper_counts(data: Dict[int, Dict[str, dict]], hits: List[dict]) -> List[dict]:
    """Per-year denominators, including how many papers HAVE each disclosure-relevant section."""
    rows = []
    for year, papers in sorted(data.items()):
        yh = [h for h in hits if h["year"] == year]
        secs = [paper_sections(p) for p in papers.values()]
        row = {"year": year, "papers_in_dataset": len(papers),
               "papers_with_any_candidate": len({h["paper_id"] for h in yh}),
               "papers_with_priority_1plus": len({h["paper_id"] for h in yh if h["priority"] >= 1}),
               "papers_with_priority_2plus": len({h["paper_id"] for h in yh if h["priority"] >= 2})}
        for k in ("has_acknowledgments", "has_ethics_statement", "has_dedicated_statement", "has_appendix"):
            row["papers_" + k] = sum(s[k] for s in secs)
        rows.append(row)
    return rows


# ==============================================================================================
# 5. CODING WORKBOOK
# ==============================================================================================

AUTO_COLS = ["hit_id", "year", "paper_id", "title", "source_url", "location_auto", "section_heading",
             "subsection_heading", "matched_terms", "screen_route", "cue", "priority", "auto_flags", "text"]
CODER_COLS = ["is_disclosure", "exclusion_reason", "location_verified", "coder", "notes"]
WIDTHS = {"hit_id": 18, "year": 6, "paper_id": 9, "title": 28, "source_url": 20, "location_auto": 18,
          "section_heading": 20, "subsection_heading": 14, "matched_terms": 15, "screen_route": 14,
          "cue": 16, "priority": 8, "auto_flags": 16, "text": 80, "is_disclosure": 12,
          "exclusion_reason": 20, "location_verified": 18, "coder": 12, "notes": 28}


def _split_rows(hits: List[dict]):
    rng = random.Random(RANDOM_SEED)
    to_code = sorted([h for h in hits if h["priority"] >= 1],
                     key=lambda h: (-h["priority"], bool(h["auto_flags"]), h["year"], h["paper_id"], h["paragraph_no"]))
    others = [h for h in hits if h["priority"] < 1]
    recall = rng.sample(others, min(RECALL_SAMPLE_SIZE, len(others)))
    recall_ids = {h["hit_id"] for h in recall}
    rest = [h for h in others if h["hit_id"] not in recall_ids]
    # Reliability sample: >= RELIABILITY_MIN rows, stratified so it contains likely disclosures
    # (priority >= 2) as well as ordinary candidates; otherwise almost every row is N and kappa breaks.
    pool = to_code + recall
    n_rel = min(len(pool), max(RELIABILITY_MIN, round(RELIABILITY_SHARE * len(pool))))
    strong = [h for h in pool if h["priority"] >= 2]
    weak = [h for h in pool if h["priority"] < 2]
    take_strong = min(len(strong), n_rel // 2)
    reliability = rng.sample(strong, take_strong) + rng.sample(weak, min(len(weak), n_rel - take_strong))
    reliability = sorted(reliability, key=lambda h: h["hit_id"])
    return to_code, sorted(recall, key=lambda h: h["hit_id"]), rest, reliability


def export_coding_workbook(hits: List[dict], data: Dict[int, Dict[str, dict]], path: str) -> None:
    """Sheets: to_code | recall_sample | other_mentions | reliability_10pct | paper_counts | coverage | codebook."""
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation

    bold = Font(bold=True)
    grey = PatternFill("solid", fgColor="ECE6DA")
    orange = PatternFill("solid", fgColor="FFF4E5")
    to_code, recall, rest, reliability = _split_rows(hits)

    def lists(ws, col_letter, options, last_row):
        dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{col_letter}2:{col_letter}{max(last_row, 2)}")

    def coding_sheet(ws, rows, coder_cols):
        cols = AUTO_COLS + coder_cols
        ws.append(cols)
        for c, name in enumerate(cols, 1):
            cell = ws.cell(row=1, column=c)
            cell.font = bold
            cell.fill = grey if name in AUTO_COLS else orange
            ws.column_dimensions[get_column_letter(c)].width = WIDTHS.get(name, 16)
        for r in rows:
            ws.append([r.get(c, "") for c in AUTO_COLS] + [""] * len(coder_cols))
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical="top")
        ws.freeze_panes = "B2"
        ws.auto_filter.ref = ws.dimensions
        last = len(rows) + 1
        for i, name in enumerate(coder_cols):
            letter = get_column_letter(len(AUTO_COLS) + i + 1)
            if name.startswith("is_disclosure"):
                lists(ws, letter, ["Y", "N", "Unsure"], last)
            elif name.startswith("exclusion_reason"):
                lists(ws, letter, EXCLUSION_REASONS, last)
            elif name.startswith("location"):
                lists(ws, letter, LOCATION_CODES, last)

    wb = Workbook()
    ws = wb.active
    ws.title = "to_code"
    coding_sheet(ws, to_code, CODER_COLS)
    coding_sheet(wb.create_sheet("recall_sample"), recall, CODER_COLS)
    coding_sheet(wb.create_sheet("other_mentions"), rest, CODER_COLS)
    rel_cols = []
    for name in CODER_NAMES:
        rel_cols += [f"is_disclosure__{name}", f"exclusion_reason__{name}", f"location_verified__{name}"]
    coding_sheet(wb.create_sheet("reliability_10pct"), reliability, rel_cols)

    def table_sheet(title, rows):
        ws = wb.create_sheet(title)
        if not rows:
            return
        ws.append(list(rows[0].keys()))
        for r in rows:
            ws.append(list(r.values()))
        for c in range(1, len(rows[0]) + 1):
            ws.cell(row=1, column=c).font = bold
            ws.column_dimensions[get_column_letter(c)].width = 24
    table_sheet("paper_counts", paper_counts(data, hits))
    table_sheet("coverage", coverage_report(data))

    ws = wb.create_sheet("codebook")
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 115
    for row in CODEBOOK:
        ws.append(row)
        ws.cell(row=ws.max_row, column=2).alignment = Alignment(wrap_text=True, vertical="top")
    for c in ws["A"]:
        c.font = bold
    wb.save(path)
    print(f"Saved {path}: to_code={len(to_code)}, recall_sample={len(recall)}, "
          f"other_mentions={len(rest)}, reliability_10pct={len(reliability)}")


CODEBOOK = [
    ("ITEM", "RULE"),
    ("Scope", "This workbook decides two things only: IS it an AI-use disclosure (the gate, shared by the "
              "whole group) and WHERE it sits (location). Tasks, specificity and statement type are coded "
              "by teammates on the master list exported afterwards (disclosures_master.xlsx)."),
    ("is_disclosure = Y", "The paper's OWN authors state that they used an AI tool, in producing the paper "
                          "(writing, editing, translating the text, code, figures) or as an instrument in the "
                          "research (translating stimuli, annotating, paraphrasing, summarising, generating or "
                          "checking data), OR they explicitly state that they did NOT use AI."),
    ("is_disclosure = N", "Anything else. Give the reason in exclusion_reason."),
    ("subject_of_study", "The AI tool is what is being studied, evaluated, benchmarked or compared."),
    ("method_component", "The AI model is part of the system or method the paper proposes (it is the "
                         "contribution itself, e.g. 'our pipeline uses an LLM encoder')."),
    ("third_party_use", "Someone else used the tool (related work, cited datasets, study participants)."),
    ("link_or_citation_only", "Only a URL or a reference to the tool, with no statement of use."),
    ("funding_or_name", "The term appears in a grant, project, centre or person's name."),
    ("general_discussion", "General remarks about AI (e.g. ethical concerns about generative AI)."),
    ("Unsure", "Mark Unsure and explain in notes; the group decides together."),
    ("location_verified", "Fill ONLY if location_auto is wrong. Location of the disclosure itself."),
    ("dedicated_statement", "A section or paragraph headed as an AI/LLM-use statement or disclosure."),
    ("ethics_statement", "Ethics statement / ethical considerations section."),
    ("acknowledgments", "Acknowledgments section."),
    ("body_text", "Any body section (abstract, introduction, method, experiments, results, discussion, "
                  "conclusion) and captions. The actual section is in section_heading."),
    ("footnote", "A footnote (in the Markdown: a short paragraph starting with its footnote number)."),
    ("appendix", "Appendix or supplementary material inside the PDF."),
    ("priority", "Script's guess. 3 = writing cue, or non-use cue in a disclosure place; 2 = inside a "
                 "disclosure place; 1 = 'we used / using <tool>'; 0 = plain mention."),
    ("auto_flags", "link_only, funding_or_name, likely_third_party: hints that the row is probably N. "
                   "Never decisive: read the text."),
    ("screen_route", "named_tool = a tool name was found. generic_wording = no tool name, but generic AI "
                     "wording plus a use/writing cue inside a disclosure place."),
    ("Sheet to_code", "Every priority >= 1 row. Coded by the primary coder."),
    ("Sheet recall_sample", f"{RECALL_SAMPLE_SIZE} random priority-0 rows. Code them all: the share of Y "
                            "estimates how many disclosures the screen ranks too low (screening recall)."),
    ("Sheet reliability_10pct", f"10% of the coded rows (at least {RELIABILITY_MIN}), half of them likely disclosures. "
                                "The primary coder's answers are taken from to_code / recall_sample automatically "
                                "(fill the Hemanth columns only to override); the second coder fills the "
                                "separate file made by export_second_coder_file() without seeing these answers. "
                                "Used for Cohen's kappa; report % agreement too, because kappa drops sharply "
                                "when nearly all rows are N."),
    ("Sheet other_mentions", "Remaining priority-0 rows. Not coded; kept for transparency."),
    ("Unit", "One row = one paragraph. A paper can have several disclosure paragraphs and locations."),
]


def export_second_coder_file(workbook_path: str, out_path: str, coder: str = "Second_coder") -> None:
    """A separate file with ONLY the reliability rows and empty coding columns, for the second coder.
    They never open the main workbook, so they cannot see the primary coder's answers."""
    import pandas as pd
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation

    rel = pd.read_excel(workbook_path, sheet_name="reliability_10pct", dtype=str).fillna("")
    show = ["hit_id", "year", "paper_id", "title", "source_url", "location_auto", "section_heading", "text"]
    cols = show + ["is_disclosure", "exclusion_reason", "location_verified", "notes"]
    wb = Workbook()
    ws = wb.active
    ws.title = "reliability"
    ws.append(cols)
    for c, name in enumerate(cols, 1):
        cell = ws.cell(row=1, column=c)
        cell.font = Font(bold=True)
        cell.fill = PatternFill("solid", fgColor="FFF4E5" if c > len(show) else "ECE6DA")
        ws.column_dimensions[get_column_letter(c)].width = WIDTHS.get(name, 16)
    for _, r in rel.iterrows():
        ws.append([r[c] for c in show] + ["", "", "", ""])
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "B2"
    last = max(len(rel) + 1, 2)
    for offset, options in ((0, ["Y", "N", "Unsure"]), (1, EXCLUSION_REASONS), (2, LOCATION_CODES)):
        letter = get_column_letter(len(show) + 1 + offset)
        dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{letter}2:{letter}{last}")
    cb = wb.create_sheet("codebook")
    cb.column_dimensions["A"].width = 26
    cb.column_dimensions["B"].width = 115
    for row in CODEBOOK:
        if row[0].startswith("Sheet ") or row[0] in ("priority", "auto_flags", "screen_route"):
            continue
        cb.append(row)
        cb.cell(row=cb.max_row, column=2).alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(out_path)
    print(f"Saved {out_path}: {len(rel)} rows for {coder}. Send them this file and the codebook sheet in it.")


# ==============================================================================================
# 6. RELIABILITY (Cohen's kappa, pairwise between coders)
# ==============================================================================================

def cohen_kappa(a: List[str], b: List[str]) -> Optional[float]:
    pairs = [(x, y) for x, y in zip(a, b) if x and y]
    n = len(pairs)
    if n == 0:
        return None
    labels = sorted({x for p in pairs for x in p})
    po = sum(x == y for x, y in pairs) / n
    pe = sum((sum(x == l for x, _ in pairs) / n) * (sum(y == l for _, y in pairs) / n) for l in labels)
    return 1.0 if pe == 1 else round((po - pe) / (1 - pe), 3)


def reliability(path: str, second_coder_file: Optional[str] = None, coders: Optional[List[str]] = None):
    """Pairwise kappa on the gate (is_disclosure) and on location (only rows both coders marked Y).
    If second_coder_file is given (made by export_second_coder_file and filled in by the teammate),
    its answers are merged in as the second coder's columns."""
    import pandas as pd
    coders = coders or CODER_NAMES
    df = pd.read_excel(path, sheet_name="reliability_10pct", dtype=str).fillna("")
    if second_coder_file:
        sec = pd.read_excel(second_coder_file, sheet_name="reliability", dtype=str).fillna("")
        sec = sec.set_index("hit_id")
        name = coders[1]
        for col in ("is_disclosure", "exclusion_reason", "location_verified"):
            df[f"{col}__{name}"] = df["hit_id"].map(sec[col]).fillna("")
    # Primary coder: if their reliability columns are empty, reuse their answers from to_code / recall_sample
    main = _coded_rows(path).set_index("hit_id")
    first = coders[0]
    for col in ("is_disclosure", "exclusion_reason", "location_verified"):
        key = f"{col}__{first}"
        if key not in df.columns:
            df[key] = ""
        empty = df[key] == ""
        df.loc[empty, key] = df.loc[empty, "hit_id"].map(main[col]).fillna("")
    rows = []
    for c1, c2 in combinations(coders, 2):
        g1, g2 = df[f"is_disclosure__{c1}"].str.upper(), df[f"is_disclosure__{c2}"].str.upper()
        both_y = (g1 == "Y") & (g2 == "Y")
        loc1 = df[f"location_verified__{c1}"].where(df[f"location_verified__{c1}"] != "", df["location_auto"])
        loc2 = df[f"location_verified__{c2}"].where(df[f"location_verified__{c2}"] != "", df["location_auto"])
        rows.append({"coder_a": c1, "coder_b": c2,
                     "n_rows_both_coded": int(((g1 != "") & (g2 != "")).sum()),
                     "agreement_is_disclosure_%": round(100 * (g1[(g1 != "") & (g2 != "")] == g2[(g1 != "") & (g2 != "")]).mean(), 1)
                     if ((g1 != "") & (g2 != "")).any() else None,
                     "kappa_is_disclosure": cohen_kappa(list(g1), list(g2)),
                     "n_rows_both_Y": int(both_y.sum()),
                     "agreement_location_%": round(100 * (loc1[both_y] == loc2[both_y]).mean(), 1) if both_y.any() else None,
                     "kappa_location": cohen_kappa(list(loc1[both_y]), list(loc2[both_y]))})
    out = pd.DataFrame(rows)
    valid = out["kappa_is_disclosure"].dropna()
    print(f"Mean pairwise kappa (is_disclosure): {valid.mean():.3f}" if len(valid) else
          "No overlapping coded rows yet.")
    return out


# ==============================================================================================
# 7. RESULTS FROM THE VERIFIED WORKBOOK
# ==============================================================================================

def _coded_rows(path: str):
    import pandas as pd
    frames = []
    for s in ("to_code", "recall_sample"):
        f = pd.read_excel(path, sheet_name=s, dtype=str).fillna("")
        f["sheet"] = s
        frames.append(f)
    df = pd.concat(frames, ignore_index=True)
    df["year"] = df["year"].astype(int)
    df["location"] = df["location_verified"].where(df["location_verified"] != "", df["location_auto"])
    df["is_disclosure"] = df["is_disclosure"].str.strip().str.upper()
    return df


def summarise_verified(path: str, data: Optional[Dict[int, Dict[str, dict]]] = None) -> dict:
    """Returns a dict of DataFrames:
      papers          one row per disclosing paper, with its locations
      by_paper        papers per year with >= 1 disclosure in each location (+ rate per year)
      by_disclosure   disclosure paragraphs per year per location
      availability    of papers HAVING an ethics statement / acknowledgments, how many disclose there
      recall          screening-recall estimate from the recall_sample sheet
      progress        how much has been coded
    """
    import pandas as pd
    df = _coded_rows(path)
    yes = df[df["is_disclosure"] == "Y"].copy()
    years = sorted(data.keys()) if data else sorted(df["year"].unique())
    locs = [c for c in LOCATION_CODES if c in set(yes["location"])] or LOCATION_CODES[:1]

    papers = (yes.groupby(["year", "paper_id", "title"])
              .agg(locations=("location", lambda s: ", ".join(sorted(set(s)))),
                   n_disclosure_paragraphs=("hit_id", "count"))
              .reset_index())

    by_paper = (yes.drop_duplicates(["year", "paper_id", "location"])
                .pivot_table(index="year", columns="location", values="paper_id", aggfunc="count", fill_value=0)
                .reindex(index=years, columns=locs).fillna(0).astype(int))
    by_paper["papers_disclosing"] = yes.groupby("year")["paper_id"].nunique().reindex(years).fillna(0).astype(int)
    by_paper["multi_location_papers"] = (papers[papers["locations"].str.contains(",")]
                                         .groupby("year").size().reindex(years).fillna(0).astype(int))
    if data:
        by_paper["papers_in_dataset"] = [len(data[y]) for y in years]
        by_paper["disclosure_rate_%"] = (100 * by_paper["papers_disclosing"] / by_paper["papers_in_dataset"]).round(1)
    by_paper.index.name = "year"

    by_disclosure = (yes.pivot_table(index="year", columns="location", values="hit_id", aggfunc="count", fill_value=0)
                     .reindex(index=years, columns=locs).fillna(0).astype(int))
    by_disclosure["total_paragraphs"] = by_disclosure.sum(axis=1)
    by_disclosure.index.name = "year"

    availability = None
    if data:
        rows = []
        for y in years:
            secs = {pid: paper_sections(p) for pid, p in data[y].items()}
            yy = yes[yes["year"] == y]
            for loc, key in (("ethics_statement", "has_ethics_statement"), ("acknowledgments", "has_acknowledgments"),
                             ("dedicated_statement", "has_dedicated_statement")):
                have = sum(s[key] for s in secs.values())
                used = yy.loc[yy["location"] == loc, "paper_id"].nunique()
                rows.append({"year": y, "section": loc, "papers_with_section": have,
                             "papers_disclosing_there": used,
                             "share_of_papers_with_section_%": round(100 * used / have, 1) if have else None})
        availability = pd.DataFrame(rows)

    rs = df[df["sheet"] == "recall_sample"]
    coded = rs[rs["is_disclosure"] != ""]
    n_y = int((coded["is_disclosure"] == "Y").sum())
    recall = pd.DataFrame([{
        "recall_rows_coded": len(coded), "recall_rows_total": len(rs), "Y_found_in_sample": n_y,
        "share_Y_in_sample_%": round(100 * n_y / len(coded), 1) if len(coded) else None,
        "note": "Y in this sample = disclosures the screen ranked as priority 0 (would have been missed)."}])

    tc = df[df["sheet"] == "to_code"]
    progress = pd.DataFrame([{
        "to_code_rows": len(tc), "to_code_coded": int((tc["is_disclosure"] != "").sum()),
        "recall_rows": len(rs), "recall_coded": len(coded),
        "Y": int((df["is_disclosure"] == "Y").sum()), "N": int((df["is_disclosure"] == "N").sum()),
        "Unsure": int((df["is_disclosure"] == "UNSURE").sum())}])

    return {"papers": papers, "by_paper": by_paper, "by_disclosure": by_disclosure,
            "availability": availability, "recall": recall, "progress": progress}


def plot_locations(by_paper, path: Optional[str] = None):
    """Stacked bars: papers with a disclosure in each location, per year."""
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    cols = [c for c in LOCATION_CODES if c in by_paper.columns]
    ax = by_paper[cols].plot(kind="bar", stacked=True, figsize=(9, 4.5), width=0.7, rot=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel("Year")
    ax.set_ylabel("Papers with a disclosure here")
    ax.set_title("Where ISMIR papers place AI-use disclosures")
    ax.legend(title="Location", bbox_to_anchor=(1.01, 1), loc="upper left", frameon=False)
    plt.tight_layout()
    if path:
        plt.savefig(path, dpi=200)
    return ax


# ==============================================================================================
# 8. HAND-OFF TO TEAMMATES
# ==============================================================================================

def export_disclosure_list(coded_path: str, out_path: str) -> None:
    """Master list of verified disclosures (is_disclosure = Y). Teammates add their own columns
    (tasks, specificity, statement type) to their copy, keyed by disclosure_id. This file has no
    columns of theirs, so nobody overwrites anybody."""
    df = _coded_rows(coded_path)
    yes = df[df["is_disclosure"] == "Y"].sort_values(["year", "paper_id", "hit_id"])
    out = yes.rename(columns={"hit_id": "disclosure_id"})[
        ["disclosure_id", "year", "paper_id", "title", "source_url", "location", "section_heading", "text"]]
    out.to_excel(out_path, index=False)
    print(f"Saved {out_path}: {len(out)} disclosure paragraphs from {out['paper_id'].nunique()} papers "
          f"({out.groupby(['year', 'paper_id']).ngroups} paper-years).")
