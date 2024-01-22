from bs4 import BeautifulSoup
import requests
import os
import urllib

html = urllib.request.urlopen('https://comic.naver.com/webtoon/list?titleId=814512')
soup = BeautifulSoup(html.read(),'html.parser') #웹 페이지 파싱
html.close()

#웹툰 제목 따기 ( meta 태그의 content 내용 가져오기)
comic_title = soup.head.find('meta',{'property':'og:title'}).get('content')
comic_title

#다운로드 받을 폴더 생성
os.chdir('c:/Users/kdj19/Downloads/')
dir = comic_title
if not os.path.isdir(dir):
    os.mkdir(dir)
    print(comic_title+'디렉토리 생성')
else:
    print('같은 이름의 디렉토리가 이미 있음')
os.chdir('c:/Users/kdj19/Downloads/'+dir)

comic_list=[]
tmp_list=soup.select('td>a') #<li>안에 <a>태그에
# for i in tmp_list:
#     # if ('https' in i['href']):
#     #     continue
#     comic_list.append(i['href'])
# comic_list = sorted(set(comic_list))

# for i in range(len(comic_list)):
#     print(comic_list[i])

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=814512"

# 웹 페이지의 HTML 가져오기
response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

comic_list = []

# 'td' 태그 아래에 있는 'a' 태그를 선택
tmp_list = soup.select('td a')

# 'https'가 포함된 링크를 제외하고 comic_list에 추가
for a_tag in tmp_list:
    if 'https' in a_tag['href']:
        continue
    comic_list.append(a_tag['href'])

# 중복 제거 및 정렬
comic_list = sorted(set(comic_list))

# 결과 출력
for link in comic_list:
    print(link)

