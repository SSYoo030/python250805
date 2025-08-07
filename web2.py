#web2.py

from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://www.clien.net/service/board/sold"# URL을 입력하세요

#함수 체인(메서드 체인)
data = urllib.request.urlopen(url).read()  # URL에서 데이터를 읽어옵니다
soup = BeautifulSoup(data, "html.parser")
for tag in soup.find_all('span', attrs={'data-role': 'list-title-text'}):
    title = tag.text.strip()  # 제목을 가져옵니다
    print(title)  # 제목을 출력합니다


#페이지로딩
#<span class="subject_fixed" data-role="list-title-text" title="아이폰 13미니 256 팝니다">
#       아이폰 13미니 256 팝니다
#</span>



