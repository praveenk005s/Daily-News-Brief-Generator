import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    return pipeline(
        task="text-generation",
        model="google/flan-t5-base"
    )

_summarizer = load_summarizer()

def summarize(text: str, mode: str = "short") -> str:
    if not text or len(text.strip()) < 40:
        return "No significant update available."

    if mode == "short":
        prompt = (
            
            f"{text}"
        )
        max_tokens = 80
    else:
        prompt = (
            
            f"{text}"
        )
        max_tokens = 180

    result = _summarizer(
        prompt,
        max_new_tokens=max_tokens,
        do_sample=False,
        repetition_penalty=1.8,
        truncation=True
    )

    return result[0]["generated_text"].strip()

