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

#l = maze_text.Label(maze_text.font, x=64, y=64, color=0xFFFFFF, text="hello, world!", max_glyphs=1000)

#l.anchor_point = (0.5, 0.5)

#l.anchored_position = (64, 64)

class storeageC():# helps to prevent unbound local errors
  pass

app = storeageC()# creating an instance of the storage class

app.tilt = [0, 0]# stores the tilt on the x and y axes

#g.append(l)

def test():
  print('test')

def test2():
  print('text')

bc = maze_text.menu(g, 8, 0, 16)

bc.addButton(text='print "test"', func=test)
bc.addButton(text='print "text"', func=test2)

#while True:
#  pass

#maze = maze_data.Maze(128, 128, g)# creates the maze



#for i in range(60):
  #app.tilt[0] -= sense.gyro[0]
  #app.tilt[1] += sense.gyro[1]
  #maze.move(app.tilt)
  #time.sleep(0.25)
