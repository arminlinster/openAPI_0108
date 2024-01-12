from machine import Pin , Timer
def second5(t):
    print("over 5 seconds")
def second1(t):
    print("over 1 second")
    
tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=second5)

tim1 = Timer(period=1000, mode=Timer.PERIODIC, callback=second1)