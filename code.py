import board
from displayio import Group
import adafruit_ssd1327
import busio
import time
import pers
import maze_data

sense = pers.sensor# gets a reference to the sensor
g = Group()# creates a group to be displayed
pers.display.show(g)# displays the group

class storeageC():# helps to prevent unbound local errors
  pass

app = storeageC()# creating an instance of the storage class

app.tilt = [0, 0]# stores the tilt on the x and y axes

maze = maze_data.Maze(128, 128, g)# creates the maze

while True:
  if 5*sense.gyro[0] > 0.5:
    app.tilt[0] -= 5*sense.gyro[0]
  if 5*sense.gyro[0] > 0.5:
    app.tilt[1] += 5*sense.gyro[1]
  maze.move_marble(app.tilt)
  time.sleep(0.01)
