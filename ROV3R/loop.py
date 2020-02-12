#!/usr/bin/python3

import ev3dev.ev3 as ev3


def main():
	''' main function'''

	mB = ev3.LargeMotor('outB')
	mC = ev3.LargeMotor('outC')
	
	tank_drive = MoveTank(mB, mC)
	run(tank_drive)


def run(tk_drive):
	''' run loop'''

	
	
	while True:
		
		# MOVE FORWARD
		# mB.run_forever(speed_sp=900)
		tk_drive.on(50, 50)	
		
		# CHECK IR SENSOR
				
		# IF IR SENSORY PROXIMITY < 25, BACK UP TO THE RIGHT
		
		# WAIT 0.25 SEC
		
		
if __name__ == '__main__':
	main()
