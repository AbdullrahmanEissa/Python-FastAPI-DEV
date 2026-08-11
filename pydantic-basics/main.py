from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

@app.get("/")
def greeting_message():
    return {"message": "Hello"}

@app.post("/posts")
def create_post(new_post: Post):
    return {"data": new_post}
