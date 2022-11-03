import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/")
def root():
    return {"hello world": "abc"}


def main():
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
