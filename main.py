from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Address(BaseModel):
    city:str
    pincode:int
    country:str

class userdetails(BaseModel):
    name:str
    age:int
    address:Address


@app.post("/createuser")
def createdata(data:userdetails):
    return {
        'message':'Data Created',
        'Data':data
    }