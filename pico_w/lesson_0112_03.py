from machine import Pin
import time
from machine import RTC
led25 = Pin("LED", Pin.OUT)
start = time.ticks_ms()
ledstatus = False
rtc = RTC()

while True:
    #time.sleep(1)
    #led25.value(1)
    #time.sleep(1)
    #led25.value(0)
    #time.sleep(1)
    
    delta = time.ticks_diff(time.ticks_ms(), start)
    #print(delta)
    if delta > 1000:
        start = time.ticks_ms()
        print("過一秒" , rtc.datetime())
        ledstatus = not ledstatus
        led25.value(ledstatus)
        