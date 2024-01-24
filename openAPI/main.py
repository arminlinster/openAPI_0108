from  typing import Union
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

@app.get("/temperature/{celsius}")
def pico_temp(celsius: float):
    celsius = redis_conn.set('board:temp', celsius)
    return {"temperature": celsius}

@app.get("/temperature")
def now_temp():
    celsius = redis_conn.get('board:temp')
    return {"溫度": celsius}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/{date}/{celsius}")
async def get_item(date:str,celsius:float):
    print(f"日期:{date}")
    print(f"溫度:{celsius}")
    return{"date":date,"celsius":celsius}
fake_items_db = [{"item_name" : "foo"} , {"item_name" : "poo"} , {"item_name" : "Too"}]

#@app.get("/items/")
#async def read_item(skip: int = 0 , limit: int = 10):
#    return fake_items_db[ skip : skip + limit]

app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    print(f"光線:{light}")
    return {"狀態":"儲存成功1"}