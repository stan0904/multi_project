from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time
from aiot_lcd1602 import LCD1602
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
from aiot_rgbled import RGBLed

aiot_lcd1602 = LCD1602()

aiot_dht20 = DHT20()

tiny_rgb = RGBLed(pin2.pin, 4)

if True:
  display.scroll('LCD')
  display.scroll('FAN')
  display.scroll('DHT20')
  display.scroll('ADC')
  display.scroll('RGB')

while True:
  pin0.write_analog(round(translate(100, 0, 100, 0, 1023)))
  time.sleep_ms(5000)
  pin0.write_analog(round(translate(0, 0, 100, 0, 1023)))
  time.sleep_ms(1000)
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('Temp:')
  aiot_lcd1602.move_to(10, 0)
  aiot_lcd1602.putstr('')
  aiot_lcd1602.move_to(10, 0)
  aiot_lcd1602.putstr((str(temperature()) + '*C'))
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr('Light:')
  aiot_lcd1602.move_to(10, 1)
  aiot_lcd1602.putstr('')
  aiot_lcd1602.move_to(10, 1)
  aiot_lcd1602.putstr((str(light_level()) + 'lx'))
  time.sleep_ms(3000)
  aiot_dht20.read_dht20()
  display.scroll((str(aiot_dht20.dht20_temperature()) + '*C'))
  display.scroll((str(aiot_dht20.dht20_humidity()) + '%'))
  time.sleep_ms(3000)
  display.scroll((pin1.read_analog()))
  display.scroll('-')
  display.scroll((translate((pin1.read_analog()), 0, 4095, 0, 100)))
  time.sleep_ms(2000)
  tiny_rgb.show(0, hex_to_rgb('#ff0000'))
  time.sleep_ms(1000)
  tiny_rgb.show(0, hex_to_rgb('#0000ff'))
  time.sleep_ms(1000)
  time.sleep_ms(10)
