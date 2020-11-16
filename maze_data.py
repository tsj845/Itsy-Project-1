import random
from math import sin, cos, pi
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
        #self.speed_x = 1 #Placeholder of 1, will represent pixels per second
        #self.speed_y = 1
        g.append(self.tiles)
        g.append(self.marble)
    def checkBounds(self, x, y):# will check if the marble collides with a wall
        """
        PLAN FOR HOW THE FUNCTION WILL FUNCTION:
        
        will find all tiles the marble overlaps, if any are filled in black then the marble is out
        of bounds, otherwise the move is legal
        
        BENEFITS TO THIS METHOD:
        
        possibly much faster
        will probably not be as hard to read the code
        
        PART THAT I HAVE WORKED OUT:
        
        1. loop over all tiles and use a function that checks for overlap (this could be optimised to
        only check tiles near to the marble)
        
        2. then if an overlap is found check the fill of the overlapping tile
        3. if the fill is black then return False
        4. once all overlaps are checked, none of the overlapping tiles are black then return True
        """
        return True# placeholder
        for index in range(getRange()):
            pass
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
