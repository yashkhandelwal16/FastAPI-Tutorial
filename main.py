from fastapi import FastAPI,HTTPException,Depends
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
import bcrypt

app = FastAPI()

#JWT Config
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES= 30

#Password Hashing Setup (Using bcrypt directly)
def hash_password(password: str) -> str:
    pw_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw_bytes, salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    pw_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(pw_bytes, hashed_bytes)

#OauthSetup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy user DB
fake_user_db = {
    "admin":{
        "username":"admin",
        "hashed_password":hash_password("1234")
    }
}

#Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return token

#Login API(OAuth2 Form)
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )
    access_token = create_token({"sub":form_data.username})

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }

#Token Varify
def verify_token(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
#Protected Route
@app.get("/protected")
def protected_route(username: str = Depends(verify_token)):
    return {
        "message":"Hello you have access to this protected route!",
        "user":username
    }