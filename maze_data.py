from time import sleep
from random import seed, randrange
#import math
from displayio import Bitmap, Palette, TileGrid, Group
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect

sprites = Bitmap(32, 32, 2)# creates the spritesheet
colors = Palette(2)# creates the color palette
colors[0] = 0x000000# fills in the color palette
colors[1] = 0xFFFFFF

for i in range(16):# this generates the path tiles
    for i2 in range(16):
        sprites[i, i2] = 1

def 2dLst(rows, cols):
    l = [[None for col in cols] for row in rows]
    return l

class Maze:
    def __init__(self, width, height, g):
        self.width = width
        self.height = height
        self.tiles = TileGrid(sprites, pixel_shader = colors, width=16, height=16, tile_width=16,tile_height=16, default_tile=1)
        self.marble = Circle(random.randint(0, 15)*8, random.randint(0, 15)*8, 8, fill=0xFFFFFF, outline=0x000000) #placed randomly, for now
        self.speed_x = 1 #Placeholder of 1, will represent pixels per second
        self.speed_y = 1
        self.board = []
        for i in range(16):
            self.board.append([])
            for j in range(16):
                self.board[i].append(0)
        self.generate()
        time.sleep(0.25)
        print(self.board)
        count = 0
        count2 = 0
        for i in self.board:
            for j in i:
                if j == 0:
                    self.tiles[count, count2] = 0
                count2 += 1
            count += 1
            count2 = 0
        g.append(self.tiles)
        g.append(self.marble)
    def generate(self):
        board = 2dLst(8, 8)
        xs = [] #stores past "moves" so that if it is stuck in corner, it can go back
        ys = [] #same as above, but for y
        b = 0 #how far back in the array to go
        x = 0 #current x
        y = 0 #current y
        branches = random.randint(1, 3)
        while True:# how do you exit the loop?
            if b==0:
                #if b is 0, add x and y to lists
                xs.append(x)
                ys.append(y)
            else:
                #otherwise, temporarily change x and y to be past x and y
                x = xs[len(xs)-b-1]
                y = ys[len(ys)-b-1]
            failed = True #tests if failed
            direction = random.randint(0, 4)
            if (direction==0 or direction==4) and x+1<15 and board[x+1][y]==0:
                board[x][y] = 1
                x += 1
                failed = False #sets failed to false because it succeeded
            elif (direction==0 or direction==4) and x+1==15:
                break
            elif direction==1 and y+1<16 and board[x][y+1]==0:
                board[x][y] = 1
                y += 1
                failed = False
            elif direction==2 and x-1>=0 and board[x-1][y]==0:
                board[x][y] = 1
                x -= 1
                failed = False
            elif direction==3 and y-1>=0 and board[x][y-1]==0:
                board[x][y] = 1
                y -= 1
                failed = False
            if failed:
                #if it failed, change b so that it goes back a "move"
                print("failed") #for debugging
                b += 1
                if b == len(xs):
                    #if b is too big, go back to beginning (doesn't test all posibilities above, so it will probably succeed after this)
                    b = 0
            elif b != 0:
                #if it didn't fail and b isn't 0, b=0
                b = 0
        self.makePaths(board)
    def makePaths(self, board):
        for i in range(8):#testing, this way you can check the board
            print(board[i])#testing
        t = 'c'
        x = 0
        y = 0
        z = 0
        strings = []
        for row in range(8):
            for col in range(8):
                if board[row][col] == 0:
                    if row < 7:
                        if board[row+1][col] == 0:
                            t = 'r'
                            x = col
                            y = row
                            r = row
                            while board[r][col] == 0:
                                z += 1
                                board[r][col] = 1
                                r += 1
                            string = t + str(x) + str(y) + '-' + str(z)
                            strings.append(string)
                            t = 'c'
                            x = 0
                            y = 0
                            z = 0
                    if col < 7:
                        if board[row][col+1] == 0:
                            t = 'c'
                            x = row
                            y = col
                            r = col
                            while board[row][r] == 0:
                                z += 1
                                board[r][col] = 1
                                r += 1
                            string = t + str(x) + str(y) + '-' + str(z)
                            strings.append(string)
                            t = 'c'
                            x = 0
                            y = 0
                            z = 0
        return strings# for testing, this way you can check it
    def setMode(self, mode):
        self.marble.behavior = mode
    def clearPaths(self):# this is a debugging tool, may be usefull for generating new mazes after-
        self.paths.clear()## old ones are beaten by the player
        for i in range(64):# sets all the tiles to walls and clears the list of paths
            self.tiles[i] = 1
    def createPath(self, string):# syntax: "txy-z"
        self.paths.append(string)# puts the string used to generate the path in the list of paths
        if string[0] == 'c':# checks the orientation of the path
            for i in range(int(string[2]), int(string[4])):# sets the colors
                self.tiles[i+int(string[1])*8] = 0
        else:
            for i in range(int(string[2]), int(string[4])):
                self.tiles[i*8+int(string[1])] = 0
    def move_marble(self, tilt):
        self.speed_x += 10*math.sin(tilt[0]*math.pi/180)
        self.speed_y += 10*math.sin(tilt[1]*math.pi/180)
        if self.direction != None:
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
