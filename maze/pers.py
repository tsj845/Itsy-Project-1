import board
import displayio
import adafruit_ssd1327
import busio
import time

i2c = busio.I2C(board.SCL, board.SDA)

i2c.try_lock()

### these can be un-commented after Tristan is able to attach the IMU to the itsy ###
######################################
from adafruit_lsm6ds import LSM6DS33#
sensor = LSM6DS33.LSM6DS(i2c)###############
######################################
### do not un-comment the above lines ###

displayio.release_displays()

display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
time.sleep(1)
display = adafruit_ssd1327.SSD1327(display_bus, width=128, height=128)

g = Group()

display.show(g)