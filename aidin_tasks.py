"""
aidin_tasks.py: TASKS coding of AI-use disclosures (RQ2: which tasks do disclosures report?)
MERE project (AI Tool Disclosure in Sound & Music Computing). Owner: tasks dimension (Aidin).

Input:  disclosures_master.xlsx  (verified disclosures from the shared gate, keyed by disclosure_id;
        made by export_disclosure_list() in rj_disclosure_location.py)
Output: aidin_tasks_coding.xlsx  (one row per disclosure paragraph, one 0/1 column per task)

Workflow (see aidin_tasks.ipynb):
    master = load_master("disclosures_master.xlsx")
    export_coding_workbook(master, "aidin_tasks_coding.xlsx")   # keyword pre-coding
    ... the coder reads every paragraph and corrects the task columns in Excel ...
    res = summarise("aidin_tasks_coding.xlsx")                   # tables for the paper

Unit of analysis: the disclosure paragraph (as in the location dimension). A paragraph can report
several tasks (multi-label). Results are given per paragraph and per paper.
"""

from __future__ import annotations

import re
from typing import Dict, List

# ==============================================================================================
# 1. CODEBOOK
# ==============================================================================================
# Level 1 = stage of the research process. Level 2 = task.
# Paper-production tasks come from RQ2 (decided before coding, deductive). Research-instrument
# tasks were added after a first reading of the disclosures (inductive), because most disclosures
# describe AI used inside the research rather than for writing the paper.

STAGES = {
    "paper_production": "AI used to produce the paper itself (text, code, figures, literature).",
    "research_instrument": "AI used inside the research to do work a researcher could have done by hand.",
    "other": "No task can be identified, or the statement declares non-use.",
}

TASKS: Dict[str, dict] = {
    # --- paper production (deductive, from RQ2) ---
    "language_editing": {
        "stage": "paper_production",
        "definition": "Writing, editing, proofreading, grammar or wording of the paper's text.",
        "regex": r"proof-?read\w*|grammar|grammatical|spell(ing)?[- ]?check\w*|polish\w*|"
                 r"language (editing|improvement|correction)|rephras\w* (the|our) (text|paper|manuscript)|"
                 r"writing (assistan\w+|support)|wording",
    },
    "translation_text": {
        "stage": "paper_production",
        "definition": "Translating the paper's own text.",
        "regex": r"translat\w*[^.]{0,40}\b(this|the|our) (paper|manuscript|article)\b|"
                 r"\b(paper|manuscript)\b[^.]{0,40}translat\w*",
    },
    "coding": {
        "stage": "paper_production",
        "definition": "Writing or debugging code (for the analysis, the experiments or the figures).",
        "regex": r"code generation|generat\w* (the )?code|coding assistan\w*|copilot|debug\w*|"
                 r"programming assistan\w*",
    },
    "literature": {
        "stage": "paper_production",
        "definition": "Searching, reading or summarising the literature / related work.",
        "regex": r"literature (search|review)|related work|search(ing)? for (papers|references)",
    },
    "data_analysis": {
        "stage": "paper_production",
        "definition": "Analysing the results (statistics, interpretation).",
        "regex": r"statistical analys\w*|analy[sz](e|ed|ing) (the )?(results|data)",
    },
    "figures": {
        "stage": "paper_production",
        "definition": "Making figures, plots or visualisations for the paper.",
        "regex": r"visuali[sz]ation\w*|\bplots?\b|\bfigures?\b(?! \d)",
    },
    # --- research instrument (inductive, from the data) ---
    "data_generation": {
        "stage": "research_instrument",
        "definition": "Generating data the study uses: text prompts, synthetic lyrics, captions, "
                      "descriptions, stimuli.",
        "regex": r"(generat\w*|creat\w*|produc\w*|synthes\w*)[^.]{0,60}\b(prompts?|lyrics|captions?|"
                 r"data(set)?s?|samples?|descriptions?|stimuli|dialogues?|utterances?)\b|"
                 r"\b(prompts?|lyrics|captions?|descriptions?|samples?)\b[^.]{0,40}\b(generated|created|produced)\b|"
                 r"\bsynthetic\b",
    },
    "annotation_judging": {
        "stage": "research_instrument",
        "definition": "Labelling, annotating or categorising items, or judging their quality "
                      "(LLM as annotator or judge).",
        "regex": r"prompt\w* (it|them) to (automatically )?(label|annotate|categori[sz]e|classify)|"
                 r"to (automatically )?(label|annotate|categori[sz]e|classify)\b|(labell?ed|annotated) by|"
                 r"evaluate whether|assess\w* (the )?(quality|whether)|judg\w*|made sense",
    },
    "summarising_paraphrasing": {
        "stage": "research_instrument",
        "definition": "Summarising, paraphrasing or rewriting research material (lyrics, tags, captions).",
        "regex": r"summar\w*|paraphras\w*|rewr(i|o)t\w*|transform\w* (them |it )?into",
    },
    "translation_materials": {
        "stage": "research_instrument",
        "definition": "Translating study materials (instructions, stimuli, datasets).",
        "regex": r"translat\w*",
    },
    "decision_support": {
        "stage": "research_instrument",
        "definition": "Consulting the tool to support a design decision (e.g. choosing genres).",
        "regex": r"supported (using|by)|affirm\w*|help\w* (us )?(to )?(choose|select|decide)",
    },
    # --- other ---
    "explicit_non_use": {
        "stage": "other",
        "definition": "The authors state that they did NOT use AI for some part of the work.",
        "regex": r"\bno (generative )?(ai|llms?|language models?)\b|\b(did not|didn't|were not|was not) "
                 r"(use|used)\b[^.]{0,40}\b(ai|llms?|chatgpt)\b",
    },
    "unspecified": {
        "stage": "other",
        "definition": "AI use is stated but the task cannot be identified.",
        "regex": None,   # set automatically when nothing else matches
    },
}
TASK_COLS: List[str] = list(TASKS)

# translation of the paper's text wins over translation of materials
_OVERRIDES = {"translation_text": "translation_materials"}

# Tool mentions (to find the sentences that talk about the AI tool)
TOOL_RX = re.compile(
    r"\bchat\s?-?gpt\b|\bgpt-?\s?\d(\.\d)?(o|-turbo)?\b|\bgpt-?4o\b|\bopenai\b|\bclaude\b|\bgemini\b|"
    r"\bcopilot\b|\bgrammarly\b|\bdeepl\b|\bllms?\b|\blarge language models?\b|\bgen(erative)?\s?ai\b|"
    r"\bai tools?\b|\bbloom\b|\bqwen\b|\bself-instruct\b",
    re.I,
)
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z“\"(])")


# ==============================================================================================
# 2. PRE-CODING (keyword hints; every paragraph is then read and corrected by hand)
# ==============================================================================================

def load_master(path: str):
    import pandas as pd
    df = pd.read_excel(path, dtype=str).fillna("")
    df["year"] = df["year"].astype(int)
    return df


def ai_sentences(text: str) -> List[str]:
    """Sentences of the paragraph that mention an AI tool (the task is coded from these)."""
    clean = re.sub(r"<sup>.*?</sup>", "", text)          # footnote markers break sentence splitting
    sents = _SENT_SPLIT.split(" ".join(clean.split()))
    return [s for s in sents if TOOL_RX.search(s)]


def tools_mentioned(text: str) -> str:
    found = []
    for m in TOOL_RX.finditer(text):
        t = m.group(0).strip()
        if t.lower() not in [f.lower() for f in found]:
            found.append(t)
    return ", ".join(found)


def precode(text: str) -> Dict[str, int]:
    """Keyword pre-coding of one disclosure paragraph. Returns {task: 0/1}."""
    sents = " ".join(ai_sentences(text)) or text
    codes = {t: 0 for t in TASK_COLS}
    for task, spec in TASKS.items():
        if spec["regex"] and re.search(spec["regex"], sents, re.I):
            codes[task] = 1
    for winner, loser in _OVERRIDES.items():
        if codes[winner]:
            codes[loser] = 0
    if not any(codes[t] for t in TASK_COLS if t != "unspecified"):
        codes["unspecified"] = 1
    return codes


# ==============================================================================================
# 3. CODING WORKBOOK
# ==============================================================================================

INFO_COLS = ["disclosure_id", "year", "paper_id", "title", "location", "section_heading",
             "tools_mentioned", "ai_sentences"]
WIDTHS = {"disclosure_id": 18, "year": 6, "paper_id": 9, "title": 28, "location": 14,
          "section_heading": 18, "tools_mentioned": 16, "ai_sentences": 70, "notes": 30, "text": 90}


def export_coding_workbook(master, path: str) -> None:
    """Sheets: coding (edit the orange task columns) | auto_labels (untouched pre-codes) | codebook."""
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation

    grey, orange = PatternFill("solid", fgColor="ECE6DA"), PatternFill("solid", fgColor="FFF4E5")
    rows = []
    for _, r in master.iterrows():
        rec = {c: r.get(c, "") for c in INFO_COLS if c in master.columns}
        rec["tools_mentioned"] = tools_mentioned(r["text"])
        rec["ai_sentences"] = " | ".join(ai_sentences(r["text"]))
        rec.update(precode(r["text"]))
        rec["notes"] = ""
        rec["text"] = r["text"]
        rows.append(rec)

    def sheet(ws, cols, editable):
        ws.append(cols)
        for c, name in enumerate(cols, 1):
            cell = ws.cell(row=1, column=c)
            cell.font = Font(bold=True)
            cell.fill = orange if name in editable else grey
            ws.column_dimensions[get_column_letter(c)].width = WIDTHS.get(name, 11)
        for rec in rows:
            ws.append([rec.get(c, "") for c in cols])
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical="top")
        ws.freeze_panes = "B2"
        ws.auto_filter.ref = ws.dimensions

    cols = INFO_COLS + TASK_COLS + ["notes", "text"]
    wb = Workbook()
    ws = wb.active
    ws.title = "coding"
    sheet(ws, cols, editable=set(TASK_COLS) | {"notes"})
    dv = DataValidation(type="list", formula1='"1,0"', allow_blank=True)
    ws.add_data_validation(dv)
    first = get_column_letter(len(INFO_COLS) + 1)
    last = get_column_letter(len(INFO_COLS) + len(TASK_COLS))
    dv.add(f"{first}2:{last}{len(rows) + 1}")

    sheet(wb.create_sheet("auto_labels"), ["disclosure_id"] + TASK_COLS, editable=set())

    cb = wb.create_sheet("codebook")
    cb.column_dimensions["A"].width = 26
    cb.column_dimensions["B"].width = 22
    cb.column_dimensions["C"].width = 100
    cb.append(["task", "stage", "definition"])
    for t, spec in TASKS.items():
        cb.append([t, spec["stage"], spec["definition"]])
    cb.append([])
    for line in CODING_RULES:
        cb.append(["rule", "", line])
    for row in cb.iter_rows():
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    for c in cb[1]:
        c.font = Font(bold=True)
    wb.save(path)
    print(f"Saved {path}: {len(rows)} disclosure paragraphs from "
          f"{master[['year', 'paper_id']].drop_duplicates().shape[0]} papers.")


CODING_RULES = [
    "Code what the AUTHORS used the AI tool for, from the sentences that mention the tool "
    "(column ai_sentences); read the full paragraph (column text) for context.",
    "Put 1 in every task that applies (multi-label). Leave 0 or empty otherwise.",
    "The pre-filled 1s are keyword hints only. Read every paragraph and correct them; "
    "the sheet auto_labels keeps the untouched hints for comparison.",
    "Text prompts, synthetic lyrics, captions or stimuli made by the tool = data_generation.",
    "Tool labels, annotates or judges items = annotation_judging.",
    "Tool summarises, paraphrases or rewrites research material = summarising_paraphrasing.",
    "Translation of the paper's text = translation_text; of instructions, stimuli or data = "
    "translation_materials.",
    "A statement that AI was NOT used for something = explicit_non_use (plus any task that WAS done).",
    "Use unspecified only if no task can be identified.",
]


# ==============================================================================================
# 4. RESULTS
# ==============================================================================================

def _read_coding(path: str, sheet: str = "coding"):
    import pandas as pd
    df = pd.read_excel(path, sheet_name=sheet, dtype=str).fillna("")
    for t in TASK_COLS:
        df[t] = df[t].apply(lambda v: 1 if str(v).strip() in ("1", "1.0") else 0)
    if "year" in df.columns:
        df["year"] = df["year"].astype(int)
    return df


def summarise(path: str) -> dict:
    """Returns DataFrames:
      tasks          paragraphs and papers per task (with stage), most frequent first
      by_year        papers per task per year
      stages         papers and paragraphs per stage
      per_paper      one row per paper with its tasks
      auto_vs_final  agreement between the keyword hints and the final codes
    """
    import pandas as pd
    df = _read_coding(path)
    long = df.melt(id_vars=["disclosure_id", "year", "paper_id"], value_vars=TASK_COLS,
                   var_name="task", value_name="coded")
    long = long[long["coded"] == 1].copy()
    long["stage"] = long["task"].map(lambda t: TASKS[t]["stage"])
    long["paper"] = long["year"].astype(str) + "/" + long["paper_id"]

    tasks = (long.groupby(["stage", "task"])
             .agg(paragraphs=("disclosure_id", "nunique"), papers=("paper", "nunique"))
             .reset_index().sort_values(["papers", "paragraphs"], ascending=False))
    total_papers = df.assign(paper=df["year"].astype(str) + "/" + df["paper_id"])["paper"].nunique()
    tasks["share_of_disclosing_papers_%"] = (100 * tasks["papers"] / total_papers).round(1)

    by_year = (long.drop_duplicates(["paper", "task"])
               .pivot_table(index="task", columns="year", values="paper", aggfunc="count", fill_value=0))

    stages = (long.groupby("stage")
              .agg(paragraphs=("disclosure_id", "nunique"), papers=("paper", "nunique")).reset_index())

    per_paper = (long.groupby(["year", "paper_id"])
                 .agg(tasks=("task", lambda s: ", ".join(sorted(set(s)))),
                      stages=("stage", lambda s: ", ".join(sorted(set(s)))))
                 .reset_index())

    auto = _read_coding(path, "auto_labels").set_index("disclosure_id")
    final = df.set_index("disclosure_id")
    decisions = len(final) * len(TASK_COLS)
    same = sum(int(auto.loc[i, t] == final.loc[i, t]) for i in final.index for t in TASK_COLS)
    changed = [(i, t, int(auto.loc[i, t]), int(final.loc[i, t]))
               for i in final.index for t in TASK_COLS if auto.loc[i, t] != final.loc[i, t]]
    auto_vs_final = pd.DataFrame([{"decisions": decisions, "same": same,
                                   "agreement_%": round(100 * same / decisions, 1),
                                   "paragraphs_changed": len({c[0] for c in changed}),
                                   "changes": "; ".join(f"{i}:{t} {a}->{b}" for i, t, a, b in changed)}])
    return {"tasks": tasks, "by_year": by_year, "stages": stages, "per_paper": per_paper,
            "auto_vs_final": auto_vs_final, "n_papers": total_papers, "n_paragraphs": len(df)}


# ==============================================================================================
# 5. FIGURE
# ==============================================================================================

TASK_LABELS = {
    "data_generation": "Data / prompt generation",
    "summarising_paraphrasing": "Summarising / paraphrasing",
    "annotation_judging": "Annotation / judging",
    "translation_materials": "Translating study materials",
    "decision_support": "Decision support",
    "language_editing": "Language editing",
    "translation_text": "Translating the paper",
    "coding": "Coding",
    "literature": "Literature search / review",
    "data_analysis": "Data analysis",
    "figures": "Figures",
    "explicit_non_use": "Explicit non-use",
    "unspecified": "Unspecified",
}
STAGE_LABELS = {"research_instrument": "AI as a research instrument",
                "paper_production": "AI for producing the paper",
                "other": "Other"}
# Categorical slots 1-3 of the reference palette (validated: CVD dE >= 9.2, normal-vision >= 27.6)
STAGE_COLORS = {"research_instrument": "#2a78d6", "paper_production": "#eb6834", "other": "#1baf7a"}
INK, INK_2, GRID = "#0b0b0b", "#52514e", "#e4e3df"


def plot_tasks(path_coding: str, out_png: str = None, show_zero: bool = True):
    """Horizontal bars: papers reporting each task, grouped and coloured by stage.
    Zero rows are kept on purpose: they show which planned (deductive) codes never occurred."""
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch

    res = summarise(path_coding)
    counts = res["tasks"].set_index("task")["papers"].to_dict()
    n = res["n_papers"]
    order = []
    for stage in ("research_instrument", "paper_production", "other"):
        ts = [t for t in TASK_COLS if TASKS[t]["stage"] == stage and (show_zero or counts.get(t, 0))]
        order += sorted(ts, key=lambda t: -counts.get(t, 0))
    order = order[::-1]                                   # matplotlib draws bottom-up
    vals = [counts.get(t, 0) for t in order]

    fig, ax = plt.subplots(figsize=(7.2, 0.32 * len(order) + 1.3), dpi=200)
    fig.patch.set_facecolor("white")
    ax.barh(range(len(order)), vals, height=0.55,
            color=[STAGE_COLORS[TASKS[t]["stage"]] for t in order], zorder=3)
    for i, v in enumerate(vals):
        label = f"{v} ({100 * v / n:.0f}%)" if v else "0"
        ax.text(v + 0.12, i, label, va="center", ha="left", fontsize=8, color=INK_2 if v else "#8a8985")
    ax.set_yticks(range(len(order)))
    ax.set_yticklabels([TASK_LABELS[t] for t in order], fontsize=8.5, color=INK)
    ax.set_xlim(0, max(vals) + 1.6)
    ax.set_xlabel(f"Papers reporting the task (of {n} disclosing papers)", fontsize=8.5, color=INK_2)
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.tick_params(axis="x", labelsize=8, colors=INK_2, length=0)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color=GRID, linewidth=0.8, zorder=0)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    stages_used = [s for s in ("research_instrument", "paper_production", "other")
                   if any(TASKS[t]["stage"] == s for t in order)]
    ax.legend(handles=[Patch(color=STAGE_COLORS[s], label=STAGE_LABELS[s]) for s in stages_used],
              loc="lower right", frameon=False, fontsize=8)
    ax.set_title("Tasks reported in AI-use disclosures, ISMIR 2021-2025", fontsize=10, color=INK,
                 loc="left", pad=10)
    fig.tight_layout()
    if out_png:
        fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
    return fig, ax
