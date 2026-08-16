from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {
        "application": "FastAPI Blog",
        "version": "0.1.0",
        "status": "running",
    }
