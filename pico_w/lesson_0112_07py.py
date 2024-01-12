from machine import Pin , Timer
led25 = Pin("LED",Pin.OUT)

def second1(t):
    print("over 1 second")
    led25.toggle()
    


tim1 = Timer(period=1000, mode=Timer.PERIODIC, callback=second1)