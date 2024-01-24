from machine import Pin
import time

p0 = Pin(15, mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False

while True:
    if btn.value():
        p0.on()
        is_press = True
        p0.on()
        #print('按鈕按下')
    else:
        if is_press == True:
            print('release')
            is_press = False
            p0.off()
    time.sleep_ms(10)
#p0.on()
#time.sleep(1)
#p0.off()
#print("LED current 電壓 :",p0.value())
#p2 = Pin(2. Pin.IN)
#print(p2.value())

#p4 = Pin(4, Pin.IN, Pin.PULL_UP)
#p5 = Pin(5, Pin.OUT, value=1)