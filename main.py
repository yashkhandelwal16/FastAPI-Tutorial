from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return {
        'message':'You are at home now !'
    }

# Path Parameter means Dynamic Routes.

@app.get("/home/{user_id}")
def userid(user_id:int):                                   # This is Data Validation
    return {
        'message':user_id
    }