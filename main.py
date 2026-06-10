from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Ensuring uploads folder exists
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Static files setup
app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

# Upload file api 
@app.post("/upload")
def upload_file(file:UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR,filename)
    if not filename:
        raise HTTPException(
            status_code=400,
            detail="File not Selected"
        )
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        return {
            "message":"File Uploaded Successfully",
            "Filename":filename,
            "File_URL":f"http://127.0.0.1:8000/files/{filename}"
        }
    
# Get file url api 
@app.get("/files/{filename}")
def get_file(filename:str):
    file_path = os.path.join(UPLOAD_DIR,filename)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File Not Found"
        )
    return{
        "File_URL":f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return {
        "message":"File Uploaded API Running !"
    }





