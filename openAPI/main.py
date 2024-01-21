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
    
# 接收pico_w傳來的資料(溫度、時間)
@app.get("/temperature/{celsius}/{time}")
def save_temperature(celsius:float, time:str):
    redis_conn.set('board:temperature', celsius)
    redis_conn.set('board:time', time)
    return 'Save successfully'

# 顯示溫度頁
@app.get("/temperature")
def read_temperature():
    celsius = redis_conn.get('board:temperature')
    time = redis_conn.get('board:time')
    return {"溫度": celsius, "時間": time}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

