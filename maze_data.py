import random
from math import sin, cos, pi
from displayio import *
from adafruit_display_shapes.circle import Circle
#from adafruit_display_shapes.rect import Rect## we aren't using it right now so no need to import it

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
        self.tiles = TileGrid(sprites, pixel_shader = colors, width=8, height=8, tile_width=16,
                              tile_height=16, default_tile=1)
        self.marble = Circle(8, 8, 8, fill=0xFFFFFF,
                             outline=0x000000) #placed at (0, 0)
        #self.speed_x = 1 #Placeholder of 1, will represent pixels per second
        #self.speed_y = 1
        g.append(self.tiles)
        g.append(self.marble)
        self.paths = []
    def generateMaze(self, nPaths=5):
        pass
    def createPath(self, string):
        pass
    def checkBounds(self, x, y):
        for path in self.paths:
            if path[0] == 'c':
                if y == int(path[1])*16:
                    if x >= int(path[2])*16 and x < int(path[4])*16:
                        return True
            else:
                if x == int(path[1])*16:
                    if y >= int(path[2])*16 and y < int(path[4])*16:
                        return True
        return False
    def move_marble(self, tilt):
        """
        direction value mapping:
        0.0 : no x control, inverted y control
        0.125 : inverted x & y controls
        0.25 : inverted x control, no y control
        0.375 : inverted x control, normal y control
        0.5 : no x control, normal y control
        0.657 : normal x & y controls
        0.8 : normal x control, inverted y control
        0.925 : normal x control, inverted y control
        we can use these to change the controls and make things harder if we want
        
        i think this could be the way to go if you have any disagreements let me know
        """
        direction = 0.675# interesting thing is that if this changed the controls change
        nx = self.marble.x + round(sin(direction*2*pi)*(tilt[0]/4))
        ny = self.marble.y + round(cos(direction*2*pi)*(tilt[1]/4))
        if ny > -1 and ny < 113:
            if checkBounds(self.marble.x, y):
                self.marble.y = ny
        if nx > -1 and nx < 113:
            if checkBouds(x, self.marble.y):
                self.marble.x = nx
        #self.speed_x += 10*math.sin(tilt[0]*math.pi/180)
        #self.speed_y += 10*math.sin(tilt[1]*math.pi/180)
        #if self.direction != None:
            #change_x = round(math.cos(self.direction*2*math.pi)*self.speed_x)
            #change_y = round(math.cos(self.direction*2*math.pi)*self.speed_y)
            #check if it is at wall
            #if self.marble.x + change_x > 110:
            #    self.marble.x = 110
            #    self.speed_x = 0
            #elif self.marble.x + change_x < 0:
            #    self.marble.x = 0
            #    self.speed_x = 0
            #else:
            #    self.marble.x += change_x
            #if self.marble.y + change_y> 110:
            #    self.marble.y = 110
            #    self.speed_y = 0
            #elif self.marble.y + change_y< 0:
            #    self.marble.y = 0
            #    self.speed_y = 0
            #else:
            #     self.marble.y += change_y
