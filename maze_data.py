import random

class Marble:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.marble = Marble(random.randint(0, 15), random.randint(0, 15))
