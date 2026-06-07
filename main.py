from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Below two paragraph of code are the standard code of any Global error handling.
#--------------------------------------------------------------------------------------------------------------------------------------
class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def usernotfoundhandler(request:Request, exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )
#--------------------------------------------------------------------------------------------------------------------------------------

# As you know it is using HTTPException
@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    return {
        "id":1,
        "name":"Yash"
    }

# Usecase of the Global Error Handling here
@app.get("/user/{name}")
def get_user(name:str):
    if name != "Yash":
        raise UserNotFoundException("Yash")
    return{
        "name":name
    }