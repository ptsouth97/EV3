#!/usr/bin/python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound


def main():
	''' main function to initialize settings'''

	# initialize tank drive
	tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

	# initialize infrared sensor in proximity mode
	infrared = InfraredSensor()
	infrared.mode = 'IR-PROX'
	
	# intialize sounds
	sounds = Sound()
	
	# call run function
	run(tank_drive, infrared, sounds)


def run(tank, ir, sound):
	''' run loop to drive ROV3R forward until it encounters an obstacle'''

	while True:

		# Drive ROV3R forward
		tank.on(100, 100)

		# Check ir sensor for proximity to objects
		distance = ir.value()

		# If proximity is less than 60, beep and back up to the right for 1/4 second
		if distance < 60:
			# Beep
			sound.beep()

			# Backup
			tank.on_for_seconds(-100, 0, 0.25)
			continue

	return
		

if __name__ == '__main__':
	main()
