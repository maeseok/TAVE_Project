from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as req
import requests
import json
from selenium import webdriver
from time import sleep
import pandas as pd
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}




url = "https://comic.naver.com/webtoon" # 접근할 url
res = requests.get(url,headers=headers) # 원하는 url의 정보
print(res.text)
#print(res.raise_for_status()) # 웹페이지의 상태가 정상인지 확인
#url="https://comic.naver.com/webtoon/list?titleId=814512"
#data = requests.get(url,headers=headers).text
#print(data)
#value= data.json()   
#kospi = value['result']['siseList']
#df=pd.DataFrame(kospi)
#df=df[['cd','dt','ov','ncv','cv','cr']] #특정 열 선택
#df = df.rename(columns={'cd':'code',"dt":"date",'ov':'open','ncv':'close','cv':'diff','cr':'rate'}) #열 이름 변경
#print(value)

https://comic.naver.com/webtoon/detail?titleId=769209&no=93&week=wed
https://comic.naver.com/webtoon/detail?titleId=769209&no=92&week=wed

https://comic.naver.com/webtoon/detail?titleId=814512&no=14&week=thu
https://comic.naver.com/webtoon/detail?titleId=814512&no=13&week=thu