#자주 쓰는 쿼리들을 모델화해서 넣어놓은 것
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel

class Actor(Base):
    __tablename__ = "actors"
    actor_id = Column(Integer, primary_key=True, index=True)
    actor_name = Column(String, nullable=False)
    actor_image_url = Column(String, nullable=False)

class Webtoon(Base):
    __tablename__ = "webtoons"

    webtoon_id = Column(Integer, primary_key=True, index=True)
    webtoon_name = Column(String, index=True)
    
    characters = relationship("WebtoonCharacter", back_populates="webtoon")


class WebtoonCharacter(Base):
    __tablename__ = "webtoon_characters"
    character_id = Column(Integer, primary_key=True, index=True)
    character_name = Column(String, index=True)
    image_url = Column(String)
    webtoon_name = Column(String)
    webtoon_id = Column(Integer, ForeignKey("webtoons.webtoon_id"))
    webtoon = relationship("Webtoon", back_populates="characters")

#pydantic은 파이썬 타입 어노테이션을 사용해서 데이터 유효성 검사와 설정 관리를 하는 라이브러리
class WebtoonInput(BaseModel):
    webtoon_character: str