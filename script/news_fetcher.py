import os
import requests

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

BASE_URL = "https://gnews.io/api/v4/top-headlines"

CATEGORY_MAP = {
    "Technology": "technology",
    "Business": "business",
    "Sports": "sports",
    "Health": "health",
    "Entertainment": "entertainment",
    "Politics": "nation",
}

def fetch_news(category, max_articles=10):
    if not GNEWS_API_KEY:
        raise RuntimeError("GNEWS_API_KEY not set")

    params = {
        "apikey": GNEWS_API_KEY,
        "category": CATEGORY_MAP.get(category, "general"),
        "lang": "en",
        "country": "in",
        "max": max_articles,
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    articles = []
    for item in data.get("articles", []):
        articles.append({
            "title": item.get("title"),
            "description": item.get("description"),
            "content": item.get("content"),  # IMPORTANT
            "url": item.get("url"),
            "source": item.get("source", {}).get("name", "GNews"),
            "publishedAt": item.get("publishedAt"),
        })

    return articles
