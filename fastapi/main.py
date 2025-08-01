from fastapi import FastAPI
from typing import Optional
# import uvicorn


app = FastAPI()

@app.get("/")
def index():
    return {"data": "list of the blogs"}

@app.get("/blog/unpublished")
def unpublished():
    # fetch all unpublished from the database
    
    return {"data":"all unpublished"}

@app.get("/blog/")
def show(limit:int, published:bool=True, sort:Optional[str]=None):
    # fetch the blog from the database
    return {"data":[limit, published, sort]}

@app.get("/blog/{id}/comments")
def get_comments(id:int, limit:int=10):
    # fetch the comments from the database
    return {"data":[id, limit]}


from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post("/blog")
def create_blog(blog:Blog):
    # creates a blog
    return {"data":f"blog is created with title as \n {blog}"}
