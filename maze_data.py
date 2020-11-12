import random
import math
from displayio import *
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect

sprites = Bitmap(32, 32, 2)
colors = Palette(2)
colors[0] = 0x000000
colors[1] = 0xFFFFFF

for i in range(16):# this generates the path tiles
    for i2 in range(16):
        sprites[i, i2] = 1
    
class Maze:
    def __init__(self, width, height, g):
        self.width = width
        self.height = height
        self.tiles = TileGrid(sprites, pixel_shader = colors, width=8, height=8, tile_width=16,tile_height=16, default_tile=1)
        self.marble = Circle(random.randint(0, 15)*8, random.randint(0, 15)*8, 8, fill=0xFFFFFF, outline=0x000000) #placed randomly, for now
        self.speed_x = 1 #Placeholder of 1, will represent pixels per second
        self.speed_y = 1
        g.append(self.tiles)
        g.append(self.marble)
    def move_marble(self, tilt):
        self.speed_x += 20*math.sin(tilt[0]*math.pi/180)
        self.speed_y += 20*math.sin(tilt[1]*math.pi/180)
        if self.direction != None:
            change_x = round(math.cos(self.direction*2*math.pi)*self.speed_x)
            change_y = round(math.cos(self.direction*2*math.pi)*self.speed_y)
            self.marble.x += change_x
            self.marble.y += change_y
            if self.marble.x > 110:
                self.marble.x = 110
                 self.speed_x = 0
            if self.marble.x < 0:
                self.marble.x = 0
                 self.speed_x = 0
            if self.marble.y > 110:
                self.marble.y = 110
                self.speed_y = 0
            if self.marble.y < 0:
                self.marble.y = 0
                self.speed_y = 0
            print(tilt[1])
