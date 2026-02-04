import streamlit as st
from transformers import pipeline

# ==================================================
# Load summarizer once
# ==================================================
@st.cache_resource
def load_summarizer():
    return pipeline(
        task="text-generation",
        model="google/flan-t5-base"
    )

_summarizer = load_summarizer()

# ==================================================
# Clean output (remove prompt leakage)
# ==================================================
def _clean(text: str) -> str:
    blacklist = [
        "read the full news",
        "write a detailed summary",
        "do not use bullet points",
        "make it informative",
        "summary:",
        "news:"
    ]

    lines = []
    for line in text.splitlines():
        if not any(bad in line.lower() for bad in blacklist):
            lines.append(line.strip())

    text = " ".join(lines)

    # Remove duplicate adjacent words
    words = text.split()
    cleaned = []
    for w in words:
        if not cleaned or w.lower() != cleaned[-1].lower():
            cleaned.append(w)

    return " ".join(cleaned).strip()

# ==================================================
# Public summarize function
# ==================================================
def summarize(text: str, mode: str = "short") -> str:
    if not text or len(text.strip()) < 50:
        return "No significant update available."

    if mode == "short":
        prompt = ("News:\n\n"
            
            f"{text}"
        )
        max_tokens = 80
    else:
        prompt = (
            "News:\n\n"
            f"{text}"
        )
        max_tokens = 200

    result = _summarizer(
        prompt,
        max_new_tokens=max_tokens,
        do_sample=False,
        repetition_penalty=2.0,
        truncation=True
    )

    return _clean(result[0]["generated_text"])
