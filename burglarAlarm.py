from machine import Pin
from utime import sleep

sensor_pir = Pin(28, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)
buzzer = Pin(14, Pin.OUT)

def pir_handler(pin):
    sleep(0.1)
    if pin.value():
        print("Alarm!!!")
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            sleep(0.1)

sensor_pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()
    sleep(5)