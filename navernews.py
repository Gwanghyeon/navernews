import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re
from datetime import datetime

result = requests.get('https://news.naver.com/main/home.nhn')
src = result.content
soup = BeautifulSoup(src, 'lxml')
d = datetime.now()

class News:

    def politics(self):
        tag_all = soup.find_all(class_=re.compile("rig.rankpol"))
        base_url = 'https://news.naver.com/'
        print("\n가장 많이 본 뉴스: 정치", d.strftime("%Y-%m-%d %I:%M %p"))
        for i, headline in enumerate(tag_all, start=1):
            print('{} | {}\n{}'.format(str(i), headline.text, base_url+headline.attrs['href']))

    def economy(self):
        tag_all = soup.find_all(class_=re.compile("rig.rankeco"))
        base_url = 'https://news.naver.com/'
        print("\n가장 많이 본 뉴스: 경제", d.strftime("%Y-%m-%d %I:%M %p"))
        for i, headline in enumerate(tag_all, start=1):
            print('{} | {}\n{}'.format(str(i), headline.text, base_url+headline.attrs['href']))

    def society(self):
        tag_all = soup.find_all(class_=re.compile("rig.ranksoc"))
        base_url = 'https://news.naver.com/'
        print("\n가장 많이 본 뉴스: 사회", d.strftime("%Y-%m-%d %I:%M %p"))
        for i, headline in enumerate(tag_all, start=1):
            print('{} | {}\n{}'.format(str(i), headline.text, base_url+headline.attrs['href']))

    def life(self):
        tag_all = soup.find_all(class_=re.compile("rig.ranklif"))
        base_url = 'https://news.naver.com/'
        print("\n가장 많이 본 뉴스: 생활/문화", d.strftime("%Y-%m-%d %I:%M %p"))
        for i, headline in enumerate(tag_all, start=1):
            print('{} | {}\n{}'.format(str(i), headline.text, base_url+headline.attrs['href']))

    def science(self):
        tag_all = soup.find_all(class_=re.compile("rig.ranksci"))
        base_url = 'https://news.naver.com/'
        print("\n가장 많이 본 뉴스: IT/과학", d.strftime("%Y-%m-%d %I:%M %p"))
        for i, headline in enumerate(tag_all, start=1):
            print('{} | {}\n{}'.format(str(i), headline.text, base_url+headline.attrs['href']))

    def world(self):
        tag_all = soup.find_all(class_=re.compile("rig.rankwor"))
        base_url = 'https://news.naver.com/'
        print("\n가장 많이 본 뉴스: 세계", d.strftime("%Y-%m-%d %I:%M %p"))
        for i, headline in enumerate(tag_all, start=1):
            print('{} | {}\n{}'.format(str(i), headline.text, base_url+headline.attrs['href']))


news = News()
news_type=int(input("보고싶은 뉴스 번호를 선택하세요:\n1:정치\n2:경제\n3:사회\n4:생활/문화\n5:세계\n6:IT/과학\n👉 "))

if news_type == 1:
    news.politics()
elif news_type == 2:
    news.economy()
elif news_type == 3:
    news.society()
elif news_type == 4:
    news.life()
elif news_type == 6:
    news.science()
elif news_type == 5:
    news.world()
else:
    print("잘못된 요청입니다")

