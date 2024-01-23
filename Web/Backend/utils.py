from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import *

# 웹툰 이름으로 웹툰 ID를 찾는 함수
def get_webtoon_id(webtoon_name: str, db: Session = Depends(get_db)):
    webtoon = db.query(Webtoon).filter(Webtoon.webtoon_name == webtoon_name).first()
    if not webtoon:
        raise HTTPException(status_code=404, detail="Webtoon not found")
    return webtoon.webtoon_id


def get_webtoon_characters(webtoon_name: str, db: Session):
    # 특정 웹툰 이름에 해당하는 웹툰 캐릭터들을 조회하는 로직
    characters = db.query(WebtoonCharacter.character_name).filter(WebtoonCharacter.webtoon_name == webtoon_name).all()

    # 만약 해당 웹툰 이름에 해당하는 캐릭터들이 없으면 예외를 발생시킴
    if not characters:
        raise HTTPException(status_code=404, detail=f"Webtoon characters not found for the given name: {webtoon_name}")

    # 캐릭터들의 이름 리스트를 반환
    return [character.character_name for character in characters]


# 데이터베이스 조회 함수
def get_character_image_url(character_name, db: Session = Depends(get_db)):
    # 데이터베이스에서 캐릭터의 이미지 URL을 조회하는 로직
    image_url = db.query(WebtoonCharacter.image_url).filter(WebtoonCharacter.character_name == character_name).scalar()
    # 만약 데이터베이스에서 캐릭터 정보를 가져오지 못하면 예외를 발생시킴
    if not image_url:
        raise HTTPException(status_code=404, detail="Character not found")
    return image_url        


# 데이터베이스 조회 함수
def get_actors_info(actor_names, db: Session = Depends(get_db)):
    # MySQL 데이터베이스에서 배우 정보(이름, url만)를 조회하는 로직
    #actors_url = db.query(Actor.actor_image_url).filter(Actor.actor_name.in_(actor_names)).all()
    actors_info = db.query(Actor.actor_name, Actor.actor_image_url).filter(Actor.actor_name.in_(actor_names)).all()

    # 만약 데이터베이스에서 배우 정보를 가져오지 못하면 예외를 발생시킴
    if not actors_info:
        raise HTTPException(status_code=404, detail="Actors not found")
    return actors_info
