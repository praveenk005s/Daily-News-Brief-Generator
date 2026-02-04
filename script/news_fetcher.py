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
        return []   # ✅ SAFE fallback

    params = {
        "apikey": GNEWS_API_KEY,
        "category": CATEGORY_MAP.get(category, "general"),
        "lang": "en",
        "country": "in",
        "max": max_articles
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return []   # ✅ SAFE fallback

    articles = []
    for item in data.get("articles", []):
        articles.append({
            "title": item.get("title", ""),
            "description": item.get("description", ""),
            "content": item.get("content", ""),
            "url": item.get("url", ""),
            "source": item.get("source", {}).get("name", "GNews"),
            "publishedAt": item.get("publishedAt", datetime.utcnow().isoformat())
        })

    return articles
