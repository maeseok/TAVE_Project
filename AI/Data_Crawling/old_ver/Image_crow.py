from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os

#Chrome driver
print('Loading...')
options = ChromeOptions()
#options.add_argument("headless") #백그라운드 실행
options.add_experimental_option("detach", True)
#이 부분 미리 드라이버 다운로드 해놓으면 시간 약간 단축될 듯
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(30)

#폴더 생성 함수
def createFolder (name) :
    if os.path.isdir("./{}".format(name)) == False :
        os.mkdir("./{}".format(name))
        print('{} 폴더 생성 완료'.format(name))
    else :
        print('이미 존재하는 폴더입니다.')

'''def scroll_down(cnt):
    for i in range(cnt):
        driver.find_element(By.XPATH, '//body').send_keys(Keys.END)
        time.sleep(2)'''
        
#대용량 ver
def scroll_down():
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(2.5)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_elements(By.CSS_SELECTOR,".LZ4I").click() #스크롤을 내리다 보면 "결과 더보기"가 뜨는 경우 이를 클릭해준다
            except:
                break
        last_height = new_height
def scroll_down2():
    elem =driver.find_element(By.TAG_NAME, "body")
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    try:
        #'결과 더보기' 버튼의 원소를 selector로 찾아 클릭한다
        driver.find_element(By.CSS_SELECTOR, '#islmp > div > div > div > div > div.C5Hr4 > div.K414Oe > div.FAGjZe > input').click()

        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
    except:
        pass
#배우 이미지 다운로드 함수
def DownloadImage(keyword,size):
    for i in range(len(keyword)):
        url = 'https://www.google.com/search?tbm=isch&q={}'.format(keyword[i])
        driver.get(url)
        scroll_down2()
        createFolder(keyword[i])
        #이미지 src 추출
        img = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
        src = [i.get_attribute('src') for i in img]
        
        tmp=0
        for j in range(size):
            tmp+=1
            #이미지 URL 다운로드
            try:
                urllib.request.urlretrieve(src[j], "./{}\\Image_{}.jpg".format(keyword[i],tmp))
                print(tmp)
                print("[%] Download : Success  ({}{})".format(keyword[i],j+1))
                print()
            except:
                print("[%] Download : Fail")
                tmp-=1

#폴더 생성
createFolder("배우사진")
os.chdir('./배우사진')

#배우 리스트
#https://namu.wiki/w/%EB%B0%B0%EC%9A%B0/%ED%95%9C%EA%B5%AD

# 사이트 접속하기
keyword=["강동원"] #인물 리스트만 설정하면 될 듯
DownloadImage(keyword,500)