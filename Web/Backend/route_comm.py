from fastapi import APIRouter, Depends, Request
from utils import *
from model_serve import *
router = APIRouter()

@router.get("/")
def read_root(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}

# /get_characters 엔드포인트: 웹툰 이름을 받아 해당 웹툰 캐릭터들의 이름을 반환
@router.get("/get_characters")
async def get_characters(webtoon_name: str, db: Session = Depends(get_db)):
    characters = get_webtoon_characters(webtoon_name, db)
    return characters

# /get_actor_image_url 엔드포인트(모델에 image_url입력해서 배우 3명 리스트 출력)
@router.get("/get_actor_name")
async def get_actor_name(character_name: str, db: Session = Depends(get_db)):
    # 데이터베이스에서 캐릭터의 이미지 URL을 조회
    image_url = get_character_image_url(character_name, db)
    # 모델 서빙 함수를 통해 결과를 가져옴
    model_result = model_serving_function(image_url)
    return model_result

