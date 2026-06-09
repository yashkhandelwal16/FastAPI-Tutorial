import time
import asyncio
from fastapi import FastAPI

app = FastAPI()


# Normal function 
def task():
    time.sleep(3)
    return "Done"

# async-await function
async def task():
    await asyncio.sleep(3)
    return "Done"

# asyncio use in route
@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message":"Async API"
    }
