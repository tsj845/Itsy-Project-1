import board
import busio
import time
import pers
from adafruit_register import i2c_bit

sense = pers.sensor# gets a reference to the sensor

r = i2c_bit.RWBit(0x58, 6, lsb_first=False)
r2 = i2c_bit.RWBit(0x58, 5, lsb_first=False)
r3 = i2c_bit.RWBit(0x58, 4, lsb_first=False)

r.__set__(sense, 1)
r2.__set__(sense, 1)
r3.__set__(sense, 1)

tapBit = i2c_bit.RWBit(0x1C, 1, lsb_first=False)

def run():
  while True:
    if tapBit:
      print('tap')