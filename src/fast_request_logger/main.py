from fastapi import FastAPI, Request
from rich import print
from datetime import datetime
import json
import logging

# set the unvicorn logger level
logging.getLogger("uvicorn").setLevel(logging.WARN)
app = FastAPI(port=8000)

print("Send a request to http://127.0.0.1:8000 to see the request")

@app.get("/")
async def root_get():
    return {"message": "The app is running..."}



@app.post("/", status_code=201)
async def root_post(request: Request):
    body = await request.json()
    headers = dict(request.headers)
    print("Req Time:", datetime.now())
    print("Req Method:", "POST")
    print("Req Body: ", body)
    print("Req Headers: ", headers)

    return {"message": "POST request processed successfully."}


@app.put("/", status_code=201)
async def root_put(request: Request):
    body = await request.json()
    headers = dict(request.headers)
    print("Req Time:", datetime.now())
    print("Req Method:", "PUT")
    print("Req Body: ", body)
    print("Req Headers: ", headers)

    return {"message": "PUT request processed successfully."}
