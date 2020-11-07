import board
import displayio
import adafruit_ssd1327
import busio
import time
import pers
import maze_data

display = pers.display
sense = pers.sensor

class storage():
  pass

app = storage()

app.tilt = [0, 0]

maze = maze_data.maze()

for i in range(60):
  app.tilt[0] += sense.rotation[0]
  app.tilt[1] += sense.rotation[1]
  maze.move(app.tilt)
  time.sleep(0.25)
