from adafruit_display_text.label import Label
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
import terminalio

font = terminalio.FONT

white = 0xFFFFFF
black = 0x000000

class menu():
    def __init__(self, g, x, y, spacing, color=0xFFFFFF, backing=0x000000, max_buttons=5):
        self.maxB = max_buttons
        self.mainColor = color
        self.backingColor = backing
        self.group = Group(max_size=max_buttons)
        g.append(self.group)
        self.button_count = 0
        self.selected_button = 0
        self.x = x
        self.y = y
        self.ySpacing = spacing
    def toggleColors(self):
        sub = self.group[self.selected_button]
        l = sub[1]
        r = sub[0]
        if l.color == white:
            l.color = black
            l.background_color = white
            r.fill = white
            r.outline = black
    def addButton(self, text=None):
        self.button_count += 1
        if text == None:
            text = f'Button {self.button_count}'
        subGroup = Group()
        l = Label(font, color=self.mainColor, background_color=self.backingColor, text=text,
                  x=self.x, y=self.y+self.button_count*self.ySpacing)
        r = Rect(self.x, self.y/2+self.button_count*self.ySpacing, l.bounding_box[2],
                 fill=self.backing_color, outline=self.color)
        subGroup.append(r)
        subGroup.append(l)
        if self.button_count == 1:
            self.toggleColors()
        self.group.append(subGroup)
    def move(self, direc):
        if direc == 'up':
            if self.selected_button > 0:
                self.toggleColors()
                self.selected_button -= 1
                self.toggleColors()
        else:
            if self.selected_button < self.button_count:
                self.toggleColors()
                self.selected_button += 1
                self.toggleColors()