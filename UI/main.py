import requests
import pandas as pd

url = 'https://openapi-0119.onrender.com/pico_w/?count=2'

r = requests.get(url=url)

if r.status_code == 200:
    print("下載成功")
    data = r.json()

dataFrame = pd.DataFrame(data)
print(dataFrame)