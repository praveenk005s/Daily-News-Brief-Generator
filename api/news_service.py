import requests
import feedparser
import os

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

RSS_FEEDS = {
    "technology": [
        "https://feeds.bbci.co.uk/news/technology/rss.xml",
        "https://feeds.reuters.com/reuters/technologyNews"
    ],
    "business": [
        "https://feeds.reuters.com/reuters/businessNews"
    ],
    "sports": [
        "https://www.espn.com/espn/rss/news"
    ],
    "politics": [
        "https://feeds.bbci.co.uk/news/politics/rss.xml"
    ]
}

# ---------------------------
# GNews API (Primary)
# ---------------------------
def fetch_from_gnews(category: str):
    if not GNEWS_API_KEY:
        return []

    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "topic": category,
        "lang": "en",
        "max": 10,
        "token": GNEWS_API_KEY
    }

    try:
        r = requests.get(url, params=params, timeout=5)
        data = r.json()

        return [{
            "title": a["title"],
            "description": a["description"],
            "source": a["source"]["name"],
            "published": a["publishedAt"]
        } for a in data.get("articles", [])]

    except Exception:
        return []

# ---------------------------
# RSS fallback
# ---------------------------
def fetch_from_rss(category: str):
    articles = []

    for feed_url in RSS_FEEDS.get(category, []):
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            articles.append({
                "title": entry.title,
                "description": entry.get("summary", ""),
                "source": feed.feed.get("title", "RSS"),
                "published": entry.get("published", "")
            })

    return articles

# ---------------------------
# Unified fetch
# ---------------------------
def fetch_live_news(category: str):
    category = category.lower()

    articles = fetch_from_gnews(category)

    if not articles:
        articles = fetch_from_rss(category)

    return articles
