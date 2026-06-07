from fastapi import FastAPI

app = FastAPI()

@app.get("/")                                                    # API
def home():
    return {'message' : "This is home route"}


@app.get("/users")                                               #API
def home():
    return {'message' : "This is users route"}

@app.get("/api/fetch")                                           #API
def home():
    return {'message' : "Here /api/fetch is an API Endpoints whereas /fetch is route"}

