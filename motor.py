#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep


'''makes a large motor on port B turn through 360° at speed 900 
and optionally apply a 'hold' (like a strong brake - see later):'''
'''
m = LargeMotor('outB')

m.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")

sleep(5)   # Give the motor time to move'''


'''This example runs a large motor attached to port B backwards for 
3 seconds with a 'speed setpoint' set to -750 (equivalent to a power 
setting of -75 in the standard EV3 software).'''
'''
m = LargeMotor('outB')
m.run_timed(time_sp=3000, speed_sp=-750)
print("set speed (speed_sp) = " + str(m.speed_sp))
sleep(1)  # it takes a moment for the motor to start moving
print("actual speed = " + str(m.speed))
sleep(4)'''

'''turn motor forever'''

m = LargeMotor('outB')

m.run_forever(speed_sp=900)
sleep(5)
m.stop(stop_action="hold")
sleep(5)
