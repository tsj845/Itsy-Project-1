from random import seed, randrange
import math
from displayio import *
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect

sprites = Bitmap(32, 32, 2)
colors = Palette(2)
colors[0] = 0x000000
colors[1] = 0xFFFFFF

for i in range(16):
    for i2 in range(16):
        sprites[i, i2] = 1

def distance(x1, y1, x2, y2):
    return round(sqrt(pow((x2 - x1),2) + pow((y2 - y1),2)))

class Marble:
    def __init__(self, x, y, parent):
        self.parent = parent
        self.sprite = Circle(x, y, 8, fill=0xFFFFFF, outline=0x000000)
    def oOB(self, x, y):
        for path in self.parent.paths:
            if path[0] == 'c':
                if y == int(path[1])*16:
                    if x >= int(path[2])*16 and x < int(path[4])*16:
                        return True
            else:
                if x == int(path[1])*16:
                    if y >= int(path[2])*16 and y < int(path[4])*16:
                        return True
        return False
    def move(self, direction, step):
        x = self.sprite.x
        y = self.sprite.y
        if direction == 'up' and self.sprite.y > 8:
            y -= step
        elif direction == 'down' and self.sprite.y < 120:
            y += step
        elif direction == 'right' and self.sprite.x < 120:
            x += step
        elif direction == 'left' and self.sprite.x > 8:
            x -= step
        if self.oOB(x, y):
            self.sprite.x = x
            self.sprite.y = y

class Maze:
    def __init__(self, width, height, g):
        self.width = width
        self.height = height
        self.tiles = TileGrid(sprites, pixel_shader = colors, width=8, height=8, tile_width=16, tile_height=16, default_tile=1)
        self.marble = Marble(8, 8, self)
        g.append(self.tiles)
        g.append(self.marble.sprite)
        self.paths = []
        self.goal = (7, 7)
    def checkWin(self):
        win = False
        if distance(self.marblePos[0], self.marblePos[1], self.goal[0], self.goal[1]) < 16:
            win = True
        print(win)
    def generateMaze(self):
        pass
    def clearPaths(self):
        self.paths.clear()
        for i in range(64):
            self.tiles[i] = 1
    def createPath(self, string):
        self.paths.append(string)
        if string[0] == 'c':
            for i in range(int(string[2]), int(string[4])):
                self.tiles[i+int(string[1])*8] = 0
        else:
            for i in range(int(string[2]), int(string[4])):
                self.tiles[i*8+int(string[1])] = 0
    def move(self, tilt):
        direc1 = 'up'
        direc2 = 'up'
        speed1 = 0
        speed2 = 0
        if abs(tilt[0]) > 3:
            if tilt[0] > 0:
                direc1 = 'right'
            else:
                direc1 = 'left'
            speed1 = abs(round(tilt[0]))
        if abs(tilt[1]) > 3:
            if tilt[1] > 0:
                direc2 = 'down'
            else:
                direc2 = 'up'
            speed2 = abs(round(tilt[1]))
        self.marble.move(direc1, speed1)
        self.marble.move(direc2, speed2)
