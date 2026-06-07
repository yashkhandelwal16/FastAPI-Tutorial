from fastapi import FastAPI, HTTPException, Header,Depends

app = FastAPI()

# Normal Usecase of Depends
#-----------------------------------------------------------------------------
def common_logic():
    return {
        "message":"Commom Logic Executed"
    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data
#-----------------------------------------------------------------------------


# Resuable Logic of using Depends
#----------------------------------------------------------------------------
def get_current_user():
    return {
        "user":"Yash"
    }

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return user
# ---------------------------------------------------------------------------


# Real Authentication Example [Important]
#----------------------------------------------------------------------------
def verify_token(token:str = Header(None)):
    if token != "secrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {
        "user":"Authorized User"
    }

@app.get("/secure_data")
def secure_data(user = Depends(verify_token)):
    return {
        "message":"Secure Data Accessed",
        "user":user
    }
# ---------------------------------------------------------------------------

