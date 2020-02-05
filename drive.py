#!/usr/bin/python3


import ev3dev.ev3 as ev3
from time import sleep


def main():
	''' main function for testing purposes'''

	my_loop()


def my_loop():

	mB = ev3.LargeMotor('outB')
	mC = ev3.LargeMotor('outC')

	ir = ev3.InfraredSensor()

	distance = ir.value()

	while True:

		mB.run_forever(speed_sp=900)
		sleep(5)

		if distance < 25:
			break

		# go straight (motors B & C)
		# IR - check if distance is less than 25
		# if so, motors B&C go back and right


if __name__ == '__main__':
	main()
