# TAVE  _Project
웹툰 실사화 배우 추천 시스템


![Untitled (1)](https://github.com/maeseok/TAVE_Project/assets/87814233/8d33ed25-1433-44a7-b02a-ee1921e2f5d4)





## 👨‍🏫 프로젝트 소개
최근 비질란테, 이두나 등 웹툰을 원작으로 실사화한 드라마가 이슈화됨에 따라 트렌드를 따라가는 주제 선정으로, 더 높은 유사도의 배우 캐스팅과 현재 실사화 되지 않은 웹툰의 궁금증 해결을 목표로 함.

## ⏲️ 개발 기간 
- 2023.11.11(토) ~ 2024.01.27(토)
- 주제 선정
- 데이터 수집
- 데이터 전처리
- 모델링
- 웹 페이지 구현
- 발표
  
## 🧑‍🤝‍🧑 개발자 소개 
TAVE_데이터 분석_12기
- **김동재** : 팀장, 클러스터링, VIT, 웹 페이지 구축 등
- **김광민** : 웹 페이지 구축 및 배포, 코사인 유사도 등
- **이수재** : 웹툰 벡터값 스케일링, CNN 등
- **[이형석](https://blog.naver.com/mae_seok)** : 크롤러 구축, Opencv 등
- **강민경** : 배우 벡터값 스케일링, SVM 등
- **김예영** : CNN, 논문 분석 등
  
## 💻 개발환경
- **IDE** : Visual Studio Code, Jupyter notebook, Colab
- **Framework** : Flutter, Fastapi
- **Library** : torch, face_recognition, sklearn, tensorflow etc.

## ⚙️ 기술 스택
- **Server** : Uvicorn
- **DataBase** : Mysql
- **온라인 회의** : Google meet
- **정보 공유** : Notion

  
## 📝 프로젝트 아키텍쳐
<img width="740" alt="KakaoTalk_20240123_015858502" src="https://github.com/maeseok/TAVE_Project/assets/87814233/145ae90f-928c-4dee-96d9-acbbb54af0f2">


![프로젝트 아키텍쳐](https://github.com/maeseok/TAVE_Project/assets/87814233/a755947d-6fc9-4234-810e-0bd422c8aee5)



## 📷 웹툰 얼굴 인식 및 특징점 추출
![Untitled (2)](https://github.com/maeseok/TAVE_Project/assets/87814233/18a500d5-a8be-46ab-8bf1-3415cabf3cd8)
![Untitled (3)](https://github.com/maeseok/TAVE_Project/assets/87814233/292c0278-47d5-4d27-a3a9-962abc60191a)


## 🎥 배우 얼굴 인식 및 특징점 추출
![KakaoTalk_20240123_012200282](https://github.com/maeseok/TAVE_Project/assets/87814233/0dd1c737-bf5c-42f3-af71-347f2db8cc12)
![KakaoTalk_20240123_004908356](https://github.com/maeseok/TAVE_Project/assets/87814233/1077f7fa-22ac-47f2-83fc-883da8e2b8f3)


## 📈 모델 성능 비교
![image](https://github.com/maeseok/TAVE_Project/assets/87814233/5f0ae995-9906-4f91-9ad2-eca797f55aa2)


## ❓ How to use?
![image](https://github.com/maeseok/TAVE_Project/assets/87814233/6e0c6cd3-ef51-4480-961c-613314e1d525)



1. 웹툰 및 인물 선택

  
2. VIT 모델을 통한 결과 추출


3. 관련있는 상위 3명의 배우 사진 출력

