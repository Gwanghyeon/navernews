import requests, sys, re
from bs4 import BeautifulSoup
from datetime import datetime
from articleBody import getArticleBody

r = requests.get('https://news.naver.com/main/home.nhn')
htmlFile = r.text
soup = BeautifulSoup(htmlFile, 'lxml')
d = datetime.now()
base_url = 'https://news.naver.com/'
section = ['pol', 'eco', 'soc', 'lif', 'wor', 'sci']
sectionName = ['정치', '경제', '사회', '생활/문화', '세계', 'IT/과학']
timeFormat = d.strftime("%m월%d일 %I:%M %p")

def run(newsType):
    tag_all = soup.find_all(class_=re.compile("rig.rank"+section[newsType]))
    newsUrls = []
    print("\n가장 많이 본 뉴스:"+sectionName[newsType], timeFormat)
    for i, headline in enumerate(tag_all, start=1):
        url = base_url + headline.attrs['href']
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

try:
    newsType=int(input("보고싶은 뉴스 번호를 선택하세요:\n1:정치\n2:경제\n3:사회\n4:생활/문화\n5:세계\n6:IT/과학\n👉 ")) - 1
except ValueError:
    print("1부터 6까지 숫자만 눌러주세요")
    sys.exit()

run(newsType)

