from script.summarizer import summarize

def generate_category_brief(article_summaries, mode="short"):
    """
    article_summaries: list of short summaries
    returns: one consolidated category brief
    """

    if not article_summaries:
        return "No major updates available for today."

    combined_text = " ".join(article_summaries)

    # Generate higher-level summary
    brief = summarize(
        combined_text,
        mode="detailed" if mode == "detailed" else "short"
    )

    return brief
