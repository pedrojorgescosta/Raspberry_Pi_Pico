from machine import Pin
from utime import sleep, ticks_ms, ticks_diff
from urandom import uniform

pressed = False
fastest_button = None
led = Pin(15, Pin.OUT)
left_button = Pin(13, Pin.IN, Pin.PULL_DOWN)
right_button = Pin(11, Pin.IN, Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        global fastest_button
        fastest_button = pin
        

led.value(1)
sleep(uniform(5,10))
led.value(0)

left_button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
right_button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
while fastest_button is None:
    sleep(0.01)

if fastest_button is left_button:
        print("Left player wins!")
elif fastest_button is right_button:
        print("Right player wins!")