import random
import math
import displayio
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect

## we need five sprites (ball, verticle passage, horizontal passage, corner, and a solid wall)
# we only need one corner slot in the sheet because we can flip it (might change it later if it turns out to be too difficult)
sprites = Bitmap(32, 32, 2)
colors = Palette(2)
colors[0] = 0x000000
colors[1] = 0xFFFFFF

class Marble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = Circle(x, y, 8)
    def move(self, direction, step):
        if direction == 'up':
            self.sprite.y -= step
        elif direction == 'down':
            self.sprite.y += step
        elif direction == 'right':
            self.sprite.x += 1
        else:
            self.sprite.x -= 1

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.marble = Marble(random.randint(0, 15)*8, random.randint(0, 15)*8) #placed randomly, for now
        self.direction = None #Starts as none, will represent what angle marble will move at (0-1)
        self.speed = 0 #Starts as none, will represent pixels per second
    def move_marble(self, tilt):
        direc1 = 'up'
        direc2 = 'up'
        speed1 = 0
        speed2 = 0
        if abs(tilt[0]) > 0:
            if tilt[0] > 0:
                self.direction = 'right'
            else:
                self.direction = 'left'
            speed1 = int(str(rounded(tilt[0]+(1 * tilt[0]/abs(tilt[0])))).split('.')[0])
        if abs(tile[1]) > 0:
            if tit[1] > 0:
                direc2 = 'down'
            else:
                direc2 = 'up'
            speed2 = int(str(rounded(tilt[1]+(1 * tilt[1]/abs(tilt[1])))).split('.')[1])
        #change_x = math.sin(self.direction*2*math.pi)*self.speed
        #change_y = math.cos(self.direction*2*math.pi)*self.speed
        #self.marble.x += change_x
        #self.marble.y += change_y
        self.marble.move(direc1, speed1)
        self.marble.move(direc2, speed2)
