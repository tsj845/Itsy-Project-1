import board
from displayio import Group
import adafruit_ssd1327
import busio
import time
import pers
import maze_data
import maze_text
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.BLUE_LED)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.SWITCH)

switch.direction = Direction.INPUT
switch.pull = Pull.UP

sense = pers.sensor
g = Group()
pers.display.show(g)

class storeageC():
  pass

app = storeageC()

app.tilt = [0, 0]

app.inMenu = False

maze = maze_data.Maze(g)

maze.createPath('c00-8')

def logic():# does the work
  app.tilt[0] -= round(sense.gyro[0])*-2
  app.tilt[1] += round(sense.gyro[1])*-2
  maze.move_marble(app.tilt)
  if not switch.value:
    led.value = True
    app.tilt = [0, 0]
    time.sleep(0.25)
  else:
    led.value = False
    time.sleep(0.25)

def run(time=0):
  if time == 0:
    while True:
      logic()
  else:
    for i in range(time*4):
      logic()

def run2():
  for i in range(10000):
    if sense.gyro[0]*5>0.5 or sense.gyro[0]*5<-0.5:
      app.tilt[0] -= 5*sense.gyro[0]
    if sense.gyro[1]*5>0.5 or sense.gyro[1]*5<-0.5:
      app.tilt[1] += 5*sense.gyro[1]
    maze.move_marble(app.tilt)
    time.sleep(0.01)