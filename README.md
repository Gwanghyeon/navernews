# navernews
Fetch the most viewed Naver news from five sections: politics, economy, society, life, world and science.

## How to 
1. Run ```$ python navernews.py``` in your terminal.
2. Choose a section number and hit enter. 1 for politics, 2 for economy, 3 for society, 4 for life, 5 for world, and 6 for science.
```
1:정치
2:경제
3:사회
4:생활/문화
5:세계
6:IT/과학
👉 
```
3. You will get the most viewed 10 articles in the section you chose. Result will be like this:
```가장 많이 본 뉴스: 세계 2020-06-07 06:40 PM
1 | 흑인아이 홀로 엘리베이터 타 참변…꼭대기층 누른 백인 여성
https://news.naver.com//main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=081&aid=0003096763&date=20200606&type=1&rankingSeq=1&rankingSectionId=104
2 | 백인 사모님은, 흑인의 하나뿐인 아들을 죽게 내버려뒀다
https://news.naver.com//main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=023&aid=0003537059&date=20200607&type=1&rankingSeq=2&rankingSectionId=104
3 | 13년전 英소녀, 24년전 獨소년…두 실종사건에 1명이 겹쳤다
https://news.naver.com//main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=025&aid=0003007120&date=20200607&type=1&rankingSeq=3&rankingSectionId=104
...
```
Feel free to go to any link for more details about the article.

## Required
- Run ```$ pip install -r requirements.txt``` in your terminal to install required python libraries.
- This program doesn't use Naver API, so you don't need api keys to use this program.

All news are provided in **Korean**.
