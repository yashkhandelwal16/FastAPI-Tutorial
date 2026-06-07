from fastapi import FastAPI

app = FastAPI()

# Query Parameter is used to do searching, sorting and filtering .

# Simple Query Parameter 

@app.get("/users")                                  # Here /users give you an error
def users(user:str):                                # But /users?user=xyz is not give you an error
    return {
        'message':user
    }

# Optional Query Paramete

@app.get("/user_id")
def userID(userid:int=None):
    return {
        'message':userid
    }

# Default Values Query Paramete

@app.get("/user_detail")
def userdetail(age:int=10):
    return {
        'message':age
    }

# Multiple Query Paramete

@app.get("/user_details")
def userdetails(name:str=None,age:int=0):
    return {
        'message':'Userdetails',
        'name':name,
        'age':age
    }
