from  typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
from pydantic import BaseModel

celsius=27
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))
redis_conn.set('board:temp', celsius)
redis_conn.set('temp:incrNum', celsius)

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

@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):
    #print(f"日期:{date}")
    redis_conn.rpush('pico_w:date',date)
    #print(f"位置:{address}")
    redis_conn.hset('pico_w:address',mapping={date:address})
    #print(f"攝氏:{celsius}")
    redis_conn.hset('pico_w:temperature',mapping={date:celsius})
    #print(f"光線:{light}")
    redis_conn.hset('pico_w:light',mapping={date:light})
    return {"狀態":"儲存成功2"}

app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):
    print(f"日期:{date}")
    print(f"位置:{address}")
    print(f"攝氏:{celsius}")
    print(f"光線:{light}")
    return {"狀態":"儲存成功1"}

class Pico_w(BaseModel):
    date:str
    address:str
    temperature:float
    light:float

@app.get("/pico_w/")
async def read_item(count:int=1):
    date_list = redis_conn.lrange('pico_w:date',-count,-1)
    dates = [date.decode() for date in date_list]
    all_Data:[Pico_w] = []
    for date in dates:
        address_get = redis_conn.hget('pico_w:address',date).decode()
        temperature_get = redis_conn.hget('pico_w:temperature',date).decode()
        light_get = redis_conn.hget('pico_w:light',date).decode()
        item = Pico_w(date=date,address=address_get,temperature=float(temperature_get),light=float(light_get))
        all_Data.append(item)

    
    return all_Data
