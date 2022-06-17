from machine import ADC
from utime import sleep
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()
sensor_temp = ADC(4)

conversion_factor = 3.3 / 65535
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27- (reading - 0.706)/0.001721
    mylcd.lcd_display_string("Temp: " + str(round(temperature, 2)).replace('.',','))
    sleep(0.5)