from bs4 import BeautifulSoup 
import urllib.request
import os, re #태그 제거

#Access Denied 에러 우회
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

#크롤링 할 웹툰 주소로 웹 페이지 요청
html = urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=725586&weekday=fri")
soup = BeautifulSoup(html.read(),"html.parser") #웹 페이지 파싱
html.close() #닫기

comic_title = soup.find("div", {"class", "detail"}).find("h2").text.split()[0] #만화 이름

os.chdir("/Users/proqk/Downloads/") #다운로드 폴더
dir = comic_title
if not os.path.isdir(dir):
    os.mkdir(dir)
    print(comic_title+" 디렉토리 생성")
else:
    print("같은 이름의 디렉토리가 이미 있음")
os.chdir("/Users/proqk/Downloads/"+dir) #다운로드 받을 폴더로 이동


comic_list=[]
tmp_list=soup.select('td>a') #<td>안에 <a>태그에
for i in tmp_list:
    if('https' in i['href']): #다음 화를 미리 만나보세요 링크 패스
        continue
    comic_list.append(i['href'])
comic_list = sorted(set(comic_list))

for i in range(len(comic_list)):
    ep_url = url="https://comic.naver.com"+comic_list[i]
    html = urllib.request.urlopen(ep_url)
    soup2 = BeautifulSoup(html.read(),"html.parser")

    ep = soup2.find('h3') #<h3>이름</h3>
    ep_title = re.sub('<.*?>', '', str(ep)) #이름만 남게
    
    if not os.path.isdir(ep_title):
        os.mkdir(ep_title)
        print(ep_title+" 디렉토리 생성")
    else:
        print("같은 이름의 디렉토리가 이미 있음")
    os.chdir(ep_title) #이동

    img_div = soup2.find("div", {"class", "wt_viewer"})
    img_all = img_div.findAll("img")

    num = 1
    for j in img_all:
        img_path = j.get("src")
        img_num = str(num)+".png"
        urllib.request.urlretrieve(img_path, img_num)
        num = num + 1
    print(ep_title+" 다운로드 완료")
    os.chdir("..") #상위 폴더로

print("다운로드 끝")