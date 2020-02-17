#!/usr/bin/python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
#import ev3dev.ev3 as ev3
#from ev3dev.motor import MoveTank


def main():
	''' main function'''

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
