#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep
import os


def main():
	''' Main function'''

	os.system('setfont Lat15-TerminusBold32x16')

	print('EV3 Python rules!')
	sleep(5)
	ev3.Sound.beep()


if __name__ == '__main__':
	main()
