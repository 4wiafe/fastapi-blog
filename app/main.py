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


@app.get("/users/me")
async def get_current_user():
    return {
        "user_id": 1,
        "username": "richmond",
        "email": "richmond@email.com",
    }


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,
        "username": "richtfmenace",
        "email": "rich@email.com",
    }
