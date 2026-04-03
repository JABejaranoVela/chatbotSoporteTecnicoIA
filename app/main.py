from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import api_router


BASE_DIR = Path(__file__).resolve().parents[1]
FRONTEND_DIR = BASE_DIR / "frontend"


app = FastAPI(
    title="chatbot-soporte-tecnico-ia",
    description="Base API for an academic technical-support chatbot project.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory=FRONTEND_DIR / "static"), name="static")
app.include_router(api_router)
