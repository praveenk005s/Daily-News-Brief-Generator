import streamlit as st
from datetime import date

from script.news_fetcher import fetch_news
from script.summarizer import summarize
from script.deduplicator import remove_duplicates
from utils.constants import CATEGORIES

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Daily News Brief",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================
if "selected_article" not in st.session_state:
    st.session_state.selected_article = None

# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.title("🗞️ Preferences")

categories = st.sidebar.multiselect(
    "Select News Categories",
    CATEGORIES,
    default=["Technology"]
)

summary_type = st.sidebar.selectbox(
    "Reading Preference",
    ["short", "detailed"]
)

selected_date = st.sidebar.date_input(
    "Select Date",
    date.today()
)

if st.sidebar.button("🔄 Refresh Latest News"):
    st.rerun()

# ==================================================
# FULL ARTICLE PAGE
# ==================================================
if st.session_state.selected_article:
    art = st.session_state.selected_article

    st.title(art.get("title", "News Article"))

    st.caption(
        f"{art.get('source', 'Unknown')} | {art.get('publishedAt', '')}"
    )

    st.markdown("---")

    full_text = (
        art.get("content")
        or art.get("description")
        or "Full article text not available from API."
    )

    st.markdown(full_text)

    st.markdown("---")

    st.markdown(
        f"🔗 [Read original article]({art.get('url', '#')})",
        unsafe_allow_html=True
    )

    if st.button("⬅ Back to Daily Brief"):
        st.session_state.selected_article = None
        st.rerun()

    st.stop()

# ==================================================
# MAIN PAGE
# ==================================================
st.title("📌 Your Personalized Daily News Brief")
st.caption(f"Date: {selected_date.strftime('%d %b %Y')}")

if not categories:
    st.warning("Please select at least one category.")
    st.stop()

for category in categories:
    st.subheader(f"🔹 Your Daily {category} Brief")

    articles = remove_duplicates(fetch_news(category))

    if not articles:
        st.info("No news available for this category.")
        continue

    for idx, art in enumerate(articles[:5], start=1):

        # 🔹 AI MUST READ FULL NEWS
        text_for_ai = (
            art.get("content")
            or art.get("description")
            or art.get("title")
        )

        summary = summarize(
            text_for_ai,
            mode=summary_type
        )

        st.markdown(f"**{idx}.** {summary}")

        if st.button(
            f"📄 Read Full Article {idx}",
            key=f"{category}_{idx}"
        ):
            st.session_state.selected_article = art
            st.rerun()

        st.markdown("---")

    sources = sorted({a.get("source", "Unknown") for a in articles})
    st.caption(f"Sources: {', '.join(sources)}")

    st.divider()
