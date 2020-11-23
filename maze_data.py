import random
import math
from displayio import *
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
import time

sprites = Bitmap(32, 32, 2)
colors = Palette(2)
colors[0] = 0x000000
colors[1] = 0xFFFFFF

for i in range(16):# this generates the path tiles
    for i2 in range(16):
        sprites[i, i2] = 1

class Maze:
    def __init__(self, width, height, g):
        self.tiles = TileGrid(sprites, pixel_shader = colors, width=8, height=8, tile_width=16,tile_height=16, default_tile=1)
        self.marble = Circle(random.randint(0, 15)*8, random.randint(0, 15)*8, 8, fill=0xFFFFFF, outline=0x000000) #placed randomly, for now
        self.speed_x = 1 #Placeholder of 1, will represent pixels per second
        self.speed_y = 1
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(0)
        self.generate()
        time.sleep(0.25)
        count = 0
        count2 = 0
        for i in self.board:
            for j in i:
                if not j:
                    self.tiles[count, count2] = 0
                count2 += 1
            count += 1
            count2 = 0
        g.append(self.tiles)
        g.append(self.marble)
            
    def generate(self):
        xs = []
        ys = []
        b = 0
        x = 0
        y = 0
        self.board[0][0] = True
        while True:
            if b==0:
                xs.append(x)
                ys.append(y)
            else:
                x = xs[len(xs)-b-1]
                y = ys[len(ys)-b-1]
            failed = True
            direction = random.randint(0, 4)
            try:
                if (direction==0 or direction==4) and x+1<7 and not self.board[x+1][y] and not self.board[x+2][y] and not self.board[x+1][y+1] and not self.board[x+1][y-1]:
                    x += 1
                    self.board[x][y] = True
                    failed = False
                elif (direction==0 or direction==4) and x+1==7:
                    x += 1
                    self.board[x][y] = True
                    xs.append(x)
                    ys.append(y)
                    break
                elif direction==1 and y+1<8 and not self.board[x][y+1] and not self.board[x][y+2] and not self.board[x+1][y+1] and not self.board[x-1][y+1]:
                    y += 1
                    self.board[x][y] = True
                    failed = False
                elif direction==2 and x-1>=0 and not self.board[x-1][y] and not self.board[x-2][y] and not self.board[x-1][y+1] and not self.board[x-1][y-1]:
                    x -= 1
                    self.board[x][y] = True
                    failed = False
                elif direction==3 and y-1>=0 and not self.board[x][y-1] and not self.board[x][y-2] and not self.board[x+1][y-1] and not self.board[x-1][y-1]:
                    y -= 1
                    self.board[x][y] = True
                    failed = False
            except Exception:
                 print(Exception)
            if failed:
                b += 1
                if b == len(xs):
                    b = 0
            elif b != 0:
                b = 0
                    
                

    def getRange(self):
        return 16#checks the top-left quadrent, be aware, optimisation is required b/c 64 is too many
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
    def move_marble(self, tilt):
        self.speed_x += 10*math.sin(tilt[0]*math.pi/180)
        self.speed_y += 10*math.sin(tilt[1]*math.pi/180)
        change_x = round(self.speed_x)
        change_y = round(self.speed_y)
        if self.marble.x + change_x > 110:
            self.marble.x = 110
            self.speed_x = 0
        elif self.marble.x + change_x < 0:
            self.marble.x = 0
            self.speed_x = 0
        else:
            self.marble.x += change_x
        if self.marble.y + change_y> 110:
            self.marble.y = 110
            self.speed_y = 0
        elif self.marble.y + change_y< 0:
            self.marble.y = 0
            self.speed_y = 0
        else:
            self.marble.y += change_y
