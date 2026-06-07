from fastapi import FastAPI

app = FastAPI()

@app.get("/")                                                    
def home():
    return {'message' : "This is home route"}


@app.get("/users")                                               
def home():
    return {'message' : "This is users route"}

@app.get("/api/fetch")                                           
def home():
    return {'message' : "Here /api/fetch is an API Endpoints whereas /fetch is route"}

