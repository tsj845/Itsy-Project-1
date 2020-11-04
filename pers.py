import board
import displayio
import adafruit_ssd1327
import busio
import time

displayio.release_displays()

i2c_bus = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c_bus, device_address=0x3D)
time.sleep(1)
display = adafruit_ssd1327.SSD1327(display_bus, width=128, height=128)
