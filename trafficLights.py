from machine import Pin
from utime import sleep
import _thread

led_red = Pin(15, Pin.OUT)
led_yellow = Pin(14, Pin.OUT)
led_green = Pin(16, Pin.OUT)

button = Pin(13, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(11, Pin.OUT)

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        sleep(0.01)
        
_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:
        led_red.value(1)
        for i in range(10):
            buzzer.value(1)
            sleep(0.2)
            buzzer.value(0)
            sleep(0.2)
        global button_pressed
        button_pressed = False
    led_red.value(1)
    sleep(5)
    led_yellow.value(1)
    sleep(2)
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(1)
    sleep(5)
    led_green.value(0)
    led_yellow.value(1)
    sleep(5)
    led_yellow.value(0)