import requests
from bs4 import BeautifulSoup

def scrape_latest_news():
    url = 'https://www.bbc.com/news'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []

    # Update this if BBC changes the structure
    articles = soup.select('a.gs-c-promo-heading')[:5]

    for article in articles:
        title = article.get_text(strip=True)
        link = article.get('href')

        if link and not link.startswith('http'):
            link = 'https://www.bbc.com' + link

        news_items.append({'title': title, 'link': link})

    return {"news": news_items}
