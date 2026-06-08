from fastapi import FastAPI, Request
import time

app = FastAPI()

# Common Middleware code
@app.middleware("http")
async def middle_ware(requests:Request,call_next):
    print("Request Recieved")
    response = await call_next(requests)
    print("Response Sent")
    return response

# Real world example of Logging middleware
@app.middleware("http")
async def logging_middleware(requests:Request,call_next):
    Start_time = time.time()
    response = await call_next(requests)
    process_time = time.time()-Start_time
    print(f"Path:{requests.url.path}  |  Time:{process_time}")
    return response