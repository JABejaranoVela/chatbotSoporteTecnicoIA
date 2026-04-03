from fastapi import APIRouter

from app.api.endpoints import chat, health, pages


api_router = APIRouter()
api_router.include_router(pages.router, tags=["pages"])
api_router.include_router(health.router, tags=["health"])
api_router.include_router(chat.router, tags=["chat"])
