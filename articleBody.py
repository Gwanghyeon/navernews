import bs4, requests

# this file is imported to navernews.py

def getArticleBody(url):
    r = requests.get(url)
    htmlFile = r.text
    soup = bs4.BeautifulSoup(htmlFile, 'html.parser')
    targetText = soup.select('#articleBodyContents')[0].stripped_strings
    for string in targetText:
        if '사진' in string or '그래픽' in string:
            continue
        print(f'  {string}')

if __name__ == '__main__':
    getArticleBody(url)
