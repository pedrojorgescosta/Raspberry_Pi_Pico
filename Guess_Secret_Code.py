from machine import ADC, Pin
from utime import sleep, ticks_ms, ticks_diff
from urandom import randint
import I2C_LCD_driver
import _thread
import time
from ws2812b_lib import WS2812b


# Set up variables
CODE_LENGTH = 4
currentCode = 0
currentDigit = 0
correctDigit = randint(0,9)
conversion_factor = 9 / 65535
str1 = "Codigo: "
str2 = "Numero: "
lastHandler = 0


# WS2812b Setup
RED_COLOR = [5, 0, 0]
YELLOW_COLOR = [5, 5, 1]
GREEN_COLOR = [0, 10, 0]
WHITE_COLOR = [5, 5, 5]

led_colors = [WHITE_COLOR,
                GREEN_COLOR, GREEN_COLOR, GREEN_COLOR, 
                YELLOW_COLOR, YELLOW_COLOR, YELLOW_COLOR,
                RED_COLOR, RED_COLOR, RED_COLOR]
num_leds = 10
pixels = WS2812b(num_leds, 0,2)
pixels.set_range(0, num_leds-1, 0, 0, 0)

# Set up Components
selector = ADC(26)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(17, Pin.OUT)
lcd = I2C_LCD_driver.lcd()
lcd.lcd_display_string(str1, 1)
lcd.lcd_display_string(str2, 2)


def setProximity(difference):
    difference
    for i in range(num_leds):
        if i < difference:
           pixels.set_led_full(i, 0, 0, 0) #Turn off the leds         
        else:
           pixels.set_led_full(i, led_colors[i][0], led_colors[i][1], led_colors[i][2]) # Turn on leds   
        

def pressed(pin):
    global currentCode, correctDigit, lastHandler    
    if ticks_diff(ticks_ms(), lastHandler) < 100:
        print('double tap')
        return    
    if len(str(currentCode)) >= CODE_LENGTH or currentDigit != correctDigit:
        buzzer.value(1)
        sleep(0.1)
        buzzer.value(0)
    else:
        currentCode *= 10
        currentCode += currentDigit
        correctDigit = randint(0,9)
    lcd.lcd_display_string("{:0<4}".format(str(currentCode)), 1, len(str1))
    lastHandler = ticks_ms()

button.irq(trigger=Pin.IRQ_RISING, handler=pressed)

timer_start = ticks_ms()
lcd.lcd_display_string("{:0<4}".format(str(currentCode)), 1, len(str1))

while len(str(currentCode)) < CODE_LENGTH:
    currentDigit = int(round(selector.read_u16() * conversion_factor, 0 ))
    lcd.lcd_display_string(str(currentDigit), 2, len(str2))
    setProximity(abs(currentDigit - correctDigit))
    sleep(0.2)

lcd.lcd_display_string("{:0<4}".format(str(currentCode)), 1, len(str1))    
lcd.lcd_display_string("Tempo: " + str((ticks_diff(ticks_ms(), timer_start))/1000) + "s", 2)

while True:
    pixels.set_range(0, num_leds-1, 0, 1, 0)
    sleep(0.5)
    pixels.set_range(0, num_leds-1, 0, 0, 1)
    sleep(0.5)
    pixels.set_range(0, num_leds-1, 1, 0, 0)
    sleep(0.5)
    pixels.set_range(0, num_leds-1, 1, 1, 1)
    sleep(0.5)
