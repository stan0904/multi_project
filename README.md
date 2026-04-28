Multi-Function Microcontroller Project
Overview

This project demonstrates a multi-functional microcontroller setup using the Yolo:Bit platform. It integrates various sensors and peripherals, including:

LCD1602 display
DHT20 temperature and humidity sensor
RGB LED
Analog input (light sensor, potentiometer)
Built-in fans and other actuators

The project continuously reads sensor data, displays it, and demonstrates control of output devices like LEDs and fans.

Features
LCD Display: Shows temperature and light level readings in real-time.
DHT20 Sensor: Reads temperature and humidity and scrolls it on the Yolo:Bit display.
Analog I/O: Demonstrates analog write and read operations (e.g., controlling fan speed).
RGB LED Control: Changes LED colors between red and blue as a visual indicator.
Data Logging: Continuously prints sensor values to the microcontroller display for monitoring.
Hardware Setup
Yolo:Bit microcontroller
DHT20 sensor connected via I2C
LCD1602 display connected via I2C
RGB LED connected to pin 2
Analog sensors connected to pin 0 and pin 1
Installation
Flash the Yolo:Bit firmware compatible with MicroPython.

Install required libraries:

from yolobit import *
from aiot_lcd1602 import LCD1602
from aiot_dht20 import DHT20
from aiot_rgbled import RGBLed
from machine import Pin, SoftI2C
import time
Upload multi_project.py to the microcontroller.
Usage
Power on the Yolo:Bit board.
The LCD will scroll messages: LCD, FAN, DHT20, ADC, RGB.
Sensor readings will update continuously on the LCD and the microcontroller display.
The RGB LED will alternate between red and blue every second.
Fan speed and analog outputs are demonstrated using pin0.write_analog() commands.
Notes
Ensure proper I2C connections for the LCD and DHT20 sensor.
Adjust pin numbers and I2C addresses in the code according to your hardware setup.
The program runs indefinitely in a loop, updating all connected peripherals.
License

This project is open-source and free to use for educational and prototyping purposes.
