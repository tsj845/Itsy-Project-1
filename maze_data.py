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
    def __init__(self, g):
        self.tiles = TileGrid(sprites, pixel_shader = colors, width=8, height=8, tile_width=16,tile_height=16, default_tile=1)
        self.marble = Circle(0, 0, 7, fill=0xFFFFFF, outline=0x000000) #placed randomly, for now
        self.speed_x = 1 #Placeholder of 1, will represent pixels per second
        self.speed_y = 1
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(False)
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
        self.marble.x = 0
        self.marble.y = 0
            
    def generate(self):
        xs = [] #stores prier x coords
        ys = [] #stores prier y coords
        b = 0 #stores how far back to go in list
        x = 0 #stores current x
        y = 0 #stores current y
        branches = 0 #stores number of branches created
        self.board[0][0] = True
        while True:
            if b==0:
                #if 0 back, add x and y to lists
                xs.append(x)
                ys.append(y)
            else:
                #otherwise, go back b x and b y
                x = xs[len(xs)-b-1]
                y = ys[len(ys)-b-1]
            failed = True #to test if it fails or not
            direction = random.randint(0, 4) #which direction to "move"
            #checks if direction is one way and if a square there would touch other squares
            if (direction==0 or direction==4) and x+1<7 and not self.rboard(x+1, y) and not self.rboard(x+2, y) and not self.rboard(x+1, y+1) and not self.rboard(x+1, y-1):
                x += 1 #if it succeeds, change x
                self.board[x][y] = True #set the square as a path
                failed = False #did not fail
            #if it has reached the edge
            elif (direction==0 or direction==4) and x+1==7:
                count = 0 #number of paths
                for i in self.board:
                    for j in i:
                        if j:
                            count += 1
                #if this is the first branch
                if branches==0:
                    #add final square
                    x += 1
                    self.board[x][y] = True
                    xs.append(x)
                    ys.append(y)
                    branches += 1 #increase branches
                    b = random.randint(0, len(xs)-1) #set random start for new branch
                    continue
                #if the count is less than half of the board
                elif count<32:
                    #continue to next branch
                    branches += 1
                    b = random.randint(0, len(xs)-1)
                    continue
                #otherwise, stop
                else:
                    break
            elif direction==1 and y+1<8 and not self.rboard(x, y+1) and not self.rboard(x, y+2) and not self.rboard(x+1, y+1) and not self.rboard(x-1, y+1):
                y += 1
                self.board[x][y] = True
                failed = False
            elif direction==2 and x-1>=0 and not self.rboard(x-1, y) and not self.rboard(x-2, y) and not self.rboard(x-1, y+1) and not self.rboard(x-1, y-1):
                x -= 1
                self.board[x][y] = True
                failed = False
            elif direction==3 and y-1>=0 and not self.rboard(x, y-1) and not self.rboard(x, y-2) and not self.rboard(x+1, y-1) and not self.rboard(x-1, y-1):
                y -= 1
                self.board[x][y] = True
                failed = False
            #if it failed, change b so next time it goes back in the lists
            if failed:
                b += 1
                #if b is longer than list, go back to beginning and try again
                if b == len(xs):
                    b = 0
            #if it didn't fail and b isn't 0, change it to 0
            elif b != 0:
                b = 0
    def rboard(self, x, y):
        if x>=0 and x<8 and y>=0 and y<8:
            return(self.board[x][y])
        else:
            return(False)

    def getRange(self):
        return 16#checks the top-left quadrent, be aware, optimisation is required b/c 64 is too many

    def checkBounds(self, x, y):
        count1 = 0
        for i in self.board:
            count2 = 0
            for j in i:
                if x >= count1*14 and x < (count1+1)*14 and y >= count2*14 and y < (count2+1)*14:
                    return j
                count2 += 1
            count1 += 1
        return(True)
    
    def move_marble(self, tilt):
        self.speed_x += 10*math.sin(tilt[0]*math.pi/180)
        self.speed_y += 10*math.sin(tilt[1]*math.pi/180)
        new_x = self.marble.x + round(self.speed_x)
        new_y = self.marble.y + round(self.speed_y)
        tl = self.checkBounds(new_x, new_y)
        tr = self.checkBounds(new_x+7, new_y)
        bl = self.checkBounds(new_x, new_y+7)
        br = self.checkBounds(new_x+7, new_y+7)
        while not tl or not tr or not bl or not br:
            tl = self.checkBounds(new_x, new_y)
            tr = self.checkBounds(new_x+7, new_y)
            bl = self.checkBounds(new_x, new_y+7)
            br = self.checkBounds(new_x+7, new_y+7)
            if not tl:
                if not tr:
                    new_y += 1
                if not bl:
                    new_x += 1
                if not br or (tr and bl):
                    new_x += 1
                    new_y += 1
            elif not tr:
                if not br:
                    new_x -= 1
                if not bl or (tl and br):
                    new_x -= 1
                    new_y += 1
            elif not bl:
                if not br:
                    new_y -= 1
                if tl and tr and br:
                    new_x += 1
                    new_y -= 1
            elif not br and tl and tr and bl:
                new_x -= 1
                new_y -= 1
                
        if new_x > 110:
            self.marble.x = 110
            self.speed_x = 0
        elif new_x < 0:
            self.marble.x = 0
            self.speed_x = 0
        else:
            self.marble.x = new_x
        if new_y> 110:
            self.marble.y = 110
            self.speed_y = 0
        elif new_y< 0:
            self.marble.y = 0
            self.speed_y = 0
        else:
            self.marble.y = new_y
