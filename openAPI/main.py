from typing import Union
import redis
from fastapi import FastAPI

app = FastAPI()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

@app.get("/")
def read_root():
    redis_conn.incrby("test123",2)
    return {"Hello": "ArminLin"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
#print(read_root())
#print('hello kitty')
