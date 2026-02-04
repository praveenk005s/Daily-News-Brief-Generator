def remove_duplicates(articles):
    if not articles:
        return []

    seen = set()
    unique = []

    for art in articles:
        key = (art.get("title"), art.get("source"))
        if key not in seen:
            seen.add(key)
            unique.append(art)

    return unique
