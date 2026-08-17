from typing import Annotated
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()

# Fake database for now
fake_posts_db = [
    {
        "post_id": 1,
        "title": "Hello FastAPI",
        "content": "My first post",
        "author": "Richmond Wiafe",
        "published": True,
    },
    {
        "post_id": 2,
        "title": "Why Python Rocks",
        "content": "Speed of dev matters",
        "author": "Sarah Johnson",
        "published": True,
    },
    {
        "post_id": 3,
        "title": "Async Explained",
        "content": "No more blocking",
        "author": "David Kim",
        "published": False,
    },
    {
        "post_id": 4,
        "title": "PostgreSQL Tips",
        "content": "Indexes are your friend",
        "author": "Emily Chen",
        "published": True,
    },
    {
        "post_id": 5,
        "title": "Deploying to Prod",
        "content": "Docker and beyond",
        "author": "Michael Brown",
        "published": False,
    },
    {
        "post_id": 6,
        "title": "Testing APIs",
        "content": "pytest and httpx",
        "author": "Aisha Bello",
        "published": True,
    },
    {
        "post_id": 7,
        "title": "Auth with JWT",
        "content": "Secure your endpoints",
        "author": "James Wilson",
        "published": True,
    },
    {
        "post_id": 8,
        "title": "Pydantic Models",
        "content": "Validate all the things",
        "author": "Sophia Martinez",
        "published": True,
    },
    {
        "post_id": 9,
        "title": "Background Tasks",
        "content": "Send emails async",
        "author": "Daniel Owusu",
        "published": False,
    },
    {
        "post_id": 10,
        "title": "WebSockets 101",
        "content": "Real-time features",
        "author": "Grace Taylor",
        "published": True,
    },
]


class PostCreate(BaseModel):
    post_id: int
    title: str
    content: str
    author: str
    published: bool = True


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


@app.get("/posts")
async def get_posts(skip: int = 0, limit: int = 10):
    return fake_posts_db[skip : skip + limit]


@app.get("/posts/search")
async def search_posts(
    q: Annotated[
        str | None,
        Query(min_length=3, max_length=30, description="Search posts by title"),
    ] = None,
    limit: Annotated[int, Query(ge=1, le=20, description="Cap the list of posts")] = 20,
):
    results = fake_posts_db

    if q:
        results = [post for post in fake_posts_db if q.lower() in post["title"].lower()]

    return results[:limit]


@app.get("/posts/filter")
async def filter_posts(
    author: Annotated[str | None, Query(min_length=3)] = None, published: bool = True
):
    results = fake_posts_db

    if author or published:
        results = [
            post
            for post in fake_posts_db
            if (author is None or author.lower() in post["author"].lower())
            and published == post["published"]
        ]

    return results


@app.get("/posts/{post_id}")
async def get_post(
    post_id: Annotated[int, Path(title="The ID of the post to retrieve", ge=1)],
):
    for post in fake_posts_db:
        if post["post_id"] == post_id:
            return post

    return {"error": "Post not found"}


@app.post("/posts")
async def create_post(post: PostCreate):
    return post.model_dump()


@app.get("/posts/{post_id}/rating")
async def post_rating(
    post_id: Annotated[int, Path(title="The ID of the post to rate", ge=1)],
    rating: Annotated[float, Query(gt=0, le=5)],
):
    for post in fake_posts_db:
        if post["post_id"] == post_id:
            post["rating"] = rating

            return {"post_id": post_id, "rating": rating}

    return {"error": "Post not found."}
