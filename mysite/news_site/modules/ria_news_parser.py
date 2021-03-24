from bs4 import BeautifulSoup
import requests
import json
import re


class News:
    def __init__(self, title, href, date='', text='', hype_rate=''):
        self.title = title
        self.href = href
        self.date = date
        self.hype_rate = hype_rate
        self.text = text
        pass

    def news_title(self):
        pass


def soup_getter(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    if page.status_code == 200:
        return soup


def get_hype_rate(url):
    base = 'https://ria.ru/services/dynamics/'
    hype = []
    js_parts_url = base + ''.join(re.findall(r'\b[0-9]{8}\b', url)) + '/' + \
                   ''.join(re.findall(r'[0-9]{10}', url)) + '.html'
    soup = soup_getter(js_parts_url)
    for elem in soup.find_all('span', class_='m-value'):
        hype.append(elem.text)
    # comment = soup.find_all('a', class_='js__toggle-chat-article color-bg-hover')
    # hype.append(comment.find_all)
    return hype[:-8:-1]



rss = soup_getter('https://ria.ru/export/rss2/archive/index.xml')
for elem in rss.find_all('item'):
    title = elem.title.text
    href = elem.guid.text
    date = elem.pubdate.text
    text = elem.description.text
    hype = get_hype_rate(href)
    n = News(title, href, date, text, str(hype))
    print(n.hype_rate)
    print(n.href)
