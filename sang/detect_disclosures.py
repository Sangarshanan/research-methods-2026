#!/usr/bin/env python3
"""
Scan ISMIR paper markdown files for AI usage disclosures and classify them.

Usage:
  python3 detect_disclosures.py --data-dir dataset --output-dir results/
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

# LEXICONS
AI_TOOLS: Dict[str, str] = {
    "chatgpt": "ChatGPT",
    "chat gpt": "ChatGPT",
    "gpt-4o": "GPT-4o",
    "gpt-4": "GPT-4",
    "gpt4": "GPT-4",
    "gpt-3.5": "GPT-3.5",
    "gpt-3": "GPT-3",
    "gpt3": "GPT-3",
    "openai": "OpenAI",
    "claude": "Claude", 
    "copilot": "Copilot",
    "github copilot": "GitHub Copilot",
    "gemini": "Gemini", 
    "bard": "Bard",     
    "llama": "LLaMA",
    "llama 2": "LLaMA 2",
    "llama 3": "LLaMA 3",
    "mistral": "Mistral",
    "grammarly": "Grammarly",
    "deepl": "DeepL",
    "dall-e": "DALL-E",
    "dalle": "DALL-E",
    "midjourney": "Midjourney",
    "stable diffusion": "Stable Diffusion",
    "whisper": "Whisper",
    "bloom": "BLOOM",
    "qwen": "Qwen",
    "palm": "PaLM",
    "falcon": "Falcon",
    "mixtral": "Mixtral",
}

# Sorted longest-first so multi-word keys match before substrings
AI_TOOLS_SORTED = sorted(AI_TOOLS.keys(), key=len, reverse=True)

AI_CONCEPTS_PATTERNS: List[Tuple[re.Pattern, str]] = [
    (re.compile(r"\blarge language models?\b", re.I), "Large Language Model"),
    (re.compile(r"\bllms?\b", re.I), "LLM"),
    (re.compile(r"\bgenerative ai\b", re.I), "Generative AI"),
    (re.compile(r"\bgenerative artificial intelligence\b", re.I), "Generative AI"),
    (re.compile(r"\bfoundation models?\b", re.I), "Foundation Model"),
    (re.compile(r"\bai assistants?\b", re.I), "AI Assistant"),
    (re.compile(r"\bai tools?\b", re.I), "AI Tool"),
    (re.compile(r"\bai-generated\b", re.I), "AI-Generated"),
    (re.compile(r"\bai-assisted\b", re.I), "AI-Assisted"),
    (re.compile(r"\bai was used\b", re.I), "AI Was Used"),
    (re.compile(r"\btext generation\b", re.I), "Text Generation"),
    (re.compile(r"\bnatural language generation\b", re.I), "Natural Language Generation"),
]

AMBIGUOUS_TOOLS: Dict[str, Dict[str, List[str]]] = {
    "claude": {
        "confirm": [
            r"claude[\s\-]?\d",
            r"anthropic",
            r"claude\s+(?:ai|sonnet|haiku|opus|instant)",
            r"claude\.ai",
        ],
        "reject": [
            r"claude\s+[A-Z][a-z]+",
            r"latour",
            r"debussy",
        ],
    },
    "bard": {
        "confirm": [
            r"google\s+bard",
            r"bard\s+(?:ai|chatbot|api|chat)",
        ],
        "reject": [
            r"\bthe\s+bard\b",
            r"shakespeare",
        ],
    },
    "gemini": {
        "confirm": [
            r"google\s+gemini",
            r"gemini\s+(?:ai|pro|ultra|nano|api|\d|advanced)",
            r"deepmind",
        ],
        "reject": [],
    },
    "falcon": {
        "confirm": [
            r"falcon\s+(?:\d+b|llm|model|ai|instruct)",
            r"tii\s+falcon",
        ],
        "reject": [
            r"millennium\s+falcon",
            r"falcon\s+(?:bird|raptor|sport|car)",
        ],
    },
    "palm": {
        "confirm": [
            r"google\s+palm",
            r"palm\s*2",
            r"palm\s+(?:api|model|chat)",
        ],
        "reject": [
            r"palm\s+(?:tree|plant|beach|reading|sunday)",
            r"(?:sweaty|clammy)\s+palm",
        ],
    },
}

# 2. SCORING SIGNALS

SECTION_SCORES: Dict[str, int] = {
    # High-signal dedicated disclosure sections
    "ai_disclosure": 5,
    "ai_use": 5,
    "ai_usage": 5,
    "declaration_of_generative_ai": 5,
    "acknowledgments": 2,
    "acknowledgements": 2,
    "acknowledgement": 2,
    "acknowledgment": 2,
    "ethics": 1,
    "ethics_statement": 1,
    "ethical_statement": 1,
    "ethical_considerations": 1,
    "reproducibility": 2,
    "data_availability": 2,
    "supplementary": 1,
    "appendix": 1,
    "header": -3,
    "conclusion": 0,
    "conclusions": 0,
    "discussion": 0,
    # Negative-score sections (risk of research/comparison mentions)
    "introduction": -1,
    "related_work": -2,
    "background": -2,
    "literature_review": -2,
    "methodology": -2,
    "method": -2,
    "methods": -2,
    "approach": -2,
    "experiments": -2,
    "experimental_setup": -2,
    "experimental_results": -2,
    "results": -2,
    "evaluation": -2,
    "analysis": -2,
    "abstract": -1,
    # Very negative
    "references": -6,
}

DISCLOSURE_THRESHOLD: int = 2    # score >= 2  → confirmed disclosure
REVIEW_THRESHOLD: int = 0        # 0 <= score < 2 → needs review; below 0 → skip

# (compiled_pattern, weight)  — pro-disclosure signals
_DISCLOSURE_SIGNAL_DEFS: List[Tuple[str, int]] = [
    # Explicit negative disclosure (highest confidence)
    (r"\bno\s+(?:generative\s+)?ai(?:\s+tools?)?\s+(?:was|were)\s+used\b|"
     r"\bno\s+(?:ai|llm|chatgpt|generative\s+ai|language\s+model|artificial\s+intelligence)\b.{0,40}\b(?:was|were)\s+used\b|"
     r"\bdid\s+not\s+(?:use|utilize|employ)\b.{0,50}\b(?:ai|llm|chatgpt|generative\s+ai)\b|"
     r"\bwithout\s+(?:the\s+use\s+of\s+)?(?:ai|llm|chatgpt|generative\s+ai)\b|"
     r"\bnot\s+(?:generated|produced|created|written)\s+(?:by|with|using)\s+(?:ai|llm|chatgpt)\b", 5),
    # First-person action verbs
    (r"\b(?:we|i|our|the\s+authors?)\s+(?:used?|utilized?|employed?|relied\s+on|leveraged?|made\s+use\s+of|prompted?|queried)\b", 3),
    (r"\bwas\s+(?:used|utilized|employed)\s+(?:to|for)\b", 3),
    # Explicit declaration language
    (r"\b(?:we|i|the\s+authors?)\s+(?:confirm|declare|disclose|attest|certify|state|acknowledge)\b", 3),
    (r"\b(?:disclosure|declare|disclose|acknowledge\s+the\s+use)\b", 3),
    (r"\bai\s+(?:usage|use)\s+(?:disclosure|statement)\b", 4),
    # Writing/editing task language
    (r"\bto\s+(?:proofread|edit|check|polish|correct|improve|review)\b", 2),
    (r"\bfor\s+(?:proofreading|editing|grammar|spell-?checking|language\s+editing)\b", 2),
    (r"\b(?:grammar|spelling|proofreading|language\s+editing)\b", 1),
    # Code and figure generation for paper
    (r"\bcode\s+generation\s+was\s+used\b|\bused\s+for\s+(?:hints\s+in\s+)?visuali[zs]ations?\b", 3),
    # General assistance
    (r"\bto\s+(?:assist|help|support|aid)\s+(?:with|in)\b", 1),
    (r"\bwith\s+the\s+(?:assistance|help|support|aid)\s+of\b", 2),
    # Research-method action language (strong explicit tool application)
    (r"\b(?:we|authors?)\b.{0,15}\b(?:used?|utilize|utilized?|employ|employed?|leveraged?|prompted?)\b.{0,40}\b(?:claude|chatgpt|gemini|gpt-4|gpt-3|whisper|stable\s+diffusion|midjourney|dall-?e|bloom|qwen|commercial\s+llm)\b", 4),
    (r"\buse\s+of\s+(?:the\s+)?(?:claude|chatgpt|gemini|gpt-4|gpt-3|llm|whisper)\b.{0,40}\bto\s+(?:generate|summarize|label|annotate|transcribe)\b", 4),
    (r"\b(?:summariz|annotat|label|generat|creat|transcrib|refin)(?:ed?|ing)\b.{0,60}\b(?:using|with|via|by)\s+(?:an?\s+|the\s+)?(?:chatgpt|claude|gemini|gpt|llm|whisper|stable\s+diffusion|large\s+language\s+model|commercial\s+llm)\b", 4),
    (r"\b(?:prompt|lyrics|captions?|images?|text|dialogue|dataset)\s+generated\s+(?:by|using|with|via)\s+(?:chatgpt|claude|gemini|gpt|llm|whisper|stable\s+diffusion)\b", 4),
    (r"\b(?:prompted?|queried?)\b.{0,40}\bto\s+(?:label|annotate|evaluate|create|generate|classify|summarize|predict)\b", 4),
    (r"\b(?:gpt-4o?|chatgpt|claude|gemini|llm|bloom)\s+was\s+(?:prompted|queried|employed|used)\b", 4),
    (r"\b(?:supported|assisted)\s+(?:using|with|by)\s+(?:chatgpt|claude|gemini|gpt|llm)\b", 4),
    (r"\bllm-(?:based|enabled|generated)\s+(?:augmentation|pseudo|captions?|dialogue|dataset)\b", 4),
    (r"\b(?:we\s+collect|collect(?:ed)?|using|used)\b.{0,30}whisper\b.{0,40}\b(?:transcription|transcribing)\b", 4),
    (r"\bzero-?shot|few-?shot|in-?context\s+learning\b", 1),
]

DISCLOSURE_SIGNALS = [
    (re.compile(pat, re.IGNORECASE), weight)
    for pat, weight in _DISCLOSURE_SIGNAL_DEFS
]

# (compiled_pattern, weight)  — anti-disclosure (research topic / false-positive) signals
_TOPIC_SIGNAL_DEFS: List[Tuple[str, int]] = [
    # Grants, funding, projects, fellowships in acknowledgments
    (r"\b(?:supported\s+by|funded\s+by|funding\s+from|grant|fellowship|scholarship|"
     r"budget\s+project|research\s+cent(?:er|re)|cent(?:er|re)\s+from|chair\s+in\s+digital|patron)\b", -5),
    # Leaked citations / bibliographies
    (r"\b(?:in\s+proceedings|international\s+conference|conference\s+on|"
     r"icassp|iclr|neurips|ismir|cvpr|ieee|acm|arxiv:\d|\bpp\.\s*\d+)\b", -5),
    # Macro ethics / societal impact / copyright debates (not author tool usage)
    (r"\b(?:societal\s+implications?|displacing\s+workers|intellectual\s+property\s+rights|"
     r"copyright\s+implications?|legal\s+uncertainty|consent\s+from\s+(?:all\s+)?creators|"
     r"copyright\s+infringement|rights\s+of\s+(?:composers|creators)|employed\s+by\s+(?:participants|teams|users))\b", -4),
    # General language modeling training objectives in MIR
    (r"\b(?:masked\s+language\s+model(?:ing)?|language\s+model\s+pretraining|"
     r"ngram\s+language\s+model|n-gram\s+language\s+model|method\s+of\s+language\s+modeling)\b", -4),
    # Comparative evaluation / benchmark performance
    (r"\b(?:outperform|baseline|benchmark|state-of-the-art|sota|compare|"
     r"accuracy|f1-?score|precision|recall|significantly\s+different)\b", -3),
    (r"\bfigure\s+\d+\b|\btable\s+\d+\b", -2),
    (r"\[\d+[–\-\d,\s]*\]", -2),                    # inline citations [1], [1,2], [40–42]
    (r"\([A-Z][a-z]+[\s,]+\d{4}\)", -1),          # author citations (Smith, 2023)
    (r"\bet\s+al\.", -1),
    (r"\b(?:propose|present|introduce|develop|train(?:ed)?|fine-?tun(?:ed)?)\b", -1),
    (r"\b(?:dataset|corpus|benchmark)\s+(?:use|using|used|based\s+on)\b", -2),
    (r"\b(?:model|system|framework|architecture|approach)\s+(?:use|uses|using|used)\b", -2),
    (r"\bprevious\s+(?:work|study|studies|research|approach)\b", -2),
    (r"\b(?:recent|existing|prior)\s+(?:work|method|approach|model)\b", -2),
]

TOPIC_SIGNALS = [
    (re.compile(pat, re.IGNORECASE), weight)
    for pat, weight in _TOPIC_SIGNAL_DEFS
]

# DISCLOSURE TYPE TAXONOMY
DISCLOSURE_TYPES: Dict[str, Dict] = {
    "negative": {
        "description": "Explicit statement that AI was NOT used",
        "patterns": [
            r"\bno\s+(?:ai|llm|chatgpt|generative\s+ai|language\s+model|artificial\s+intelligence)\b",
            r"\b(?:ai|llm|chatgpt|generative\s+ai)\b.{0,50}\b(?:not\s+used|was\s+not|were\s+not)\b",
            r"\bdid\s+not\s+(?:use|utilize|employ)\b.{0,50}\b(?:ai|llm|chatgpt|generative\s+ai)\b",
            r"\bwithout\s+(?:the\s+use\s+of\s+)?(?:ai|llm|generative\s+ai)\b",
            r"\bnot\s+(?:generated|produced|created|written)\s+(?:by|with|using)\s+(?:ai|llm|chatgpt)\b",
        ],
    },
    "writing_editing": {
        "description": "AI used for writing assistance: grammar, spelling, proofreading, language editing",
        "patterns": [
            r"\b(?:grammar|spell-?check|proofreading?|language\s+editing|copyediting|writing\s+assistance)\b",
            r"\bto\s+(?:proofread|edit|polish|correct|improve|revise|rewrite)\b.{0,60}\b(?:text|manuscript|paper|draft|writing)\b",
            r"\bfor\s+(?:proofreading|grammar|spell-?checking|language\s+editing|text\s+editing)\b",
            r"\bwriting\s+(?:assistance|support|aid|tool)\b",
            r"\b(?:edited?|polished?|corrected?|revised?)\b.{0,30}\b(?:by|using|with)\b.{0,30}\b(?:ai|llm|chatgpt|grammarly|deepl)\b",
        ],
    },
    "code_generation": {
        "description": "AI used for coding, debugging, or software implementation",
        "patterns": [
            r"\b(?:code|coding|programming|script|implementation|software|debugging|bug)\b.{0,60}\b(?:ai|llm|chatgpt|copilot|generated|assisted)\b",
            r"\b(?:ai|llm|chatgpt|copilot)\b.{0,60}\b(?:code|coding|programming|script|implementation|debugging)\b",
            r"\bgithub\s+copilot\b",
            r"\bcode\s+(?:generation|completion|suggestion)\b",
            r"\bwriting\s+(?:code|scripts|software)\b.{0,40}\b(?:ai|llm|copilot|chatgpt)\b",
        ],
    },
    "literature_search": {
        "description": "AI used for literature search, summarization, or reference finding",
        "patterns": [
            r"\b(?:literature|references?|papers?|articles?|bibliography)\b.{0,60}\b(?:search|find|summar|review)\b.{0,30}\b(?:ai|llm|chatgpt)\b",
            r"\b(?:ai|llm|chatgpt)\b.{0,60}\b(?:literature|references?|papers?|summariz)\b",
            r"\b(?:semantic\s+scholar|perplexity|elicit|consensus)\b",
        ],
    },
    "data_annotation": {
        "description": "AI used for data labeling, annotation, or dataset creation",
        "patterns": [
            r"\b(?:annotate|annotation|label(?:led?|ing)?|tag(?:ged|ging)?)\b.{0,60}\b(?:ai|llm|chatgpt|gpt|model)\b",
            r"\b(?:ai|llm|chatgpt|gpt)\b.{0,60}\b(?:annotate|annotation|label(?:led?|ing)?|tag(?:ged|ging)?)\b",
            r"\b(?:synthetic\s+(?:data|labels?|annotations?)|data\s+augmentation)\b.{0,40}\b(?:ai|llm|generated|model)\b",
            r"\b(?:ai|llm|model)\b.{0,40}\b(?:generate|generated|creating|create)\b.{0,40}\b(?:annotations?|labels?|data)\b",
        ],
    },
    "ideation": {
        "description": "AI used for brainstorming, drafting, or idea generation",
        "patterns": [
            r"\b(?:brainstorm|ideation|draft(?:ing)?|outline|idea\s+generation)\b.{0,60}\b(?:ai|llm|chatgpt)\b",
            r"\b(?:ai|llm|chatgpt)\b.{0,60}\b(?:brainstorm|ideation|draft(?:ing)?|outline|idea\s+generation)\b",
        ],
    },
    "figure_generation": {
        "description": "AI used for image or figure generation",
        "patterns": [
            r"\b(?:dall-?e|midjourney|stable\s+diffusion|image\s+generation|generated\s+image|ai-?generated\s+image)\b",
            r"\b(?:figure|image|illustration|graphic)\b.{0,60}\b(?:generated|created|produced)\b.{0,30}\b(?:by|using|with)\b.{0,20}\b(?:ai|dall-?e|midjourney|stable\s+diffusion)\b",
        ],
    },
    "research_method": {
        "description": "AI used as core research tool (e.g., prompted GPT-4 to annotate, used LLM to generate stimuli)",
        "patterns": [
            r"\b(?:prompted?|prompt(?:ing|ed)?)\b.{0,40}\b(?:model|llm|chatgpt|gpt|claude|gemini)\b",
            r"\b(?:queried?|query(?:ing)?)\b.{0,40}\b(?:model|llm|api|chatgpt|gpt)\b",
            r"\bzero-?shot|few-?shot|in-?context\s+learning\b",
            r"\b(?:model|llm|chatgpt|gpt)\b.{0,60}\b(?:generat|produc|output|respon)\b.{0,40}\b(?:stimuli|lyrics|text|descriptions?|captions?)\b",
            r"\bapi\s+(?:call|access|request|endpoint)\b.{0,40}\b(?:openai|anthropic|google|chatgpt|gpt)\b",
            r"\b(?:openai|anthropic|google)\s+api\b",
            r"\b(?:inference|forward\s+pass|model\s+output)\b.{0,40}\b(?:llm|gpt|claude|gemini|mistral)\b",
        ],
    },
    "general_unspecified": {
        "description": "Confirmed AI disclosure but no specific task identified",
        "patterns": [
            r"\bai\s+(?:usage|use)\s+(?:disclosure|statement)\b",
            r"\b(?:acknowledge|disclose|declare)\b.{0,40}\b(?:use\s+of|usage\s+of|using)\b.{0,40}\b(?:ai|llm|chatgpt|generative\s+ai|language\s+model)\b",
        ],
    },
}

# Pre-compile all type patterns
_COMPILED_TYPE_PATTERNS: Dict[str, List[re.Pattern]] = {
    dtype: [re.compile(p, re.IGNORECASE) for p in info["patterns"]]
    for dtype, info in DISCLOSURE_TYPES.items()
}

# DATACLASSES

@dataclass
class SentenceRecord:
    year: int
    paper_id: str
    section: str
    sentence: str
    tools_found: List[str]
    score: int
    is_disclosure: bool
    needs_review: bool
    disclosure_types: List[str]
    is_ambiguous: bool
    paper_url: str = ""
    task_role: str = ""
    statement_type: str = ""


@dataclass
class PaperDisclosureRecord:
    year: int
    paper_id: str
    title: str
    source_url: str
    has_disclosure: bool
    is_negative_disclosure: bool
    disclosure_types: List[str]
    tools_named: List[str]
    task_roles: List[str] = field(default_factory=list)
    statement_types: List[str] = field(default_factory=list)
    sections_placed: List[str] = field(default_factory=list)
    evidence_sentences: List[str] = field(default_factory=list)
    needs_review: bool = False
    review_sentences: List[str] = field(default_factory=list)

# HELPERS

# Abbreviations that contain periods but are NOT sentence boundaries
_ABBREV_RE = re.compile(
    r"(?:"
    r"\b(?:et\s+al|e\.g|i\.e|fig|figs|eq|eqs|sec|tab|vol|no|pp|vs|cf|al|dr|prof|mr|mrs|ms)\."
    r"|\b\d+\.\d+"    # decimal numbers
    r")",
    re.IGNORECASE,
)

def split_sentences(text: str) -> List[str]:
    """Split text into sentences, preserving abbreviations and decimals."""
    # Replace protected periods temporarily
    protected = _ABBREV_RE.sub(lambda m: m.group(0).replace(".", "⚬"), text)
    # Split on sentence boundaries
    raw = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])", protected)
    # Restore protected periods
    sentences = [s.replace("⚬", ".").strip() for s in raw if s.strip()]
    return sentences


def _check_ambiguous_tool(tool_key: str, sentence: str, window: str) -> str:
    """
    Returns 'valid', 'invalid', or 'ambiguous' for an ambiguous tool mention.
    `window` is the broader context (e.g., surrounding sentences or section snippet).
    """
    info = AMBIGUOUS_TOOLS[tool_key]
    # Check reject patterns first (in sentence + window)
    full_ctx = (sentence + " " + window).lower()
    for pat in info["reject"]:
        if re.search(pat, full_ctx, re.IGNORECASE):
            return "invalid"
    # Check confirm patterns
    for pat in info["confirm"]:
        if re.search(pat, full_ctx, re.IGNORECASE):
            return "valid"
    return "ambiguous"


def validate_tool_mention(tool_key: str, sentence: str, context: str = "") -> str:
    """Return 'valid', 'invalid', or 'ambiguous'."""
    if tool_key in AMBIGUOUS_TOOLS:
        return _check_ambiguous_tool(tool_key, sentence, context)
    return "valid"


def clean_sentence_text(text: str) -> str:
    """Clean multi-line artifacts, HTML tags/comments, headers, and conference proceedings footers."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(
        r"\s*\d+\s+Proceedings of the \d+(?:st|nd|rd|th) ISMIR Conference[^\n\.]*",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"^#+\s*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def find_tool_mentions(
    text: str, context: str = ""
) -> Tuple[List[str], bool]:
    """
    Scan `text` for AI tool/concept mentions using strict word boundaries.
    Returns (confirmed_tools, has_ambiguous).
    confirmed_tools is a deduplicated list of canonical tool names.
    """
    text_lower = text.lower()
    confirmed: List[str] = []
    has_ambiguous = False

    # Check concepts first with word boundaries
    for pat, canonical in AI_CONCEPTS_PATTERNS:
        if pat.search(text_lower):
            if canonical not in confirmed:
                confirmed.append(canonical)

    # Check tool names with word boundaries (longest-first to handle overlapping keys)
    seen_spans: List[Tuple[int, int]] = []
    for key in AI_TOOLS_SORTED:
        tool_pat = r"\b" + re.escape(key) + r"\b"
        for m in re.finditer(tool_pat, text_lower):
            start, end = m.start(), m.end()
            # Skip if already covered by a longer match
            if any(s <= start < e or s < end <= e for s, e in seen_spans):
                continue
            # Validate ambiguous tools
            status = validate_tool_mention(key, text, context)
            if status == "invalid":
                seen_spans.append((start, end))
                continue
            if status == "ambiguous":
                has_ambiguous = True
                seen_spans.append((start, end))
                continue
            # Valid
            canonical = AI_TOOLS[key]
            if canonical not in confirmed:
                confirmed.append(canonical)
            seen_spans.append((start, end))

    return confirmed, has_ambiguous


def score_sentence(sentence: str, section_name: str) -> int:
    """
    Compute disclosure relevance score for a sentence in a given section.
    Positive → more likely a disclosure; negative → not a disclosure.
    """
    score = 0

    # Section base score
    section_key = section_name.lower().strip()
    score += SECTION_SCORES.get(section_key, 0)

    # Disclosure signals
    for pattern, weight in DISCLOSURE_SIGNALS:
        if pattern.search(sentence):
            score += weight

    # Topic/research signals (negative)
    for pattern, weight in TOPIC_SIGNALS:
        if pattern.search(sentence):
            score += weight

    return score


def classify_disclosure_types(
    sentence: str, confirmed_tools: List[str]
) -> List[str]:
    """
    Return a list of disclosure type keys that apply to this sentence.
    Falls back to 'general_unspecified' if no specific type matches.
    """
    matched: List[str] = []
    for dtype, patterns in _COMPILED_TYPE_PATTERNS.items():
        if dtype == "general_unspecified":
            continue
        for pat in patterns:
            if pat.search(sentence):
                matched.append(dtype)
                break

    # Also check for tool-specific types
    tool_names_lower = " ".join(t.lower() for t in confirmed_tools)
    if any(t in tool_names_lower for t in ["dall-e", "midjourney", "stable diffusion"]):
        if "figure_generation" not in matched:
            matched.append("figure_generation")
    if "grammarly" in tool_names_lower or "deepl" in tool_names_lower:
        if "writing_editing" not in matched:
            matched.append("writing_editing")
    if "copilot" in tool_names_lower:
        if "code_generation" not in matched:
            matched.append("code_generation")

    if not matched:
        matched.append("general_unspecified")

    return matched


def assign_task_role(sentence: str, tools_found: List[str]) -> str:
    """Assign a human-readable, specific Task/Role to the AI tool disclosure."""
    sl = sentence.lower()
    tl = " ".join(t.lower() for t in tools_found)

    if "no generative ai" in sl or "no ai" in sl or "without the use of ai" in sl or "without using ai" in sl:
        return "Negative prose disclosure / Code hints for figures"
    if "deepl" in tl or "translate" in sl:
        return "Non-English prompt translation"
    if "summarize" in sl or "summarized" in sl:
        if "billboard" in sl or "verse" in sl:
            return "Lyrics summarization / Prompt creation"
        return "Audio caption summarization"
    if "synthetic lyrics" in sl or "lyrics in the style" in sl:
        if "dataset" in sl:
            return "Synthetic lyrics dataset creation"
        return "Synthetic lyrics generation"
    if "back-end" in sl or "initial prompts" in sl:
        return "Backend prompt construction"
    if "text prompt generated by chatgpt" in sl or "text prompt generated" in sl:
        return "Text prompt generation for evaluation"
    if "whisper" in tl or "transcription" in sl or "transcribe" in sl or "speech to text" in sl:
        return "Automatic lyrics transcription"
    if "gemini" in tl and ("label" in sl or "dimension" in sl):
        return "Automated evaluation labeling"
    if "claude" in tl and ("evaluate" in sl or "questions and answers" in sl or "quality" in sl or "sense based" in sl):
        return "Question-answer quality assessment"
    if "claude" in tl and "caption" in sl:
        return "In-context caption generation"
    if "bloom" in tl or "tag-to-caption" in sl:
        return "Tag-to-caption dataset augmentation"
    if "dialogue" in sl or "utterances" in sl:
        return "Utterance & dialogue generation"
    if "prompt engineering" in sl and ("mir" in sl or "error detection" in sl):
        return "Prompt engineering for MIR reasoning"
    if "supported using chatgpt" in sl or "distinct musical characteristics" in sl or "genre selection" in sl:
        return "Genre selection assistance"
    if "stable diffusion" in tl or "rich-text-to-image" in sl or "coloring" in sl or "figure" in sl:
        return "Image synthesis / Figure creation"
    if "emotion annotation" in sl or "samples across three independent runs" in sl or "gpt-4o was prompted" in sl:
        return "Music emotion annotation"
    if "metascore" in sl or "metadata into natural language captions" in sl:
        return "Metadata-to-caption generation"
    if "prompt the llm to generate multiple candidates" in sl or "generate multiple candidates" in sl:
        return "Question candidate generation"
    if "qwen" in tl or "probability of a lightweight" in sl or "log probability" in sl:
        return "Answer probability evaluation"
    if "piast" in sl or "youtube" in sl:
        return "YouTube metadata refinement"
    if "lp-musiccaps" in sl or "pseudo-music caption" in sl or "pseudo caption" in sl:
        return "Dataset pseudo-caption creation"
    if "grammar" in sl or "proofread" in sl or "editing" in sl:
        return "Grammar & language editing"
    if "code" in sl or "implementation" in sl or "coding" in sl:
        return "Code implementation / debugging"

    return "Research method / Tool application"


def assign_statement_type(task_role: str) -> str:
    """Map a granular task_role to one of 4 high-level statement type buckets.

    Buckets:
      Type 1 — Dataset Creation & Corpus Augmentation
      Type 2 — Core System & Method Pipeline
      Type 3 — Evaluation & Annotation Support
      Type 4 — Manuscript & Presentation Assistance
    """
    TYPE1 = {
        "Synthetic lyrics generation",
        "Synthetic lyrics dataset creation",
        "Dataset pseudo-caption creation",
        "Tag-to-caption dataset augmentation",
        "Utterance & dialogue generation",
        "Metadata-to-caption generation",
        "YouTube metadata refinement",
        "Audio caption summarization",
        "In-context caption generation",
    }
    TYPE2 = {
        "Automatic lyrics transcription",
        "Backend prompt construction",
        "Non-English prompt translation",
        "Prompt engineering for MIR reasoning",
        "Question candidate generation",
        "Answer probability evaluation",
        "Research method / Tool application",  # fallback → closest fit
    }
    TYPE3 = {
        "Lyrics summarization / Prompt creation",
        "Text prompt generation for evaluation",
        "Automated evaluation labeling",
        "Question-answer quality assessment",
        "Music emotion annotation",
        "Genre selection assistance",
    }
    TYPE4 = {
        "Grammar & language editing",
        "Image synthesis / Figure creation",
        "Negative prose disclosure / Code hints for figures",
        "Code implementation / debugging",
    }

    if task_role in TYPE1:
        return "Type 1 — Dataset Creation & Corpus Augmentation"
    if task_role in TYPE2:
        return "Type 2 — Core System & Method Pipeline"
    if task_role in TYPE3:
        return "Type 3 — Evaluation & Annotation Support"
    if task_role in TYPE4:
        return "Type 4 — Manuscript & Presentation Assistance"
    return "Ambiguous"


# CORE ANALYSIS

def _has_ai_signal(text: str) -> bool:
    """Quick pre-filter: does this text mention any AI tool or concept with word boundaries?"""
    text_lower = text.lower()
    for pat, _ in AI_CONCEPTS_PATTERNS:
        if pat.search(text_lower):
            return True
    for key in AI_TOOLS_SORTED:
        if re.search(r"\b" + re.escape(key) + r"\b", text_lower):
            return True
    return False


def analyze_paper(
    year: int,
    paper_id: str,
    paper_data: dict,
    disclosure_threshold: int = DISCLOSURE_THRESHOLD,
    review_threshold: int = REVIEW_THRESHOLD,
) -> Tuple[List[SentenceRecord], PaperDisclosureRecord]:
    """
    Scan all sections of a paper and extract AI disclosure sentences.
    Returns (sentence_records, paper_record).
    """
    sections: dict = paper_data.get("sections", {})
    title: str = paper_data.get("title", "")
    source_url: str = paper_data.get("metadata", {}).get("source_url", "")

    all_sentence_records: List[SentenceRecord] = []
    confirmed_sentence_records: List[SentenceRecord] = []
    review_sentence_records: List[SentenceRecord] = []

    all_tools_named: List[str] = []
    all_disclosure_types: List[str] = []
    all_sections_placed: List[str] = []

    for section_name, section_text in sections.items():
        if not section_text or not isinstance(section_text, str):
            continue
        # Quick pre-filter at section level
        if not _has_ai_signal(section_text):
            continue

        sentences = split_sentences(section_text)
        for sentence in sentences:
            if len(sentence) < 20:  # skip very short fragments
                continue
            if not _has_ai_signal(sentence):
                continue

            # Find tool mentions in this sentence + broader section context
            tools_found, is_ambiguous = find_tool_mentions(sentence, context=section_text[:500])
            has_concept = any(pat.search(sentence) for pat, _ in AI_CONCEPTS_PATTERNS)
            if not tools_found and not has_concept:
                # Ambiguous tool mention but no confirmed signal — still score it
                if not is_ambiguous:
                    continue

            score = score_sentence(sentence, section_name)
            is_disclosure = score >= disclosure_threshold
            needs_review = (review_threshold <= score < disclosure_threshold)

            if score < review_threshold and not is_disclosure:
                continue

            dtypes = classify_disclosure_types(sentence, tools_found) if is_disclosure else []
            clean_text = clean_sentence_text(sentence)
            # Skip corrupted OCR table fragments, markdown tables, or attribution header lines
            if re.search(r"\d+%\s+\d+%", clean_text) or clean_text.startswith("|") or "|---" in clean_text or "attribution:" in clean_text.lower():
                continue

            rec = SentenceRecord(
                year=year,
                paper_id=paper_id,
                section=section_name,
                sentence=clean_text,
                tools_found=tools_found,
                score=score,
                is_disclosure=is_disclosure,
                needs_review=needs_review,
                disclosure_types=dtypes,
                is_ambiguous=is_ambiguous,
                paper_url=source_url,
                task_role=assign_task_role(clean_text, tools_found) if is_disclosure else "",
                statement_type=assign_statement_type(assign_task_role(clean_text, tools_found)) if is_disclosure else "",
            )
            all_sentence_records.append(rec)
            if is_disclosure:
                # Deduplicate identical or OCR-duplicate sentences within the same paper
                if any(clean_text in r.sentence or r.sentence in clean_text or clean_text[:40] == r.sentence[:40] or ("claude" in clean_text.lower() and "claude" in r.sentence.lower()) for r in confirmed_sentence_records):
                    continue
                confirmed_sentence_records.append(rec)
                for t in tools_found:
                    if t not in all_tools_named:
                        all_tools_named.append(t)
                for dt in dtypes:
                    if dt not in all_disclosure_types:
                        all_disclosure_types.append(dt)
                if section_name not in all_sections_placed:
                    all_sections_placed.append(section_name)
            if needs_review:
                review_sentence_records.append(rec)

    has_disclosure = len(confirmed_sentence_records) > 0
    is_negative = any(
        "negative" in rec.disclosure_types
        for rec in confirmed_sentence_records
    )
    # If ONLY negative type, it's a negative-only disclosure
    all_dtypes_flat = []
    for rec in confirmed_sentence_records:
        all_dtypes_flat.extend(rec.disclosure_types)

    paper_record = PaperDisclosureRecord(
        year=year,
        paper_id=paper_id,
        title=title,
        source_url=source_url,
        has_disclosure=has_disclosure,
        is_negative_disclosure=is_negative,
        disclosure_types=sorted(set(all_disclosure_types)),
        tools_named=all_tools_named,
        task_roles=sorted(set(rec.task_role for rec in confirmed_sentence_records if rec.task_role)),
        statement_types=sorted(set(rec.statement_type for rec in confirmed_sentence_records if rec.statement_type)),
        sections_placed=all_sections_placed,
        evidence_sentences=[rec.sentence for rec in confirmed_sentence_records],
        needs_review=len(review_sentence_records) > 0 or any(
            rec.is_ambiguous for rec in confirmed_sentence_records
        ),
        review_sentences=[rec.sentence for rec in review_sentence_records],
    )

    return all_sentence_records, paper_record


def analyze_dataset(
    dataset: Dict[int, Dict[str, dict]],
    disclosure_threshold: int = DISCLOSURE_THRESHOLD,
    review_threshold: int = REVIEW_THRESHOLD,
) -> Tuple[List[SentenceRecord], List[PaperDisclosureRecord]]:
    """
    Analyze all papers in the dataset.
    Returns (all_sentence_records, all_paper_records).
    """
    all_sentences: List[SentenceRecord] = []
    all_papers: List[PaperDisclosureRecord] = []

    years_sorted = sorted(dataset.keys())
    for year in years_sorted:
        papers = dataset[year]
        print(f"  Analysing {year}: {len(papers)} papers …", flush=True)
        for paper_id, paper_data in sorted(papers.items()):
            sent_recs, paper_rec = analyze_paper(
                year, paper_id, paper_data,
                disclosure_threshold=disclosure_threshold,
                review_threshold=review_threshold,
            )
            all_sentences.extend(sent_recs)
            all_papers.append(paper_rec)

    return all_sentences, all_papers

# EXPORT FUNCTIONS

def _join(lst: List[str]) -> str:
    return "; ".join(lst) if lst else ""


def export_papers_csv(records: List[PaperDisclosureRecord], path: str) -> None:
    """Write one row per paper."""
    fieldnames = [
        "year", "paper_id", "title", "source_url",
        "has_disclosure", "is_negative_disclosure",
        "disclosure_types", "tools_named", "task_roles", "statement_types", "sections_placed",
        "evidence_sentence_1", "evidence_sentence_2",
        "num_evidence_sentences", "needs_review",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in records:
            evs = r.evidence_sentences
            w.writerow({
                "year": r.year,
                "paper_id": r.paper_id,
                "title": r.title,
                "source_url": r.source_url,
                "has_disclosure": r.has_disclosure,
                "is_negative_disclosure": r.is_negative_disclosure,
                "disclosure_types": _join(r.disclosure_types),
                "tools_named": _join(r.tools_named),
                "task_roles": _join(r.task_roles),
                "statement_types": _join(r.statement_types),
                "sections_placed": _join(r.sections_placed),
                "evidence_sentence_1": evs[0] if len(evs) > 0 else "",
                "evidence_sentence_2": evs[1] if len(evs) > 1 else "",
                "num_evidence_sentences": len(evs),
                "needs_review": r.needs_review,
            })
    print(f"  → {path}")


def export_sentences_csv(records: List[SentenceRecord], path: str) -> None:
    """Write one row per confirmed disclosure sentence with columns: year, paper, tool, task_role, statement_type, paper_url, statement."""
    confirmed = [r for r in records if r.is_disclosure]
    fieldnames = ["year", "paper", "tool", "task_role", "statement_type", "paper_url", "statement"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in confirmed:
            tools_str = "; ".join(r.tools_found) if r.tools_found else "; ".join(r.disclosure_types)
            w.writerow({
                "year": r.year,
                "paper": r.paper_id,
                "tool": tools_str,
                "task_role": r.task_role,
                "statement_type": r.statement_type,
                "paper_url": r.paper_url,
                "statement": r.sentence,
            })
    print(f"  → {path}  ({len(confirmed)} sentences)")


def export_needs_review_csv(records: List[SentenceRecord], path: str) -> None:
    """Write borderline / ambiguous sentences for manual review with columns: year, paper, tool, task_role, paper_url, statement."""
    review = [r for r in records if r.needs_review and not r.is_disclosure]
    fieldnames = ["year", "paper", "tool", "task_role", "paper_url", "statement"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in review:
            tools_str = "; ".join(r.tools_found) if r.tools_found else "; ".join(r.disclosure_types)
            w.writerow({
                "year": r.year,
                "paper": r.paper_id,
                "tool": tools_str,
                "task_role": r.task_role,
                "paper_url": r.paper_url,
                "statement": r.sentence,
            })
    print(f"  → {path}  ({len(review)} sentences)")


def export_yearly_csv(paper_records: List[PaperDisclosureRecord], path: str) -> None:
    """Write year-by-year summary."""
    dtype_keys = list(DISCLOSURE_TYPES.keys())
    fieldnames = [
        "year", "total_papers",
        "papers_with_disclosure", "disclosure_rate_pct",
        "papers_negative", "negative_rate_pct",
    ] + [f"papers_{dt}" for dt in dtype_keys] + [
        "most_common_tool", "most_common_section",
        "papers_needing_review",
    ]

    # Group by year
    by_year: Dict[int, List[PaperDisclosureRecord]] = defaultdict(list)
    for r in paper_records:
        by_year[r.year].append(r)

    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for year in sorted(by_year.keys()):
            recs = by_year[year]
            total = len(recs)
            with_disc = sum(1 for r in recs if r.has_disclosure)
            negative = sum(1 for r in recs if r.is_negative_disclosure)

            tool_counter: Counter = Counter()
            section_counter: Counter = Counter()
            type_counts: Dict[str, int] = {dt: 0 for dt in dtype_keys}
            review_count = 0

            for r in recs:
                for t in r.tools_named:
                    tool_counter[t] += 1
                for s in r.sections_placed:
                    section_counter[s] += 1
                for dt in r.disclosure_types:
                    if dt in type_counts:
                        type_counts[dt] += 1
                if r.needs_review:
                    review_count += 1

            most_tool = tool_counter.most_common(1)[0][0] if tool_counter else ""
            most_section = section_counter.most_common(1)[0][0] if section_counter else ""

            row = {
                "year": year,
                "total_papers": total,
                "papers_with_disclosure": with_disc,
                "disclosure_rate_pct": round(100 * with_disc / total, 1) if total else 0,
                "papers_negative": negative,
                "negative_rate_pct": round(100 * negative / total, 1) if total else 0,
                "most_common_tool": most_tool,
                "most_common_section": most_section,
                "papers_needing_review": review_count,
            }
            for dt in dtype_keys:
                row[f"papers_{dt}"] = type_counts[dt]
            w.writerow(row)
    print(f"  → {path}")


def print_summary(paper_records: List[PaperDisclosureRecord]) -> None:
    """Print a human-readable year-by-year statistics summary."""
    by_year: Dict[int, List[PaperDisclosureRecord]] = defaultdict(list)
    for r in paper_records:
        by_year[r.year].append(r)

    total_papers = len(paper_records)
    total_disc = sum(1 for r in paper_records if r.has_disclosure)

    print("\n" + "=" * 60)
    print("  AI DISCLOSURE DETECTION — SUMMARY")
    print("=" * 60)

    for year in sorted(by_year.keys()):
        recs = by_year[year]
        n = len(recs)
        disc = sum(1 for r in recs if r.has_disclosure)
        neg = sum(1 for r in recs if r.is_negative_disclosure)
        review = sum(1 for r in recs if r.needs_review)

        type_counts: Counter = Counter()
        for r in recs:
            type_counts.update(r.disclosure_types)

        tool_counter: Counter = Counter()
        for r in recs:
            tool_counter.update(r.tools_named)

        pct = 100 * disc / n if n else 0
        print(f"\n  {year}  ({n} papers)")
        print(f"    Disclosures   : {disc:>4}  ({pct:.1f}%)")
        print(f"    Negative only : {neg:>4}")
        if type_counts:
            top = type_counts.most_common(3)
            print(f"    Top types     : " + ", ".join(f"{k}={v}" for k, v in top))
        if tool_counter:
            top_tools = tool_counter.most_common(3)
            print(f"    Top tools     : " + ", ".join(f"{k}={v}" for k, v in top_tools))
        print(f"    Needs review  : {review}")

    print(f"\n  TOTAL: {total_disc}/{total_papers} papers with disclosures "
          f"({100*total_disc/total_papers:.1f}%)")
    print("=" * 60 + "\n")

# 8. DATASET LOADING (via analyse_dataset.py)

def load_dataset(
    data_dir: Optional[str],
    years: Optional[List[int]],
    verbose: bool = True,
) -> Dict[int, Dict[str, dict]]:
    """Load ISMIR dataset using analyse_dataset.load_ismir_dataset."""
    # Ensure the script's own directory is on sys.path so analyse_dataset is importable
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)

    try:
        from analyse_dataset import load_ismir_dataset  # type: ignore
    except ImportError as exc:
        print(f"ERROR: Could not import analyse_dataset: {exc}", file=sys.stderr)
        print("Make sure analyse_dataset.py is in the same directory.", file=sys.stderr)
        sys.exit(1)

    kwargs: dict = {"verbose": verbose}
    if data_dir:
        kwargs["data_dir"] = data_dir
    if years:
        kwargs["years"] = years

    dataset = load_ismir_dataset(**kwargs)
    return dataset

# 9. CLI

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Detect and classify AI usage disclosures in ISMIR papers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument(
        "--data-dir",
        metavar="PATH",
        default=None,
        help="Path to data directory (default: auto-detect dataset/ or ISMIR_Papers/)",
    )
    p.add_argument(
        "--years",
        type=int,
        nargs="+",
        metavar="YEAR",
        default=None,
        help="Filter to specific years, e.g. --years 2023 2024 2025",
    )
    p.add_argument(
        "--output-dir",
        metavar="PATH",
        default=".",
        help="Directory to write CSV output files (default: current directory)",
    )
    p.add_argument(
        "--threshold",
        type=int,
        default=DISCLOSURE_THRESHOLD,
        metavar="N",
        help=f"Minimum score to classify as confirmed disclosure (default: {DISCLOSURE_THRESHOLD})",
    )
    p.add_argument(
        "--review-threshold",
        type=int,
        default=REVIEW_THRESHOLD,
        metavar="N",
        help=f"Minimum score for 'needs review' (default: {REVIEW_THRESHOLD})",
    )
    p.add_argument(
        "--no-summary",
        action="store_true",
        help="Suppress the console summary",
    )
    p.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress progress messages",
    )
    return p


def main(argv: Optional[List[str]] = None) -> None:
    args = build_parser().parse_args(argv)

    verbose = not args.quiet
    os.makedirs(args.output_dir, exist_ok=True)

    # Load dataset
    if verbose:
        print("Loading dataset …")
    dataset = load_dataset(
        data_dir=args.data_dir,
        years=args.years,
        verbose=verbose,
    )
    if not dataset:
        print("ERROR: No papers loaded.", file=sys.stderr)
        sys.exit(1)

    total = sum(len(v) for v in dataset.values())
    if verbose:
        print(f"Loaded {total} papers across {len(dataset)} year(s).")
        print("Detecting disclosures …")

    # Analyse
    sentence_records, paper_records = analyze_dataset(
        dataset,
        disclosure_threshold=args.threshold,
        review_threshold=args.review_threshold,
    )

    # Export
    if verbose:
        print("\nWriting output files …")

    export_papers_csv(
        paper_records,
        os.path.join(args.output_dir, "disclosure_per_paper.csv"),
    )
    export_sentences_csv(
        sentence_records,
        os.path.join(args.output_dir, "disclosure_sentences.csv"),
    )
    export_needs_review_csv(
        sentence_records,
        os.path.join(args.output_dir, "disclosure_needs_review.csv"),
    )
    export_yearly_csv(
        paper_records,
        os.path.join(args.output_dir, "disclosure_per_year.csv"),
    )

    # Summary
    if not args.no_summary:
        print_summary(paper_records)


if __name__ == "__main__":
    main()

