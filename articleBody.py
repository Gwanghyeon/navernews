import bs4, requests

# this file is imported to navernews.py
url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=079&aid=0003373061&date=20200617&type=1&rankingSeq=6&rankingSectionId=100'

def getArticleBody(url):
    r = requests.get(url)
    htmlFile = r.text
    soup = bs4.BeautifulSoup(htmlFile, 'lxml')
    targetText = soup.select('#articleBodyContents')[0].stripped_strings
    for string in targetText:
        if '사진' in string or '그래픽' in string:
            continue
        print(f'  {string}')

if __name__ == '__main__':
    getArticleBody(url)
