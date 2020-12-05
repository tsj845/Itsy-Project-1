import board
from displayio import Group
import adafruit_ssd1327
import busio
import time
import pers
import maze_data
import maze_text

sense = pers.sensor# gets a reference to the sensor
g = Group()# creates a group to be displayed
pers.display.show(g)# displays the group

class storeageC():# helps to prevent unbound local errors
  pass

app = storeageC()# creating an instance of the storage class

app.tilt = [0, 0]# stores the tilt on the x and y axes

#maze = maze_data.Maze(128, 128, g)# creates the maze



#for i in range(60):
  #app.tilt[0] -= sense.gyro[0]
  #app.tilt[1] += sense.gyro[1]
  #maze.move(app.tilt)
  #time.sleep(0.25)
