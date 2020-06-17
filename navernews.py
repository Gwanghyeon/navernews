import requests, sys
from bs4 import BeautifulSoup
from pprint import pprint
import re, sys
from datetime import datetime
from articleBody import getArticleBody

result = requests.get('https://news.naver.com/main/home.nhn')
src = result.content
soup = BeautifulSoup(src, 'lxml')
d = datetime.now()

class News:

    base_url = 'https://news.naver.com/'
    section = ['pol', 'eco', 'soc', 'lif', 'wor', 'sci']
    sectionName = ['정치', '경제', '사회', '생활/문화', '세계', 'IT/과학']
    timeFormat = d.strftime("%m월%d일 %I:%M %p")

    def politics(self):
        base_url = self.base_url
        section = self.section
        sectionName = self.sectionName
        timeFormat = self.timeFormat
        tag_all = soup.find_all(class_=re.compile("rig.rank"+section[0]))
        newsUrls = []
        print("\n가장 많이 본 뉴스:"+sectionName[0], timeFormat)
        for i, headline in enumerate(tag_all, start=1):
            url = self.base_url + headline.attrs['href']
            title = headline.text
            print(f'{i} | {title}\n{url}')
            newsUrls.append(url)
        try:
            choice = int(input('\n읽고 싶으신 기사 번호를 선택하세요: ')) - 1
        except ValueError:
            sys.exit()
        print()
        print(f'{choice + 1}| {tag_all[choice].text}')
        url = newsUrls[choice]
        getArticleBody(url)

    def economy(self):
        base_url = self.base_url
        section = self.section
        sectionName = self.sectionName
        timeFormat = self.timeFormat
        tag_all = soup.find_all(class_=re.compile("rig.rank"+section[1]))
        newsUrls = []
        print("\n가장 많이 본 뉴스:"+sectionName[1], timeFormat)
        for i, headline in enumerate(tag_all, start=1):
            url = self.base_url + headline.attrs['href']
            title = headline.text
            print(f'{i} | {title}\n{url}')
            newsUrls.append(url)
        try:
            choice = int(input('\n읽고 싶으신 기사 번호를 선택하세요: ')) - 1
        except ValueError:
            sys.exit()
        print()
        print(f'{choice + 1}| {tag_all[choice].text}')
        url = newsUrls[choice]
        getArticleBody(url)

    def society(self):
        base_url = self.base_url
        section = self.section
        sectionName = self.sectionName
        timeFormat = self.timeFormat
        tag_all = soup.find_all(class_=re.compile("rig.rank"+section[2]))
        newsUrls = []
        print("\n가장 많이 본 뉴스:"+sectionName[2], timeFormat)
        for i, headline in enumerate(tag_all, start=1):
            url = self.base_url + headline.attrs['href']
            title = headline.text
            print(f'{i} | {title}\n{url}')
            newsUrls.append(url)
        try:
            choice = int(input('\n읽고 싶으신 기사 번호를 선택하세요: ')) - 1
        except ValueError:
            sys.exit()

        print()
        print(f'{choice + 1}| {tag_all[choice].text}')
        url = newsUrls[choice]
        getArticleBody(url)

    def life(self):
        base_url = self.base_url
        section = self.section
        sectionName = self.sectionName
        timeFormat = self.timeFormat
        tag_all = soup.find_all(class_=re.compile("rig.rank"+section[3]))
        newsUrls = []
        print("\n가장 많이 본 뉴스:"+sectionName[3], timeFormat)
        for i, headline in enumerate(tag_all, start=1):
            url = self.base_url + headline.attrs['href']
            title = headline.text
            print(f'{i} | {title}\n{url}')
            newsUrls.append(url)
        try:
            choice = int(input('\n읽고 싶으신 기사 번호를 선택하세요: ')) - 1
        except ValueError:
            sys.exit()

        print()
        print(f'{choice + 1}| {tag_all[choice].text}')
        url = newsUrls[choice]
        getArticleBody(url)

    def world(self):
        base_url = self.base_url
        section = self.section
        sectionName = self.sectionName
        timeFormat = self.timeFormat
        tag_all = soup.find_all(class_=re.compile("rig.rank"+section[4]))
        newsUrls = []
        print("\n가장 많이 본 뉴스:"+sectionName[4], timeFormat)
        for i, headline in enumerate(tag_all, start=1):
            url = self.base_url + headline.attrs['href']
            title = headline.text
            print(f'{i} | {title}\n{url}')
            newsUrls.append(url)
        try:
            choice = int(input('\n읽고 싶으신 기사 번호를 선택하세요: ')) - 1
        except ValueError:
            sys.exit()
        print()
        print(f'{choice + 1}| {tag_all[choice].text}')
        url = newsUrls[choice]
        getArticleBody(url)

    def science(self):
        base_url = self.base_url
        section = self.section
        sectionName = self.sectionName
        timeFormat = self.timeFormat
        tag_all = soup.find_all(class_=re.compile("rig.rank"+section[5]))
        newsUrls = []
        print("\n가장 많이 본 뉴스:"+sectionName[5], timeFormat)
        for i, headline in enumerate(tag_all, start=1):
            url = self.base_url + headline.attrs['href']
            title = headline.text
            print(f'{i} | {title}\n{url}')
            newsUrls.append(url)
        try:
            choice = int(input('\n읽고 싶으신 기사 번호를 선택하세요: ')) - 1
        except ValueError:
            sys.exit()
        print()
        print(f'{choice + 1}| {tag_all[choice].text}')
        url = newsUrls[choice]
        getArticleBody(url)

news = News()
sectionNumDict = {1: news.politics, 2: news.economy, 3: news.society, 4: news.life, 5: news.world, 6: news.science}

try:
    newsType=int(input("보고싶은 뉴스 번호를 선택하세요:\n1:정치\n2:경제\n3:사회\n4:생활/문화\n5:세계\n6:IT/과학\n👉 "))
except ValueError:
    print("1부터 6까지 숫자만 눌러주세요")
    sys.exit()

sectionNumDict[newsType]()

