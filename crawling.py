import requests # 크롤링을 하기 위한 모듈
from bs4 import BeautifulSoup # 크롤링한 데이터를 사용할 수 있는 형태의 의미있는 데이터로 정리하기 위한 모듈
from datetime import datetime # 오늘 날짜를 얻기 위한 모듈

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%83%91100" # 크롤링 하고자 하는 사이트를 입력
response = requests.get(url) # requests.get을 통한 return 값을 response에 넣는다.

# BeautifulSoup는 의미있는 데이터로 만들어준다. response.text의 형식은 str 형식이기 때문에 BeautifulSoup를 이용해 정보를 사용하기 좋은 형태로 정리를 해준다.
soup = BeautifulSoup(response.text, 'html.parser')
response.encoding = 'utf-8' # 크롤링한 파일이 깨지는 것을 막기 위한 코드입니다. 
# (1) BeautifulSoup(데이터, 파싱) --> 데이터는 html이 들어가야 한다. 파싱 작업은 우리가 필요한 의미 있는 데이터들로 정리할 수 있도록 도와준다. 파이썬에 있는 기본 파싱도구 'html.parser'를 이용할 수 있다. 
# (2) soup.tilte을 해보면 html에서 title 태그 자체를 가져오는 코드이다. 단, 첫 번째 등장하는 태그만을 출력. findAll 사용
# (3) soup.title.string을 하면 title 태그 안에 있는 내용을 출력한다. 
# (4) soup.findAll('span')을 하면 크롤링한 html 파일에서 span 이라는 태그를 가진 모든 것을 출력해준다.

# (1) file = open("naver.html", "w", encoding='utf-8') <--- file 을 만들어서 크롤링한 데이터를 넣는 파일을 만드는 코드 3줄
# (2) file.write(response.text)
# (3) file.close()

music_rank_file = open("musicrank.txt", "w", encoding = 'utf-8') # 윈도우 기반의 컴퓨터는 encoding = 'utf-8'을 써줘야 글씨가 안 깨진다. 

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 차트 순위입니다.\n")) # 실시간으로 추출하고 있는 날짜를 나타낸다. 

rank = 1
results = soup.findAll("a", "tit")
for result in results:
    music_rank_file.write(str(rank)+ "위: " + result.get_text() + "\n") 
    # (1) BeautifulSoup를 해논 크롤링 데이터에서 findAll을 적용해서 데이터를 선별한 후 .get_text()를 사용하면 태그로 둘러싸인 글자의 값만 얻을 수 있다. 
    # (2) 위에서 받아온 데이터를 파일로 출력해보기
    # (3) open 함수의 모드 r(read), w(write), a(append) 세 가지 모드가 있다. 
    rank += 1

music_rank_file.close() # 열었던 파일은 꼭 닫아줘야 한다. 