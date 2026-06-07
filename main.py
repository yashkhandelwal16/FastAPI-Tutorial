from fastapi import FastAPI
from pydantic import BaseModel

# BaseModel class declaration

class userdetails(BaseModel):
    name:str
    age:int
    address:str


app = FastAPI()

# Post request is used send the data on server
# Except get request , all requests test on swagger ui

# Request body is responsible for handling the data at backend side 
# when frontend send the data to server using the post request and input method.


# JSON data handling But comes with no data validation so not recommended.

@app.post("/create")
def createdata(data:dict):
    return {
        'message':'Data Created',
        'Data':data
    }

# To overcome above problem and also manage the data in Json with data validation, use Pydantic model 

@app.post("/createuser")
def createdata(data:userdetails):
    return {
        'message':'Data Created',
        'Data':data
    }
