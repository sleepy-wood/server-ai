import uvicorn
from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    port: int = 8000
    clip_host: str = "localhost"
    clip_port: int = 51000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


app = FastAPI()


@app.get("/api/v1/")
def root():
    return {"hello world": "abc"}


def main():
    settings = Settings()
    uvicorn.run(app, host="0.0.0.0", port=settings.port)
