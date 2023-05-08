import logging
from datetime import datetime

from fastapi import FastAPI, Request
from rich import print

# set the unvicorn logger level
logging.getLogger("uvicorn").setLevel(logging.WARN)
app = FastAPI(port=8000)

print("Send a request to http://127.0.0.1:8000 to see the request")


@app.get("/", status_code=200)
async def root_get(request: Request):
    return await log_request(request, "GET")


@app.put("/", status_code=201)
async def root_put(request: Request):
    return await log_request(request, "PUT")


@app.post("/", status_code=201)
async def root_post(request: Request):
    return await log_request(request, "POST")


@app.delete("/", status_code=204)
async def root_delete(request: Request):
    return await log_request(request, "DELETE")


@app.patch("/", status_code=201)
async def root_patch(request: Request):
    return await log_request(request, "PATCH")


async def log_request(request: Request, method: str):
    body = await request.json()
    headers = dict(request.headers)

    log_item = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "method": method,
        "body": body,
        "headers": headers,
    }

    print(log_item)

    return {"message": f"{method} request successful."}
