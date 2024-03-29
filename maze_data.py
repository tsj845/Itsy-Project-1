from random import seed, randrange
import math
from displayio import *
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect

sprites = Bitmap(32, 32, 2)# creates the spritesheet
colors = Palette(2)# creates the color palette
colors[0] = 0x000000# fills in the color palette
colors[1] = 0xFFFFFF

for i in range(16):# this generates the path tiles
    for i2 in range(16):
        sprites[i, i2] = 1

class Marble:
    def __init__(self, x, y, parent):
        self.parent = parent
        self.sprite = Circle(x, y, 8, fill=0xFFFFFF, outline=0x000000)# creates the marble drawn onscreen
    def oOB(self, x, y):
        for path in self.parent.paths:# checks all of the paths
            if path[0] == 'c':# this checks the orientation of the path
                if y == int(path[1])*16:# this makes sure that the y coordinate is in the path at all
                    if x >= int(path[2])*16 and x < int(path[4])*16:# checks to make sure that the x coordinate is valid
                        return True
            else:
                if x == int(path[1])*16:# these do the same tasks as the lines above except that the x and y checking is swapped
                    if y >= int(path[2])*16 and y < int(path[4])*16:
                        return True
        return False
    def move(self, direction, step):
        x = self.sprite.x# this provides a value that won't affect the sprite if changed
        y = self.sprite.y
        if direction == 'up' and self.sprite.y > 8:# these if statements ensure that the marble isn't going to go off the screen
            y -= step# the x and y coordinates of the sprite are not changed until later so that they can be checked
        elif direction == 'down' and self.sprite.y < 120:
            y += step
        elif direction == 'right' and self.sprite.x < 120:
            x += step
        elif direction == 'left' and self.sprite.x > 8:
            x -= step
        if self.oOB(x, y):# ensures that the x and y coordinates are valid before applying them to the marble
            self.sprite.x = x
            self.sprite.y = y

class Maze:
    def __init__(self, width, height, g):
        self.width = width
        self.height = height
        self.tiles = TileGrid(sprites, pixel_shader = colors, width=8, height=8, tile_width=16,
                              tile_height=16, default_tile=1)
        # self.tiles stores the color values for the maze
        self.marble = Marble(8, 8, self)# creates a marble
        g.append(self.tiles)# renders the maze and marble
        g.append(self.marble.sprite)
        self.paths = []# this is the list of all the paths
        self.goal = (7, 7)# the goal for the maze (will contain a seperate texture later)
    def checkWin(self):# currently doesn't trigger anything
        ## checks to see if the sprite is within twelve (12) pixels of the center coordinates of the tile marked as the goal
        win = False
        if abs(self.goal[0]*16 - self.marble.sprite.x) < 16 and abs(self.goal[1]*16 - self.marble.sprite.y) < 16:
            win = True
        print(win)
    def generateMaze(self):
        pass
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
    def move(self, tilt):# allows the marble to move through the maze
        direc1 = 'up'# "up" is a placeholder, there are two direction and speed variables because-
        direc2 = 'up'## there are two axes
        speed1 = 0
        speed2 = 0
        if abs(tilt[0]) > 3:# provides a thresh hold for movement
            if tilt[0] > 0:# checks if the player has tilted the maze right or left
                direc1 = 'right'# sets the direction variable accordingly
            else:
                direc1 = 'left'
            speed1 = abs(round(tilt[0]))
        if abs(tilt[1]) > 3:
            if tilt[1] > 0:
                direc2 = 'down'
            else:
                direc2 = 'up'
            speed2 = abs(round(tilt[1]))
        self.marble.move(direc1, speed1)# moves the marble
        self.marble.move(direc2, speed2)
        self.checkWin()# checks if the player has won
