from adafruit_display_text.label import Label
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from displayio import Group
import terminalio

font = terminalio.FONT

white = 0xFFFFFF
black = 0x000000

class menuHandler():
    def __init__(self):
        self.menus = []
        self.selectedMenu = None
    def newMenu(self, menu):
        self.menus.append(menu)
    def menuOpened(self, menu):
        if self.selectedMenu != None:
            self.selectedMenu.hide(False)
        self.selectedMenu = menu
    def menuClosed(self, menu):
        self.selectedMenu = None
    def event(self, name):
        if self.selectedMenu == None:
            return
        if name == 'button_up':
            self.selectedMenu.move('up')
        elif name == 'button_down':
            self.selectedMenu.move('down')
        elif name == 'button_select':
            self.selectedMenu.select()

menuHandler = menuHandler()

class menu():
    def __init__(self, g, x, y, spacing, color=white, backing=black, max_buttons=5, title=None):
        self.maxB = max_buttons
        self.mainColor = color
        self.backing_color = backing
        self.n = 1
        if title != None:
            self.n = 2
        self.group = Group(max_size=max_buttons+self.n)
        self.group.append(Rect(0, 0, 128, 128, fill=black))
        self.group.append(title)
        g.append(self.group)
        self.group.hidden = True
        self.button_count = 0
        self.selected_button = 0
        self.x = x
        self.y = y
        self.ySpacing = spacing
        self.funcs = []
        self.status = False
        menuHandler.newMenu(self)
    def show(self):
        self.group.hidden = False
        self.status = True
        menuHandler.menuOpened(self)
    def hide(self, v=True):
        self.group.hidden = True
        self.status = False
        if v:
            menuHandler.menuClosed(self)
    def toggleColors(self):
        sub = self.group[self.selected_button+self.n]
        l = sub[1]
        r = sub[0]
        if l.color == white:
            l.color = black
            r.fill = white
            r.outline = black
        else:
            l.color = white
            r.fill = black
            r.outline = white
    def addButton(self, text=None, func=None):
        self.button_count += 1
        if text == None:
            text = f'Button {self.button_count}'
        subGroup = Group()
        #background_color=self.backing_color
        l = Label(font, color=self.mainColor, text=text,
                  x=self.x, y=self.y+self.button_count*self.ySpacing)
        #round((self.y/4*3)+self.button_count*self.ySpacing)
        r = Rect(self.x-4, l.y-6, l.bounding_box[2]+8,
                 l.bounding_box[3], fill=self.backing_color, outline=self.mainColor)
        subGroup.append(r)
        subGroup.append(l)
        self.group.append(subGroup)
        if self.button_count == 1:
            self.toggleColors()
        self.funcs.append(func)
        if self.status:
            self.hide()
            self.show()
        else:
            self.show()
            self.hide()
    def move(self, direc):
        if direc == 'up':
            if self.selected_button > 0:
                self.toggleColors()
                self.selected_button -= 1
                self.toggleColors()
        else:
            if self.selected_button < self.button_count-1:
                self.toggleColors()
                self.selected_button += 1
                self.toggleColors()
    def select(self):
        func = self.funcs[self.selected_button]
        if func != None:
            func()

class subMenu(menu):
    def __init__(self, g, x, y, spacing, color=white, backing=black, max_buttons=5, title=None):
        self.maxB = max_buttons
        self.mainColor = color
        self.backing_color = backing
        self.n = 1
        if title != None:
            self.n = 2
        self.group = Group(max_buttons+self.n)