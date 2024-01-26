import requests
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

url = 'https://openapi-0119.onrender.com/pico_w/?count=7'
#自動reload頁面每10秒
st_autorefresh(interval=10000, limit=10000, key="fizzbuzzcounter")

r = requests.get(url=url)

if r.status_code == 200:
    print("下載成功")
    data = r.json()

dataFrame = pd.DataFrame(data)

st.header("學院養雞場")
st.divider()
st.caption("😍溫度-光線表表😍")
st.write(dataFrame)
st.divider()
st.caption("光線😍")
st.line_chart(dataFrame,x='date',y='light')
st.divider()
st.caption("溫度😍")
st.line_chart(dataFrame,x='date',y='temperature',color='#ff0000')