from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed Origins(Frontend URL)
Origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = Origins,          # Allowed Front end
    allow_credentials = True,
    allow_method = ["*"],             # Get,Put,Post,Delete
    allow_headers = ["*"]
    )

# Get API 
@app.get("/")
def home():
    return {
        "message":"CORS ENABLE API"
    }

