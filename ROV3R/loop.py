#!/usr/bin/python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank

from time import sleep


def main():
	''' main function'''

	tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
	run(tank_drive)


def run(tank):
	''' run loop'''

	tank.on_for_seconds(100, 100, 5, brake=True, block=True)

	return
		

if __name__ == '__main__':
	main()
