#!/usr/bin/python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound


def main():
	''' main function'''

	tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

	infrared = InfraredSensor()
	infrared.mode = 'IR-PROX'
	
	sounds = Sound()
	
	run(tank_drive, infrared, sounds)


def run(tank, ir, sound):
	''' run loop'''

	while True:

		# Check ir sensor for proximity to objects
		distance = ir.value()

		# Drive ROV3R forward
		tank.on(100, 100)

		# If proximity is less than 60, beep and back up to the right for 1/4 second
		if distance < 60:
			sound.beep()
			tank.on_for_seconds(-100, 0, 0.25)
			continue


	return
		

if __name__ == '__main__':
	main()
