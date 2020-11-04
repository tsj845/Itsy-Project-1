import board
import displayio
import adafruit_ssd1327
import busio
import time

displayio.release_displays()

# This pinout works on a Metro and may need to be altered for other boards.
i2c_bus = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c_bus, device_address=0x3D)
time.sleep(1)
display = adafruit_ssd1327.SSD1327(display_bus, width=128, height=128)

m = displayio.Bitmap(128, 128, 2)
p = displayio.Palette(2)
p[0] = 0x000000
p[1] = 0xFFFFFF

for row in range(128):
    for col in range(128):
        m[row, col] = 1

tile_grid = displayio.TileGrid(m, pixel_shader=p)

g = displayio.Group()

g.append(tile_grid)

display.show(g)

time.sleep(10)