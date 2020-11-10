# ciruit python libraries unable to be put into github directly:
goto: https://circuitpython.org/libraries
download Bundle Version 6.x

# you will need:
1. adafruit_bus_device
2. adafruit_lsm6ds
3. adafruit_register

# Instructions:
drag these files into the "lib" folder on the Isty

# Marble Maze

GOAL:

to create a program for the adafruit ItsyBitsy nrf52840 + SSD1327 OLED Monochrome display with inputs from a 6 dof IMU + a five directional button

CURRENT TASKS:
1. connect the display to the itsy (done)
2. connect the dof IMU to the itsy (pending)
3. create a sprite sheet containing a marble and all required maze peices (pending)
4. give the player the ability to control the marble by tilting the IMU (pending)
5. ensure that the mable is not able to pass through walls

FANCY BITS:
1. randomly generated mazes
2. marble is able to roll between the two walls of a passage

EXTRA FANCY BITS:
1. multiplayer support using bluetooth + internet
2. add flappy bird
