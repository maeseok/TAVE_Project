from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import *
from models import *
from route_comm import *
from model_serve import *
from apis_base import api_router

app = FastAPI()
router = APIRouter()

def include_cors(app):
    # 모든 origin에서 발생하는 요청들을 처리해 줌
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# api에서 라우터를 만들어서 등록
def include_router(app):
    return app.include_router(api_router)

def start_application():
    app = FastAPI(title="Webtoon", version="1.0")
    include_cors(app)
    include_router(app)
    return app

app = start_application()


# /get_actor_info 엔드포인트(모델에 image를 입력해서 배우 3명 리스트 출력 및 DB에서 배우의 image_url 조회)
@app.post("/get_actor_info")
async def get_actor_info(image_url: str, db: Session = Depends(get_db)):
    # 이미지를 모델에 전달하여 결과를 가져옴
    actor_names = model_serving_function(image_url)

    # 데이터베이스에서 배우 정보 조회
    actors_info = get_actors_info(actor_names, db)

    # 3명의 배우의 image_url을 조회
    #actors_image_urls = [actor_info.image_url for actor_info in actors_info]
    actors_info_dict = {actor.actor_name: actor.actor_image_url for actor in actors_info}

    # 결과 반환
    return  actors_info_dict
