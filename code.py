import board
from displayio import Group
import adafruit_ssd1327
import busio
from time import sleep
import pers
import maze_data
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.BLUE_LED)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.SWITCH)

switch.direction = Direction.INPUT
switch.pull = Pull.UP

sense = pers.sensor# gets a reference to the sensor
g = Group()# creates a group to be displayed
pers.display.show(g)# displays the group

class storeageC():# helps to prevent unbound local errors
  pass

app = storeageC()# creating an instance of the storage class

app.tilt = [0, 0]# stores the tilt on the x and y axes

maze = maze_data.Maze(128, 128, g)# creates the maze

def logic():# does the work
  app.tilt[0] -= round(sense.gyro[0]*2)
  app.tilt[1] += round(sense.gyro[1]*2)
  maze.move(app.tilt)
  if not switch.value:
    led.value = True
    app.tilt = [0, 0]
    sleep(0.25)
    led.value = False
  else:
    sleep(0.25)

def run(time=0):# this ensures that if you want unlimited testing time you must be connected via serial port
  if time == 0:#    this ensures that the tester can do a keyboard interrupt at any time
    while True:
      logic()
  else:
    for i in range(time*4):
      logic()

#for i in range(60):
  #app.tilt[0] -= sense.gyro[0]
  #app.tilt[1] += sense.gyro[1]
  #maze.move(app.tilt)
  #time.sleep(0.25)
