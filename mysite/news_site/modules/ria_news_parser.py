from bs4 import BeautifulSoup
import requests
import json
import re


from bs4 import BeautifulSoup
import requests
import json
import re
import urllib.parse as urlparse
from requests.exceptions import MissingSchema


class News:
    def __init__(self, title, href, date='', text='', hype_rate=''):
        self.title = title
        self.href = href
        self.date = date
        self.hype_rate = hype_rate
        self.text = text
        pass

    @staticmethod
    def soup_getter(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")
        if page.status_code == 200:
            return soup

    @staticmethod
    def get_hype_rate(url):
        base = 'https://ria.ru/services/dynamics/'
        hype = []
        js_parts_url = base + ''.join(re.findall(r'\b[0-9]{8}\b', url)) + '/' + \
                       ''.join(re.findall(r'[0-9]{10}', url)) + '.html'
        soup = News.soup_getter(js_parts_url)
        for elem in soup.find_all('span', class_='m-value'):
            hype.append(elem.text)
        # comment = soup.find_all('a', class_='js__toggle-chat-article color-bg-hover')
        # hype.append(comment.find_all)
        return hype[:-8:-1]

    @staticmethod
    def get_rss_feed(url):
        rss = ''
        soup = News.soup_getter(url)
        try:
            rss_url = soup.find(lambda tag: tag.name == "a" and "RSS" in tag.text)['href']
        except TypeError:
            try:
                rss_url = soup.find('a', attrs={'href': re.compile(r"rss")}).get('href')
            except TypeError:
                return "Не удалось получить RSS ленту сайта"
        try:
            rss = News.soup_getter(rss_url)
        except MissingSchema:
            rss = News.soup_getter(urlparse.urljoin(url, rss_url))
        return rss


def main():
    rss = News.soup_getter(News.get_rss_feed('https://ria.ru/'))
    for elem in rss.find_all('item'):
        title = elem.title.text
        href = elem.guid.text
        date = elem.pubdate.text
        text = elem.description.text
        hype = News.get_hype_rate(href)
        n = News(title, href, date, text, str(hype))
        print(n.hype_rate)
        print(n.href)


if __name__ == '__main__':
    main()