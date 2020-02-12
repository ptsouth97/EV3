#!/usr/bin/python3

import ev3dev.ev3 as ev3
from time import sleep


def main():
	''' main function'''

	mB = ev3.LargeMotor('outB')
	mC = ev3.LargeMotor('outC')
	
	ifr = ev3.InfraredSensor()
	ifr.mode = 'IR-PROX'
	
	tank_drive = MoveTank(mB, mC)
	run(tank_drive, ifr)


def run(tk_drive, ir):
	''' run loop'''
	
	while True:
		
		# MOVE FORWARD
		# mB.run_forever(speed_sp=900)
		tk_drive.on(50, 50)	
		
		# CHECK IR SENSOR
		distance = ir.value()
		
		# IF IR SENSORY PROXIMITY < 25, BACK UP TO THE RIGHT
		if distance < 50:
			ev3.Sound.beep()
			
			# WAIT 0.25 SEC
			sleep(0.25)
		
		
if __name__ == '__main__':
	main()
