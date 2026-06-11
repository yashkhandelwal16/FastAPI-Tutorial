from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Get all data 
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

# Get single post 
@app.get("/posts/{posts_id}")
def get_post(posts_id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{posts_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Page Not Found"
        )
    return response.json()
