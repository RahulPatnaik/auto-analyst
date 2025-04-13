import requests
from bs4 import BeautifulSoup
import json
import os

def get_wikipedia_summary(company, save_dir):
    url = f"https://en.wikipedia.org/wiki/{company.replace(' ', '_')}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    paragraphs = soup.select('p')
    summary = ''
    for p in paragraphs:
        if p.text.strip():
            summary = p.text.strip()
            break

    data = {
        "company": company,
        "source": url,
        "summary": summary
    }

    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, f"{company}.json"), 'w') as f:
        json.dump(data, f, indent=2)

    print(f"[✓] Saved summary for {company}")