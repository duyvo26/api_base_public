from fastapi import FastAPI
from app.routers import base

# Tạo instance của FastAPI
app = FastAPI()

# Include các router vào ứng dụng chính
app.include_router(base.router)


@app.route("/favicon.ico")
def favicon():
    return "", 204


@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application"}
