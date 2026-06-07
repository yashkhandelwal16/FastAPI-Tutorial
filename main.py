from fastapi import FastAPI, status, HTTPException

app = FastAPI()


# Using the built in status_code, we have to write it during writing the url.
@app.post("/create", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message":"User Created"
    }

# Using the custom status.
@app.get("/user")
def get_user():
    return {
        "status":"Success",            # Even if the user don't know the mean of code , it will understand.
        "message":"User Fetched",
        "data":{
            "name":"Yash",
            "age" : 33
        }
    }

# Raise Custom Error using the HTTPException Built-in
@app.get("/users/{user_id}")
def get_users(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    return {
        "id":1,
        "name":"Yash",
        "age":29
    }


