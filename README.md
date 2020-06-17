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


## Update
Put article number to read the body or the article you want to read when prompt like this:
```
읽고 싶으신 기사 번호를 선택하세요:
```

The result follows as:
```
읽고 싶으신 기사 번호를 선택하세요: 2

2| "개성에 남겨둔 자산 9000억…억장 무너져"
  애타는 개성공단 입주기업들
  현대아산도 긴급 대책회의
  ◆ 벼랑 끝 남북관계 ◆
  정기섭 개성공단기업협회장(앞줄 왼쪽)과 입주 기업 대표들이 17일 여의도 개성공단협회에서 기자회견을 열고 있다. [한주형 기자]
  북한이 16일 개성 남북공동연락사무소를 폭파한 것에 대해 개성공단 입주기업들이 "억장이 무너진다"며 우리 정부에 사태 해결을 촉구하고 나섰다. 이들은 북한이 예고한 '개성공단 완전 철거'도 현실화될 가능성이 높아진 것으로 우려하고 있다.
  17일 개성공단기업협회 비상대책위원회는 입장문을 내고 "개성공단은 남북 국민들의 땀과 열정으로 가꾸어온 평화 공단"이라며 "공단 재개를 영구히 막는 더 이상의 조치를 자제할 것을 촉구한다"고 밝혔다.
...
```

## Required
- Run ```$ pip install -r requirements.txt``` in your terminal to install required python libraries.
- This program doesn't use Naver API, so you don't need api keys to use this program.

All news are provided in **Korean**.
