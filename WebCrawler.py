# Un simplu WebCrawler utilizand modulele "requests" si "BeautifulSoup"

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://ziarultecucean.com/" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.findAll('a', {'rel': 'bookmark'}):
            href = link.get('href')
            print(href)
        page += 1

# Mai jos apelam functia creata mentionand si numarul de pagini dorite pentru indexare

trade_spider(2)
