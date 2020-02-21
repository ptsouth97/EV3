#!/usr/bin/python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound
from time import sleep


def main():
	''' main function'''

	tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
	#run(tank_drive)

	infrared = InfraredSensor()
	infrared.mode = 'IR-PROX'
	
	sounds = Sound()
	
	run(tank_drive, infrared, sounds)


def run(tank, ir, sound):
	''' run loop'''

	while True:

		distance = ir.value()
		#print("The distance is " + str(distance))

		tank.on(100, 100)

		if distance < 60:
			sound.beep()
			tank.on_for_seconds(-100, 0, 0.25)
			#time.sleep(0.25)
			continue

		#tank.on_for_seconds(100, 100, 5, brake=True, block=True)

	return
		

if __name__ == '__main__':
	main()
