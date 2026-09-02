from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome to my blog"}


@app.get("/healthcheck")
async def check_health():
    return {"status": "ok"}
