import maze_text
from displayio import Group

white = 0xFFFFFF
black = 0x000000

class mainMenu():
    def __init__(self, g):
        self.group = Group()
        g.append(self.group)
        self.mainMenu = maze_text.menu(self.group, 8, 0, 16)
        self.videoSettings = maze_text.subMenu(self.group, 8, 0, 16, parent=self.mainMenu)
        self.gameSettings = maze_text.subMenu(self.group, 8, 8, 16, parent=self.mainMenu)
        self.mainMenu.addButton(text="video settings", func=self.videoSettings.show)
        self.mainMenu.addButton(text="game settings", func=self.gameSettings.show)
        self.videoSettings.addButton(text="return to main menu", func=self.hide)
        self.videoSettings.addButton(text="toggle color mode (W.I.P)", func=None)
        self.gameSettings.addButton(text="return to main menu", func=self.hide)
    def move(self, direc):
        maze_text.menuHandler.event(f'button_{direc}')