from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

details = []

class Userdata(BaseModel):
    id:int
    name:str
    age:int
    address:str
    password:int
    accountpassword:int

class Usershow(BaseModel):
    id:int
    name:str
    age:int
    address:str

@app.post("/users")
def user_create(user:Userdata):
    details.append(user)
    return {
        "message":"Data Created",
        "Data":user
    }

@app.get("/users", response_model=List[Usershow])
def getuser():
    return details

@app.get("/users/{user_id}", response_model=Usershow)
def get_user(user_id:int):
    for detail in details:
        if detail.id == user_id:
            return detail
    return {
        "error":"User not found"
    }
