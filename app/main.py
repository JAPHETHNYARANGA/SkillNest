from fastapi import FastAPI
from app.api.routes import users, courses
from app.core.config import settings
from app.db.init_db import init_db


init_db()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="CourseCraft - Online Course Platform",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


app.include_router(users.router, prefix=settings.API_V1_STR)
app.include_router(courses.router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to CourseCraft!"}