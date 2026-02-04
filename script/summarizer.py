from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_summarizer():
    return pipeline("text-generation", model="google/flan-t5-base")

summarizer = load_summarizer()

def summarize(text, mode="short"):
    if not text or len(text) < 50:
        return "No significant update available."

    if mode == "short":
        prompt = f"Summarize this news in 1–2 short sentences:\n{text}"
        max_tokens = 60
    else:
        prompt = f"Write a clear detailed summary in 5–7 sentences:\n{text}"
        max_tokens = 160

    result = summarizer(
        prompt,
        max_new_tokens=max_tokens,
        do_sample=False,
        repetition_penalty=2.0,
        truncation=True
    )

    return result[0]["generated_text"].strip()
