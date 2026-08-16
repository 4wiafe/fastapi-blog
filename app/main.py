from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {
        "application": "FastAPI Blog",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/about")
async def about():
    return {
        "developer": "Richmond Wiafe",
        "project": "FastAPI Blog",
        "language": "Python",
    }
