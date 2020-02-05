#!/usr/bin/python3

import ev3dev.ev3 as ev3


def main():
	''' main function'''

	mB = ev3.LargeMotor('outB')
	mC = ev3.LargeMotor('outC')

	run(mB, mC)


def run(mB, mC):
	''' run loop'''

	while True:

		mB.run_forever(speed_sp=900)


if __name__ == '__main__':
	main()
