#!/usr/bin/env python3
# so that script can be run from Brickman

# import statements
import ev3dev.ev3 as ev3
from time import sleep


def main():
	''' main function for testing purposes'''

	# instantiate a motor object on the 'B' port
	m = ev3.LargeMotor('outB')
	
	#turn_360(m)
	backwards(m)
	#turn_forever(m)


def turn_360(m):
	'''makes a large motor on port B turn through 360° at speed 900 
	   and optionally apply a 'hold' (like a strong brake - see later):'''

	# run_to_rel_pos runs to a position relative to the current position value

	# position_sp specifies the target position for run_to_rel_pos command
	position_sp=360

	# speed_sp sets the target speed in tacho counts per second
	speed_sp=900

	# stop actions = coast, brake, or hold
	stop_action='hold'

	m.run_to_rel_pos(position_sp=position_sp, speed_sp=speed_sp, stop_action=stop_action)

	# Wait for completion
	m.wait_while('running')

	# Beep when completed
	ev3.Sound.beep()

	# Alternatively, give the motor time to move
	#sleep(5)
  
	return


def backwards(m):
	'''This example runs a large motor attached to port B backwards for 
	3 seconds with a 'speed setpoint' set to -750 (equivalent to a power 
	setting of -75 in the standard EV3 software).'''

	# run_timed runs the motor for the amount of time specified

	# time_sp is amount of time motor will run in milliseconds
	time_sp=3000

	# speed_sp sets the target speed in tacho counts per second ('-' for backwards)
	speed_sp=-750

	m.run_timed(time_sp=time_sp, speed_sp=speed_sp)
	print("set speed (speed_sp) = " + str(m.speed_sp))
	sleep(1)  # it takes a moment for the motor to start moving
	print("actual speed = " + str(m.speed))
	m.wait_while('running')
	#sleep(4)

	ev3.Sound.beep()

	return


def turn_forever(m):
	'''turn motor forever'''

	m.run_forever(speed_sp=900)
	sleep(5)
	m.stop(stop_action="hold")
	sleep(5)

	ev3.Sound.beep()

	return


if __name__ == '__main__':
	main()
