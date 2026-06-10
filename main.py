from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Hello Yash !"
    }

@app.get("/add")
def add(a:int,b:int):
    return{
        "Result":a+b
    }

