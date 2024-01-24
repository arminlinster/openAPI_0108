from machine import ADC , Pin
import utime

def getLightValue():
    adc_light = ADC(Pin(28))
    light_value = adc_light.read_u16()
    return light_value

while True:
    print(getLightValue())
