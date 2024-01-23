from fastapi import APIRouter

router = APIRouter()
api_router = APIRouter()
api_router.include_router(router, prefix="/comm", tags=["comm"] )