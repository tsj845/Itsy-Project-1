import board
import busio
import time
import pers
from adafruit_register import i2c_bit
from adafruit_register import i2c_bits

sense = pers.sensor# gets a reference to the sensor
i2c = pers.i2c

r = i2c_bit.RWBit(0x58, 6, lsb_first=False)
#r2 = i2c_bit.RWBit(0x58, 5, lsb_first=False)
#r3 = i2c_bit.RWBit(0x58, 4, lsb_first=False)

#c1 = i2c_bit.RWBit(0x59, 5, lsb_first=False)

c1 = i2c_bits.RWBits(5, 0x59, 3, register_width=1, lsb_first=False, signed=False)
# 5 - 6
r.__set__(sense, 1)
#r2.__set__(sense, 1)
#r3.__set__(sense, 1)

#c1.__set__(sense, 31)

tapBit = i2c_bit.ROBit(0x1C, 7, lsb_first=False)

log = []

def run():
  while True:
    if tapBit.__get__(sense):
      print('tap')

def run2():
  for i in range(100):
    log.append(tapBit.__get__(sense))
    time.sleep(0.2)

## 0x6A

#i2c.writeto(0x18, bytes([0x05]), stop=False)
#...     result = bytearray(2)
#...     i2c.readfrom_into(0x18, result)

def byteTo(obj, t=int):
  s = str(obj)
  s = s.split('\\')
  s2 = []
  s3 = []
  for val in s:
    if 'x' in val:
      s2.append(val)
  for v in s2:
    s3.append(int(''.join(v[1:3]), 16))
  if t != int:
    for v in s3:
      v = t(v)
  return s3

def checkRegister(device, register_address):
  while not i2c.try_lock():
    pass
  try:
    address = device.i2c_device.device_address
    i2c.writeto(address, bytes([register_address]))
    result = bytearray(2)
    i2c.readfrom_into(address, result)
    i2c.unlock()
    return result
  except:
    i2c.unlock()

def cr2(dev, ra):
  da = dev.i2c_device.device_address
  bits = []
  for i in range(8):
    tBit = i2c_bit.RWBit(ra, i, lsb_first=False)
    bits.append(tBit.__get__(sense))
  return bits

def run3(secs):
  for i in range(secs*10):
    print(cr2(sense, 0x1C))
    time.sleep(0.1)