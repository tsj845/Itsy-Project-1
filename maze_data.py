import random
import math
from displayio import *
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect

sprites = Bitmap(32, 32, 2)
colors = Palette(2)
colors[0] = 0x000000
colors[1] = 0xFFFFFF

class Marble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = Circle(x, y, 8, fill=0xFFFFFF)
    def move(self, direction, step):
        if direction == 'up' and self.sprite.y > 5:
            self.sprite.y -= step
        elif direction == 'down' and self.sprite.y < 100:
            self.sprite.y += step
        elif direction == 'right' and self.sprite.x < 100:
            self.sprite.x += step
        elif direction == 'left' and self.sprite.x > 5:
            self.sprite.x -= step

class Maze:
    def __init__(self, width, height, g):
        self.width = width
        self.height = height
        self.marble = Marble(10, 10)
        g.append(self.marble.sprite)
    def move(self, tilt):
        direc1 = 'up'
        direc2 = 'up'
        speed1 = 0
        speed2 = 0
        if abs(tilt[0]) > 0:
            if tilt[0] > 0:
                direc1 = 'right'
            else:
                direc1 = 'left'
            speed1 = round(tilt[0]+(1 * tilt[0]/abs(tilt[0])))
        if abs(tilt[1]) > 0:
            if tilt[1] > 0:
                direc2 = 'down'
            else:
                direc2 = 'up'
            speed2 = round(tilt[1]+(1 * tilt[1]/abs(tilt[1])))
        self.marble.move(direc1, speed1)
        self.marble.move(direc2, speed2)
