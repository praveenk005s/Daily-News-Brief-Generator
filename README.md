🗞️ AI-Based Daily News Brief Generator

An end-to-end AI-powered news aggregation and summarization application that delivers personalized daily news briefs based on user preferences.
The system collects live news from multiple sources, summarizes full articles using NLP models, and presents short or detailed summaries in a clean, user-friendly interface.

📌 Problem Overview

In today’s fast-paced digital world, users are overwhelmed by news from multiple platforms.
Most news applications provide generic headlines, forcing users to manually browse categories and read long articles.

This project solves that problem by:

Personalizing news content

Summarizing full articles into short or detailed briefs

Reducing information overload

Helping users stay informed efficiently

🎯 Project Objective

The goal of this project is to:

Build a personalized AI-powered application

Aggregate news from multiple sources

Generate concise, readable summaries

Allow users to customize:

News categories

Reading preference (short / detailed)

Date

Deliver a clean and intuitive user experience

Deploy a publicly accessible application

🚀 Features
✅ User Preference Management

Select one or more news categories:

Technology

Business

Sports

Health

Entertainment

Politics

Save preferences for default homepage display

✅ Live News Collection

Fetches real-time news using free-tier APIs

Supports:

Public News APIs (GNews)

RSS feeds (extensible)

Avoids single-source dependency

✅ AI-Powered Summarization

Reads full article content

Generates:

Short summaries (2–3 sentences)

Detailed summaries (5–7 sentences)

Uses Hugging Face Transformers

Eliminates instruction leakage and repetition

✅ Full Article View

Click “Read Full Article”

View:

Title

Source

Published date

Full article content

External source link

Navigate back without page reload issues

✅ Customization Options

Change:

News category dynamically

Reading preference

Date (for historical context)

Refresh latest news instantly

✅ Clean Home Page Experience

Personalized daily brief shown by default

Section-wise layout per category

Source and timestamp included

No forced external navigation

🧾 Input & Output
🔹 Input

User-selected news segments

Optional date selection

Reading preference:

Short

Detailed

🔹 Output (Example)
Your Daily Technology Brief – 14 Nov 2025

• AI regulation discussions intensify across global markets
• Major tech firm announces new open-source AI framework
• Cybersecurity concerns rise following recent data breaches

Sources: BBC, Reuters, The Hindu



🛠️ Tech Stack
Backend

Python

Hugging Face Transformers (FLAN-T5)

Requests (API calls)

News Sources

GNews API (Free tier)

RSS-ready architecture

AI / NLP

google/flan-t5-base (text generation)

Prompt-controlled summarization

Frontend

Streamlit

Storage

JSON-based user preference storage

Deployment

Streamlit Cloud / Render / Hugging Face Spaces

📁 Project Structure
news_generator/
│
├── app.py                      # Streamlit frontend
├── script/
│   ├── news_fetcher.py         # News API integration
│   ├── summarizer.py           # AI summarization logic
│   ├── deduplicator.py         # Remove duplicate articles
│   └── preferences.py          # Save/load user preferences
│
├── utils/
│   ├── constants.py            # Category constants
│   └── time_utils.py           # Date formatting helpers
│
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/news-generator.git
cd news-generator

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set API Key
export GNEWS_API_KEY=your_api_key_here
# Windows PowerShell:
$env:GNEWS_API_KEY="your_api_key_here"

5️⃣ Run Application
streamlit run app.py

🌐 Deployment

The application is designed to be deployed on:

Streamlit Cloud

Render

Hugging Face Spaces

Judges can:

Select categories

Change dates

Switch between short & detailed summaries

View full articles without local setup


🔮 Future Enhancements

User authentication

Email-based daily briefs

Topic-based sentiment analysis

Offline dataset support

👨‍💻 Author

Praveen Kumar
AI & Data Science Enthusiast
