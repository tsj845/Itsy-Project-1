import board
import displayio
import adafruit_ssd1327
import busio
import time

displayio.release_displays()# allows the i2c bus to be used

i2c = busio.I2C(board.SCL, board.SDA)# initializes the i2c bus

from adafruit_lsm6ds import LSM6DS33# imports the imu driver
sensor = LSM6DS33.LSM6DS33(i2c)# initializes the imu

display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)# creates the display bus
time.sleep(1)# this is an artifact of the example code on GitHub, i have not removed it because i don't know what its purpose is
display = adafruit_ssd1327.SSD1327(display_bus, width=128, height=128)# initializes the display
