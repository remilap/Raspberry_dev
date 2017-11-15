#!/usr/bin/python

# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature

# Import Libraries
import sys
import get_temp_sensor
import add_value_initState
import manage_low_temp


t = get_temp_sensor.read_temp()

if (len(sys.argv) > 1):
    # Send value to initialstate.com
    add_value_initState.send_value(t)

    manage_low_temp.analyze(t)


