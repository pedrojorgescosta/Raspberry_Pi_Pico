from machine import Pin
import utime

def toggleLeds(leds):
    for led in leds:
            led.toggle()
            utime.sleep(0.5)

button = Pin(13, Pin.IN, Pin.PULL_DOWN)
ledPins = [15, 14, 16]
leds = []

for l in ledPins:
    led = Pin(l, Pin.OUT)
    led.value(0)
    leds.append(led)
    

while True:
    if button.value() == 1:
        toggleLeds(leds)
        utime.sleep(0.5)
        toggleLeds(leds)
        utime.sleep(1)
        toggleLeds(leds)
        utime.sleep(0.5)
        toggleLeds(reversed(leds))

