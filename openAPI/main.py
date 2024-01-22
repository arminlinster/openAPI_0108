from typing import Union
from from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv

celsius=27
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))
redis_conn.set('board:temp', celsius)

app = FastAPI()

@app.get("/")
def read_root():
    return {"pico_w": "temperture"}

@app.get("/counter/{c}")
def counter():
    counter = redis_conn.incr('temp:incrNum', 1)
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

@app.get("/temperature/{celsius}")
def pico_temp(celsius: float):
    celsius = redis_conn.set('board:temp', celsius)
    return {"temperature": celsius}

@app.get("/temperature")
def now_temp():
    celsius = redis_conn.get('board:temp')
    return {"溫度": celsius}