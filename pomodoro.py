from machine import Pin, Timer

ledPins = [11,12,13,14,15]
status = [False for _ in ledPins]
button = Pin(16, Pin.IN, Pin.PULL_DOWN)
sensor_pir = Pin(28, Pin.IN, Pin.PULL_DOWN)
RunningLed = Pin(25, Pin.OUT)
tim = Timer()
isRunning = False

leds = [Pin(i, Pin.OUT) for i in ledPins]

def tick(timer):
    incNext = False
    global leds
    for i in range(len(status)):
        if not status[i]:
            leds[i].value(1)
            status[i] = True
            break
        else:
            leds[i].value(0)
            status[i] = False

def start(pin):
    global tim, isRunning, RunningLed
    RunningLed.toggle()
    if isRunning:
        tim.deinit()
        isRunning = False
        reset()
    else:
        isRunning = True
        global status
        status = [False for _ in ledPins]
        tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)

def reset():
    status = [False for _ in ledPins]
    RunningLed.value(0)
    for led in leds:
        led.value(0)

reset()
button.irq(trigger=Pin.IRQ_RISING, handler=start)
sensor_pir.irq(trigger=Pin.IRQ_RISING, handler=start)
