from tools import connect, reconnect
from machine import ADC, Pin, Timer
import time
import urequests

connect()
adc = ADC(4)
conversion_factor = 3.3/65535

def aboard_temp(temp):
    reading_v = adc.read_u16() * conversion_factor
    celsius = round(27 - (reading_v-0.706) / 0.001721, 2)
    url_str = f'https://https://openapi-0119.onrender.com/temperature/{celsius}'
    try:
        response = urequests.get(url_str)
    except:
        print("pico_ap出現問題")
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送訊息成功", celsius)
        else:
            print("傳送失敗(render服務出問題)")
        response.close()

tim10 = Timer()
tim10.init(period=10*1000, callback=aboard_temp)