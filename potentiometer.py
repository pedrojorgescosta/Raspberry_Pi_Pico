from machine import ADC, Pin, PWM
from utime import sleep

potentiometer = ADC(26)
led = PWM(Pin(15))
led.freq(1000) # Sets frequency to 1 hertz

conversion_factor = 3.3 / 65535
while True:
    voltage = potentiometer.read_u16() * conversion_factor
    print(voltage)
    #sleep(0.5)
    led.duty_u16(potentiometer.read_u16()) # Controls the pin output, the percentage of 'On's during the frequency