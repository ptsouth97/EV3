#!/usr/bin/python3

<<<<<<< HEAD
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from time import sleep


def main():
	''' main function'''

<<<<<<< HEAD
	# mB = ev3.LargeMotor('outB')
	# mC = ev3.LargeMotor('outC')

	# run(mB, mC)
	
	tank_drive = MoveTank('outB', 'outC')
	run(tank_drive)

def run(tank):
	''' run loop'''

	# mB.run_timed(time_sp=5, speed_sp=900, stop_action='brake')
	# mB.run_forever(speed_sp=900)
	tank.on_for_seconds(100, 100, 5, brake=True, block=True)

	return
		

if __name__ == '__main__':
	main()
