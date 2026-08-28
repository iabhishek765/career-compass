import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.prediction import router as prediction_router
from app.routes.report import router as report_router
from src.database.initialize_database import initialize_database


app = FastAPI(
    title="Career Compass API",
    version="1.0.0"
)


initialize_database()


frontend_url = os.getenv(
    "FRONTEND_URL",
    "http://localhost:3000"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        frontend_url,
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://career-compass-frontend-ybm8.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(prediction_router)
app.include_router(report_router)


@app.get("/")
def root():
    return {
        "message": "Career Compass API is running"
    }