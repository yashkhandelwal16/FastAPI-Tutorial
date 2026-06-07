from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

details = []

class Users(BaseModel):
    id:int
    name:str
    age:int

# Create Route

@app.post("/users")
def create_user(user:Users):
    details.append(user)
    return {
        "message":"Data Created",
        "Data":user
    }

# Update the Data using Query Parameter

@app.put("/users/{user_id}")
def update_user(user_id:int,updated_data:Users,notify:bool=False):             # Here you can see that, Pathparam, Queryparam and Requestbody are used together
    for index,detail in enumerate(details):
        if detail.id == user_id:
            details[index] = updated_data
            return {
                "message":"Data Updated",
                "notify":notify,
                "Data":updated_data
            }
    return {
        "error":"User not found"
    }