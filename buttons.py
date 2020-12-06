import board
import gamepad
from digitalio import DigitalInOut, Direction, PULL

class pad():
    def __init__(self):
        self.pad = gamepad.GamePad(
            DigitalInOut(board.A0),
            DigitalInOut(board.A1),
            DigitalInOut(board.A2),
            DigitalInOut(board.A3),
            DigitalInOut(board.A4)
            )
    def eventCheck(self):
        print(self.pad.get_pressed())