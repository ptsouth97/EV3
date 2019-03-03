#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep


def main():
	''' Main function for testing purposes'''

	btn = ev3.Button()
	check(btn)

	
def check(btn):
	'''The loop checks whether any button is pressed and if so beeps and exits the script. 
	   The script checks the button state every 0.01 second.'''


	btn = Button()

	while True:

 		# Checks if any button is pressed.
		if btn.any():   
			# Beep and then wait for the beep to finish
			Sound.beep().wait()  

			# Stop the program
			exit()  

		else:
			# Wait 0.01 second
			sleep(0.01)  	

	return


if __name__ == '__main__':
	main()
