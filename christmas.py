# Christmas lights
from ws2812b_lib import WS2812b
from utime import sleep
from _thread import start_new_thread
from xmas_buzzer_lib import XMASSong

# WS2812b Setup
RED_COLOR = [5, 0, 0]
YELLOW_COLOR = [5, 5, 1]
GREEN_COLOR = [0, 10, 0]
WHITE_COLOR = [5, 5, 5]
OFF_COLOR = [0, 0, 0]

led_colors = [GREEN_COLOR, YELLOW_COLOR, RED_COLOR, WHITE_COLOR]
num_leds = 10
pixels = WS2812b(num_leds, 0,0)
pixels.set_range(0, num_leds-1, 0, 0, 0)
pixels.set_led(1, 5, 0 ,0)

xmasSong = XMASSong(15)

def walk(start, end, colorArr, delay = 0.2):
    red, green, blue = colorArr[0], colorArr[1], colorArr[2]
    for i in range(start, end): #The last should remain with the selected color
        pixels.set_led(i, red, green, blue)
        sleep(delay)
        pixels.set_led(i, 0, 0, 0)
    pixels.set_led(end, red, green, blue)
    
def loopSong():
    while True:
        xmasSong.play()
        sleep(0.2)
    
start_new_thread(loopSong, ()) 
    
while True:    
    for i in range(num_leds-1, -1, -1):
        walk(0, i, led_colors[(num_leds-1-i) % len(led_colors)])
        sleep(1)
    for i in range(num_leds-1, -1, -1):
        walk(0, i, OFF_COLOR)
