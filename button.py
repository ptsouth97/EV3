#!/usr/bin/env python3

'''The loop checks whether any button is pressed and if so beeps and exits the script. The script checks the button state every 0.01 second.'''

from ev3dev.ev3 import *
from time import sleep

btn = Button()

while True:
    if btn.any():    # Checks if any button is pressed.
        Sound.beep().wait()  # Wait for the beep to finish.
        exit()  # Stop the program.
    else:
        sleep(0.01)  # Wait 0.01 second	
