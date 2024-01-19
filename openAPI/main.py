from typing import Union
import os
import redis
from fastapi import FastAPI

app = FastAPI()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

@app.get("/")
def read_root():
    counter = redis_conn.incrby("test123",1)
    return {"Counter": counter}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
#print(read_root())
#print('hello kitty')
