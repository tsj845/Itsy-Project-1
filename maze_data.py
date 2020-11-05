import random

class Marble:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
