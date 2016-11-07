import sys
import time

import pygame.mixer
from pygame.mixer import Sound
pygame.mixer.init()


import RPi.GPIO as GPIO
import Adafruit_MPR121.MPR121 as MPR121

#Sounds array
sounds = {
    0: Sound("sounds/sound00.wav"),
    1: Sound("sounds/sound01.wav"),
    2: Sound("sounds/sound02.wav"),
    3: Sound("sounds/sound03.wav"),
    4: Sound("sounds/sound04.wav"),
    5: Sound("sounds/sound05.wav"),
    6: Sound("sounds/sound06.wav"),
    7: Sound("sounds/sound07.wav"),
    8: Sound("sounds/sound08.wav"),
    9: Sound("sounds/sound09.wav"),
    10: Sound("sounds/sound10.wav"),
    11: Sound("sounds/sound11.wav"),
}


# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# Main loop to print a message every time a pin is touched.
print('Press Ctrl-C to quit.')
last_touched = cap.touched()
while True:

    # Check each pin's last and current state to see if it was pressed or released.
    current_touched = cap.touched()
    for key, value in sounds.items():
        #A value of 1 means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << key
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            print('{0} touched!'.format(key))
            value.play()
        # Next check if transitioned from touched to not touched.
        if not current_touched & pin_bit and last_touched & pin_bit:
            print('{0} released!'.format(key))
    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.1)


