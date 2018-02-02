#!/usr/bin/python

# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature

# Import Libraries
import sys
import get_temp_sensor
import add_value_initState
import manage_low_temp


t = get_temp_sensor.read_temp()

# write temperature in csv file
t = round(t*10)/10
manage_low_temp.write_csv(t)

if (len(sys.argv) > 1):
    # Send value to initialstate.com
    add_value_initState.send_value(t)

    # Send sms if needed
    manage_low_temp.analyze(t)


