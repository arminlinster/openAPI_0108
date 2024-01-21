import redis
import os
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

@app.get("/")
def read_root():
    counter = redis_conn.incr("test123",1)
    return {"Counter": counter}

@app.get("/counter/{c}")
def counter(c:int):
    counter = redis_conn.incr('test123',c)
    return {"Counter": counter}
@app.get("/temperature/{d}")
def temperature(d:float):
    counter = redis_conn.incr('test123',c)
    return {"d": d}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

