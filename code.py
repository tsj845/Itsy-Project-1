import board
from displayio import Group
import adafruit_ssd1327
import busio
import time
import pers
import maze_data

sense = pers.sensor
g = Group()
pers.display.show(g)

class storeageC():
  pass

app = storeageC()

app.tilt = [0, 0]

maze = maze_data.Maze(128, 128, g)

for i in range(10000):
  if sense.gyro[0]*5>0.5 or sense.gyro[0]*5<-0.5:
    app.tilt[0] -= 5*sense.gyro[0]
  if sense.gyro[1]*5>0.5 or sense.gyro[1]*5<-0.5:
    app.tilt[1] += 5*sense.gyro[1]
  maze.move_marble(app.tilt)
  time.sleep(0.01)
