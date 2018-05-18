#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

ts = TouchSensor()

while True:
    Leds.set_color(Leds.LEFT, (Leds.GREEN, Leds.RED)[ts.value()])


