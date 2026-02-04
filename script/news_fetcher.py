import os
import requests
from datetime import datetime

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
BASE_URL = "https://gnews.io/api/v4/top-headlines"

CATEGORY_MAP = {
    "Technology": "technology",
    "Business": "business",
    "Sports": "sports",
    "Health": "health",
    "Entertainment": "entertainment",
    "Politics": "nation"
}

def fetch_news(category, max_articles=10):
    if not GNEWS_API_KEY:
        raise RuntimeError("GNEWS_API_KEY not set")

    params = {
        "apikey": GNEWS_API_KEY,
        "category": CATEGORY_MAP.get(category, "general"),
        "lang": "en",
        "country": "in",
        "max": max_articles
    }

    r = requests.get(BASE_URL, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    articles = []
    for item in data.get("articles", []):
        # 🔥 FULL CONTENT LOGIC
        full_text = " ".join(filter(None, [
            item.get("title"),
            item.get("description"),
            item.get("content")
        ]))

        articles.append({
            "title": item.get("title"),
            "content": full_text,
            "source": item.get("source", {}).get("name", "GNews"),
            "publishedAt": item.get("publishedAt", datetime.utcnow().isoformat()),
            "url": item.get("url")
        })

    return articles
