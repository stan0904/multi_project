YoLo SmartHome Project

The YoLo SmartHome Project is a multi-functional smart home prototype using Yolo:Bit. It integrates environmental sensors, display modules, analog and digital controls, and RGB lighting to demonstrate real-time home automation features.

🔹 Features
Temperature & Humidity Monitoring: Uses DHT20 to track environmental conditions.
LCD Display: Shows real-time temperature and light level.
Analog Control: Demonstrates control over devices like fans via analog output.
RGB LED Lighting: Visual feedback with dynamic colors.
Continuous Data Logging: Monitors sensors and outputs continuously.
🔹 Hardware Requirements
Yolo:Bit microcontroller
DHT20 temperature & humidity sensor (I2C)
LCD1602 display (I2C)
RGB LED (connected to pin 2)
Analog sensors (e.g., light sensor, potentiometer) connected to pin 0 and pin 1
🔹 Software Requirements
MicroPython firmware compatible with Yolo:Bit
Python libraries:
from yolobit import *
from aiot_lcd1602 import LCD1602
from aiot_dht20 import DHT20
from aiot_rgbled import RGBLed
from machine import Pin, SoftI2C
import time
🔹 Installation
Flash the Yolo:Bit board with MicroPython.
Connect hardware according to the Hardware Requirements.
Upload multi_project.py to the board.
Run the script to start the smart home system.
🔹 Usage
The Yolo:Bit display scrolls messages:
LCD → FAN → DHT20 → ADC → RGB
LCD1602 shows Temperature and Light level in real-time.
DHT20 sensor data is displayed in Celsius and percentage humidity.
RGB LED cycles between red and blue for visual feedback.
Analog output controls devices like fans via pin0.write_analog().
🔹 Example Output
LCD: Temp: 25°C Light: 120lx
DHT20: 25°C 60%
Analog Input: 50%
RGB LED: Red → Blue
🔹 Notes
Adjust pin numbers and I2C addresses according to your hardware setup.
The program loops indefinitely until the device is powered off.
🔹 License

This project is open-source and free for educational and prototyping purposes.
