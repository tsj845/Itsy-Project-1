import board
import busio
import time
from displayio import release_displays

displayio.release_displays()# allows the i2c bus to be used

i2c = busio.I2C(board.SCL, board.SDA)# initializes the i2c bus

from adafruit_lsm6ds import LSM6DS33# imports the imu driver
sensor = LSM6DS33.LSM6DS(i2c)# initializes the imu