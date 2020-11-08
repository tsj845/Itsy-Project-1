import board
import displayio
import adafruit_ssd1327
import busio
import time
import pers
import maze_data

display = pers.display
sense = pers.sensor
g = pers.g

class storeageC():
  pass

app = storeageC()

app.tilt = [0, 0]

maze = maze_data.Maze(128, 128, g)

for i in range(60):
  app.tilt[0] += sense.gyro[0]
  app.tilt[1] += sense.gyro[1]
  maze.move(app.tilt)
  time.sleep(0.25)
