#!/usr/bin/python

# Robotics - Keyboard control Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time
import lib_util
import lib_motors_evol
import curses
from curses import wrapper


#stdscr = curses.initscr()
#curses.noecho()
#curses.cbreak()
#stdscr.keypad(True)

def main(stdscr):
	# Clear screen
	stdscr.clear()
	lib_util.setDebug(1)

	lib_motors_evol.init()

	k_pres = "Key pressed: "
	to_turn = 0.5
	speed_r = 0
	speed_l = 0
	speed_turn = 0.5
	lib_motors_evol.stopMotors()
	running = True
	while running:
		stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
		c = stdscr.getkey()
		stdscr.addstr(1, 0, " " * 50)
		if c == ord('q'):
			stdscr.addstr(1, 0, k_pres + "q => EXIT")
			running = False
			lib_motors_evol.stopMotors()
			time.sleep(1)
		elif c == ord(' '):
			stdscr.addstr(0, 1, k_pres + "space => BRAKE")
			speed_l = 0
			speed_r = 0
			lib_motors_evol.stopMotors()
		elif c == curses.KEY_UP:
			stdscr.addstr(1, 0, k_pres + "UP => SPEED UP")
			if speed_l < lib_motors_evol.speed_max and speed_r < lib_motors_evol.speed_max:
				speed_l += 1
				speed_r += 1
		elif c == curses.KEY_DOWN:
			stdscr.addstr(1, 0, k_pres + "DOWN => SPEED DOWN")
			if speed_l > -lib_motors_evol.speed_max and speed_r > -lib_motors_evol.speed_max:
				speed_l -= 1
				speed_r -= 1
		elif c == curses.KEY_LEFT:
			stdscr.addstr(1, 0, k_pres + "LEFT => TURN LEFT")
			if speed_l > speed_turn:
				speed_l -= speed_turn
				lib_motors_evol.move(speed_l, speed_r)
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
                                stdscr.refresh()
				time.sleep(to_turn)
				speed_l += speed_turn
			if speed_l < -speed_turn:
				speed_l += speed_turn
				lib_motors_evol.move(speed_l, speed_r)
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
                                stdscr.refresh()
				time.sleep(to_turn)
				speed_l -= speed_turn
		elif c == curses.KEY_RIGHT:
			stdscr.addstr(1, 0, k_pres + "RIGHT => TURN RIGHT")
			if speed_r > speed_turn:
				speed_r -= speed_turn
				lib_motors_evol.move(speed_l, speed_r)
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				time.sleep(to_turn)
				speed_r += speed_turn
			if speed_r < -speed_turn:
				speed_r += speed_turn
				lib_motors_evol.move(speed_l, speed_r)
				stdscr.addstr(0, 0, "Left: " + str(speed_l) + " Right: " + str(speed_r) + " " * 10)
				stdscr.refresh()
				time.sleep(to_turn)
				speed_r -= speed_turn
		lib_motors_evol.move(speed_l, speed_r)

		stdscr.refresh()

#lib_motors_evol.LeftStay()
#lib_motors_evol.RightStay()

	lib_motors_evol.stopMotors()

	lib_motors_evol.end()

#curses.nocbreak()
#stdscr.keypad(False)
#curses.echo()
#curses.endwin()

wrapper(main)

