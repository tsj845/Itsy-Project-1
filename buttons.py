import board
import gamepad
from digitalio import DigitalInOut, Direction, PULL

pad = gamepad.GamePad(
  DigitalInOut(board.A0),
  DigitalInOut(board.A1),
  DigitalInOut(board.A2),
  DigitalInOut(board.A3),
  DigitalInOut(board.A4)
)