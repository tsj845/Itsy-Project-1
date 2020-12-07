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

maze = maze_data.Maze(g)# creates the maze
t1 = time.monotonic()
maze.move_marble([0, 0])
tDif = time.monotonic() - t1

tDel = round(tDif, 2)+0.2

while True:
  if sense.gyro[0]*3>0.5 or sense.gyro[0]*3<-0.5:
    app.tilt[0] -= 3*sense.gyro[0]
  if sense.gyro[1]*3>0.5 or sense.gyro[1]*3<-0.5:
    app.tilt[1] += 3*sense.gyro[1]
  maze.move_marble(app.tilt)
  time.sleep(tDel)
