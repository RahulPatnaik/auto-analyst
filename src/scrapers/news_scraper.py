from gnews import GNews
import json, os

def get_news(company, save_dir):
    google_news = GNews(language='en', country='US', max_results=10)
    news = google_news.get_news(company)

    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, f"{company}.json"), 'w') as f:
        json.dump(news, f, indent=2)

    print(f"[✓] Saved news for {company}")

# Example:
# get_news("OpenAI", "/content/drive/MyDrive/auto_analyst_data/raw/news")
