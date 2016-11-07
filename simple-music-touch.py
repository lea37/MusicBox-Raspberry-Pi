#READ ME
#if you only care about checking one or a few pins you can
# call the is_touched method with a pin number to directly check that pin.
# This will be a little slower than the above code for checking a lot of pin

import sys
import time

import pygame.mixer
from pygame.mixer import Sound
pygame.mixer.init()


import RPi.GPIO as GPIO
import Adafruit_MPR121.MPR121 as MPR121

sounds = {
    1: Sound("sounds/sound1.wav"),
    6: Sound("sounds/sound2.wav"),
    9: Sound("sounds/sound6.wav"),
    11: Sound("sounds/sound4.wav"),
}


# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# Main loop to print a message every time a pin is touched.
print('Press Ctrl-C to quit.')
last_touched = cap.touched()
while True:
    for key, value in sounds.items():
        if cap.is_touched(key):
            print('Pin '+ str(key) + ' is being touched!')
            value.play()


