import random
from math import sin, cos, pi
from time import sleep
from displayio import *
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_text.label import Label
import terminalio

font = terminalio.FONT

sprites = Bitmap(32, 32, 2)
colors = Palette(2)
colors[0] = 0x000000
colors[1] = 0xFFFFFF

for i in range(16):# this generates the path tiles
    for i2 in range(16):
        sprites[i, i2] = 1

class Maze:
    def __init__(self, g):
        self.tiles = TileGrid(sprites, pixel_shader = colors, width=8, height=8, tile_width=16,
                              tile_height=16, default_tile=1)
        self.marble = Circle(8, 8, 8, fill=0xFFFFFF,
                             outline=0x000000) #placed at (0, 0)
        #self.speed_x = 1 #Placeholder of 1, will represent pixels per second
        #self.speed_y = 1
        self.goal = (7, 7)
        self.threshold = 2
        self.hole = Circle(self.goal[0]*16+8, self.goal[1]*16+8, 8, fill=0x777777, outline=0xDDDDDD)
        self.mGroup = Group()
        self.mazeSub = Group()
        self.lossSub = Group()
        self.mazeSub.append(self.tiles)
        self.mazeSub.append(self.hole)
        self.mazeSub.append(self.marble)
        self.mGroup.append(self.mazeSub)
        self.mGroup.append(self.lossSub)
        g.append(self.mGroup)
        self.paths = []
        self.dA = False
        self.mode = 0
        self.limit = 8
        self.gameOver = Group()
        self.gameOver.append(Rect(0, 0, 128, 128, fill=0x000000))
        self.gameOver.append(Label(font, x=32, y=64, text="Game Over", color=0xFFFFFF))
        self.lossSub.append(self.gameOver)
        self.gameOver.hidden = True
    def onGameLoss(self):
        self.gameOver.hidden = False
    def dAn(self):
        if self.mode == 1:
            for i in range(15):
                self.marble.fill -= 0x111111
                sleep(0.5)
            self.reset()
    def reset(self, v=False):
        self.marble.x = 0
        self.marble.y = 0
        self.marble.fill = 0xFFFFFF
        self.dA = False
        if v:
            self.clearPaths()
            self.generateMaze()
    def setMode(self, mode):
        self.mode = mode
    def checkWin(self):
        xv = abs(self.goal[0]*16 - self.marble.x)
        yv = abs(self.goal[1]*16 - self.marble.y)
        if xv < 8 and yv < 8:
            self.reset(True)
    def generateMaze(self, nPaths=5):
        """
        should generate the maze
        should set the exit position by changing the goal variable
        once the exit is set run this code:
            self.hole.x = self.goal[0]*16
            self.hole.y = self.goal[1]*16
        end of code
        """
        pass
    def clearPaths(self):
        self.paths.clear()
        for i in range(64):
            self.tiles[i] = 1
    def createPath(self, string):
        """
        syntax:
        'txy-z'
        t = type -> 'r' or 'c'
        x = pos1 -> if 'r' then x coord, if 'c' then y coord
        y = pos2 -> if 'r' then starting row, if 'c' then starting col
        z = dist -> how many tiles in the path
        """
        self.paths.append(string)
        if string[0] == 'c':
            for i in range(int(string[2]), int(string[4])):
                self.tiles[i+int(string[1])*8] = 0
        else:
            for i in range(int(string[2]), int(string[4])):
                self.tiles[i*8+int(string[1])] = 0
    def checkBounds(self, x, y):
        good = False
        if self.mode != 1:
            for path in self.paths:
                if path[0] == 'c':
                    if y == int(path[1])*16:
                        if x >= int(path[2])*16 and x < int(path[4])*16:
                            good = True
                            break
                else:
                    if x == int(path[1])*16:
                        if y >= int(path[2])*16 and y < int(path[4])*16:
                            good = True
                            break
        if not good:
            if self.mode == 1:
                self.dA = True
                good = True
        return good
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
        if self.dA:
            self.dAn
            return None
        direction = 0.675# interesting thing is that if this changed the controls change
        nx = self.marble.x + round(sin(direction*2*pi)*tilt[0])
        ny = self.marble.y + round(cos(direction*2*pi)*tilt[1])
        if nx % 2 != 0:
            if nx < 0:
                nx -= 1
            else:
                nx += 1
        if ny % 2 != 0:
            if ny < 0:
                ny -= 1
            else:
                ny += 1
        if abs(nx) > self.limit:
            if nx < 0:
                nx = self.limit*-1
            else:
                nx = self.limit
        if abs(ny) > self.limit:
            if ny < 0:
                ny = self.limit*-1
            else:
                ny = self.limit
        if nx < 0:
            nx = 0
        elif nx > 112:
            nx = 112
        if ny < 0:
            ny = 0
        elif ny > 112:
            ny = 112
        if ny > -1 and ny < 113:
            if abs(ny - self.marble.y) > self.threshold:
                if self.checkBounds(self.marble.x, ny):
                    self.marble.y = ny
        if nx > -1 and nx < 113:
            if abs(nx - self.marble.x) > self.threshold:
                if self.checkBounds(nx, self.marble.y):
                    self.marble.x = nx
                else:
                    print('x bound')
            else:
                print('x threshold')
        else:
            print('x screen')
        self.checkWin()
