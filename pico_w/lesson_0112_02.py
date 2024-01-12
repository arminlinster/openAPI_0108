import machine
import time
from machine import Pin
led25 = Pin("LED", Pin.OUT)
i = 0;
while True:
    #i += 1
    #print(machine.freq() , "delay" , i)
    led25.value(1)
    time.sleep(1)
    led25.value(0)
    time.sleep(1)
