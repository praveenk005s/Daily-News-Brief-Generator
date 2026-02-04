from fastapi import FastAPI, Query
from api.news_service import fetch_live_news

app = FastAPI(
    title="Live News Scraper API",
    description="Free live news API using GNews + RSS",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "Live News Scraper API is running"}

@app.get("/news/live")
def get_live_news(
    category: str = Query(
        default="technology",
        description="News category (technology, business, sports, politics)"
    )
):
    articles = fetch_live_news(category)

    return {
        "category": category,
        "count": len(articles),
        "articles": articles
    }
