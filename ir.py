#!/usr/bin/env python3

import ev3dev.ev3 as ev3


def main():
	''' Main function for testing purposes'''

	ir = ev3.InfraredSensor()
	sensor(ir)


def sensor(ir):
	'''Connect infrared and touch sensors to any sensor ports and check they are connected'''

	assert ir.connected, "Connect a single infrared sensor to any sensor port"

	#ts = TouchSensor();    assert ts.connected, "Connect a touch sensor to any port" 
	# can have 2 statements on same line if use semi colon

	# Put the infrared sensor into proximity mode.
	ir.mode = 'IR-PROX'
	'''
	while not ts.value():    # Stop program by pressing touch sensor button
	# Infrared sensor in proximity mode will measure distance to the closest
	# object in front of it.'''

	distance = ir.value()

	if distance < 60:
		ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)

	else:
		ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)

	ev3.Sound.beep()       
	ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)  
	#make sure left led is green before exiting
	
	return


if __name__ == '__main__':
	main()
