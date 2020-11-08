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
        if direction == 'updown':
            self.sprite.y += step
            self.y += step
        elif direction == 'leftright':
            self.sprite.x += step
            self.x += step
            
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.marble = Marble(random.randint(0, 15)*8, random.randint(0, 15)*8) #placed randomly, for now
        self.direction = None #Starts as none, will represent what angle marble will move at (0-1)
        self.speed = 1 #Placeholder of 1, will represent pixels per second
    def move_marble(self):
        if self.direction != None:
            change_x = round(math.sin(self.direction*2*math.pi)*self.speed)
            change_y = round(math.cos(self.direction*2*math.pi)*self.speed)
            self.marble.move("leftright", change_x)
            self.marble.move("updown", change_y)
