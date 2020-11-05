import random
import displayio

## we need five sprites (ball, verticle passage, horizontal passage, corner, and a solid wall)
# we only need one corner slot in the sheet because we can flip it (might change it later if it turns out to be too difficult)
sprites = Bitmap(32, 32, 2)
colors = Palette(2)
colors[0] = 0x000000
colors[1] = 0xFFFFFF

class Marble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = displayio.TileGrid(sprites, tile_width=16, tile_height=16)
    def move(self, direction, step):
        if direction == 'up':
            self.sprite.y -= step
        elif direction == 'down':
            self.sprite.y += step
        elif direction == 'right':
            self.sprite.x += 1
        else:
            self.sprite.x -= 1

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.marble = Marble(random.randint(0, 15)*8, random.randint(0, 15)*8) #placed randomly, for now
        self.direction = None #Starts as none, will represent what angle marble will move at (0-1)
        self.speed = None #Starts as none, will represent pixels per second
    def move_marble(self):
        if self.direction != None and self.speed != None:
            #TODO: Impliment moving of marble (probably will involve speed being hypotenuse of right triangle, direction being angle, cos and sin to calculate legs)
