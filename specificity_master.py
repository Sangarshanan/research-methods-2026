"""
specificity_master.py: SPECIFICITY of the AI-use disclosures, coded on the shared list
(disclosures_master.xlsx, 15 paragraphs, 14 papers), keyed by disclosure_id.

Scale (Tirna's four levels, applied with one consistent rule):
    1 Low             no tool named ("an LLM", "large language models", "generative AI")
    2 Moderate        product or platform named, no model version ("ChatGPT", "Claude")
    3 High            model and version named ("GPT-3.5", "GPT-4")
    4 Extremely high  exact model variant ("GPT-4o", "GPT-3.5-turbo", "Claude 3.5 Sonnet", "Gemini 1.0 Pro")

Rule: for each disclosure, score the most specific name the paper gives for the tool used for
THAT task, anywhere in the paper (only 2024/14 names it more precisely outside the disclosure
paragraph). Tirna's original scores are kept next to the final ones, with the Excel row they come from.

Run:  python specificity_master.py      -> specificity_coding.xlsx, specificity_by_year.csv,
                                           specificity_figure.png
"""

from __future__ import annotations

LEVELS = {1: "Low", 2: "Moderate", 3: "High", 4: "Extremely high"}

# disclosure_id: (tool name used for the score, final level, Tirna row(s) in Specificity RM-TG.xlsx,
#                 Tirna's original level, human verification of the AI output reported, note)
CODES = {
    "2023-000047-p080": ("ChatGPT", 2, "2", "high", False,
                         "ChatGPT without version = Moderate by the scale; original said High."),
    "2024-000014-p078": ("GPT-4 (named in abstract and Sec. 2 for the same synthetic lyrics)", 3, "6, 7",
                         "extremely high", False,
                         "Disclosure paragraph (ethics statement) only says 'large language models'; "
                         "the paper names GPT-4 for the same task. GPT-4 = High by the scale."),
    "2024-000027-p044": ("ChatGPT", 2, "8", "moderate", False,
                         "Same. Row 9 (Sony statement about AI) is not a disclosure and is dropped."),
    "2024-000032-p042": ("ChatGPT", 2, "10", "moderate", False, "Same."),
    "2024-000032-p047": ("ChatGPT", 2, "11", "moderate", False, "Same."),
    "2024-000075-p026": ("GPT-4", 3, "", "", False,
                         "Not scored before. Row 13 (labelled 2024/90) quotes another sentence of this "
                         "paper (its own multi-agent method), not this disclosure."),
    "2024-000090-p035": ("Gemini 1.0 Pro", 4, "12", "extremely high", False, "Same."),
    "2024-000099-p058": ("GPT-3.5", 3, "15", "high", False,
                         "Same. Row 14 (third-party LP-MusicCaps captions) is not a disclosure and is dropped."),
    "2024-000112-p038": ("ChatGPT", 2, "16", "moderate", False,
                         "Same. Rows 17 and 18 come from paper 2024/104, not 2024/112, and are dropped."),
    "2025-000001-p035": ("GPT-4o", 4, "20", "extremely high", False,
                         "Same level; original quote was a reference-list entry, now scored on the disclosure."),
    "2025-000029-p070": ("Claude 3.7 Sonnet", 4, "21", "extremely high", True,
                         "Same. Authors checked Claude's judgements and report its errors."),
    "2025-000045-p046": ("GPT-4o", 4, "22", "extremely high", True,
                         "Same level; original quote was a reference-list entry. Captions were reviewed "
                         "and refined by a human music expert."),
    "2025-000060-p070": ("Claude 3.5 Sonnet", 4, "23", "extremely high", False, "Same."),
    "2025-000062-p085": ("none ('a LLM')", 1, "24", "low", False, "Same. No model named anywhere in the paper."),
    "2025-000087-p111": ("none ('generative AI tools', 'code generation')", 1, "", "", False,
                         "Not scored before. Non-use statement for the text; the code tool is not named."),
}

DROPPED_TIRNA_ROWS = {
    "3": "2023/40, not in the final list (AI is the paper's own method)",
    "4": "2023/48, not in the final list (LLM captioning is the paper's contribution)",
    "5": "2023/48, not in the final list",
    "9": "2024/27, general statement about AI by Sony, not a disclosure",
    "13": "labelled 2024/90 but quoted from 2024/75 (its multi-agent method), not a disclosure",
    "14": "2024/99, third-party dataset captions, not the authors' own use",
    "17": "labelled 2024/112 but quoted from 2024/104, not in the final list",
    "18": "labelled 2024/112 but quoted from 2024/104, not in the final list",
    "19": "2024/111, not in the final list (GPT is the subject of study)",
    "25": "2025/26, not in the final list (borderline: LLM-made captions for the paper's own dataset)",
}


def build(master_path="disclosures_master.xlsx", out_xlsx="specificity_coding.xlsx",
          out_csv="specificity_by_year.csv", out_png="specificity_figure.png"):
    import pandas as pd
    master = pd.read_excel(master_path, dtype=str).fillna("")
    master["year"] = master["year"].astype(int)
    missing = set(master["disclosure_id"]) ^ set(CODES)
    assert not missing, f"disclosure_id mismatch with the master list: {missing}"

    rows = []
    for _, r in master.iterrows():
        tool, lvl, trow, tlvl, human, note = CODES[r["disclosure_id"]]
        rows.append({"disclosure_id": r["disclosure_id"], "year": r["year"], "paper_id": r["paper_id"],
                     "title": r["title"], "location": r["location"], "tool_named": tool,
                     "specificity_level": lvl, "specificity_label": LEVELS[lvl],
                     "tirna_row": trow, "tirna_original": tlvl,
                     "changed": "yes" if (tlvl and tlvl.replace("etremely", "extremely") != LEVELS[lvl].lower())
                                or not tlvl else "no",
                     "human_verification": "yes" if human else "no", "note": note, "text": r["text"]})
    df = pd.DataFrame(rows)

    def summary(frame, unit):
        g = frame.groupby("year")["specificity_level"]
        out = pd.DataFrame({"n": g.size(), "mean": g.mean().round(2), "sd": g.std().round(2)})
        for k, name in LEVELS.items():
            out[name] = frame[frame.specificity_level == k].groupby("year").size().reindex(out.index).fillna(0).astype(int)
        tot = pd.DataFrame({"n": [len(frame)], "mean": [round(frame.specificity_level.mean(), 2)],
                            "sd": [round(frame.specificity_level.std(), 2)],
                            **{name: [int((frame.specificity_level == k).sum())] for k, name in LEVELS.items()}},
                           index=["all"])
        out = pd.concat([out, tot])
        out["high_or_extremely_high_%"] = (100 * (out["High"] + out["Extremely high"]) / out["n"]).round(1)
        out.insert(0, "unit", unit)
        out.index.name = "year"
        return out

    per_par = summary(df, "paragraphs")
    per_paper = summary(df.drop_duplicates(["year", "paper_id"]), "papers")
    by_year = pd.concat([per_par, per_paper])
    by_year.to_csv(out_csv)

    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    with pd.ExcelWriter(out_xlsx, engine="openpyxl") as xw:
        df.to_excel(xw, sheet_name="coding", index=False)
        by_year.to_excel(xw, sheet_name="by_year")
        pd.DataFrame([{"tirna_row": k, "why_dropped": v} for k, v in DROPPED_TIRNA_ROWS.items()]) \
            .to_excel(xw, sheet_name="dropped_tirna_rows", index=False)
        pd.DataFrame([{"level": k, "label": v} for k, v in LEVELS.items()] +
                     [{"level": "rule", "label": "Most specific name the paper gives for the tool used for this "
                                                 "task, anywhere in the paper. GPT-4 and GPT-3.5 = High; "
                                                 "GPT-4o, GPT-3.5-turbo, Claude 3.x Sonnet, Gemini 1.0 Pro = "
                                                 "Extremely high."}]).to_excel(xw, sheet_name="scale", index=False)
        widths = {"disclosure_id": 18, "title": 30, "tool_named": 30, "note": 60, "text": 80, "tirna_original": 14,
                  "specificity_label": 14, "human_verification": 12}
        for name, ws in xw.sheets.items():
            for c, cell in enumerate(ws[1], 1):
                cell.font = Font(bold=True)
                cell.fill = PatternFill("solid", fgColor="ECE6DA")
                ws.column_dimensions[get_column_letter(c)].width = widths.get(str(cell.value), 16)
            for row in ws.iter_rows(min_row=2):
                for cell in row:
                    cell.alignment = Alignment(wrap_text=True, vertical="top")
            ws.freeze_panes = "B2"
    plot(df, out_png)
    return df, by_year


def plot(df, out_png):
    """Stacked bars: disclosure paragraphs per year by specificity level (ordered, one-hue ramp)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    ramp = {1: "#c7dbf5", 2: "#86b0ea", 3: "#3f7fd8", 4: "#1d4f9c"}     # light -> dark = low -> high
    years = sorted(df.year.unique())
    fig, ax = plt.subplots(figsize=(6.4, 3.4), dpi=200)
    bottom = [0] * len(years)
    for k in (1, 2, 3, 4):
        vals = [int(((df.year == y) & (df.specificity_level == k)).sum()) for y in years]
        ax.bar([str(y) for y in years], vals, bottom=bottom, width=0.5, color=ramp[k],
               edgecolor="white", linewidth=1.5, label=f"{k} {LEVELS[k]}", zorder=3)
        bottom = [b + v for b, v in zip(bottom, vals)]
    for i, y in enumerate(years):
        m = df[df.year == y].specificity_level.mean()
        ax.text(i, bottom[i] + 0.2, f"mean {m:.1f}", ha="center", va="bottom", fontsize=8, color="#52514e")
    ax.set_ylabel("Disclosure paragraphs", fontsize=8.5, color="#52514e")
    ax.set_ylim(0, max(bottom) + 1.5)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.tick_params(labelsize=8, colors="#52514e", length=0)
    ax.grid(axis="y", color="#e4e3df", linewidth=0.8, zorder=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#e4e3df")
    handles, labels = ax.get_legend_handles_labels()       # legend top-down = stack top-down
    ax.legend(handles[::-1], labels[::-1], title="Specificity", fontsize=7.5, title_fontsize=8, frameon=False,
              loc="upper left", bbox_to_anchor=(1.01, 1))
    ax.set_title("Specificity of AI-use disclosures, ISMIR 2023-2025", fontsize=9.5, loc="left")
    fig.tight_layout()
    fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    df, by_year = build()
    print(df[["disclosure_id", "tool_named", "specificity_level", "tirna_original", "changed",
              "human_verification"]].to_string(index=False))
    print()
    print(by_year.to_string())
