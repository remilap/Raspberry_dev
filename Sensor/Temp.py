#!/usr/bin/python

# Import Libraries
import sys
import get_temp_envirophat
import add_value_initState
import manage_low_temp


t = get_temp_envirophat.read_temp()
print t

if (len(sys.argv) > 1):
    # Send value to initialstate.com
    add_value_initState.send_value(t)

    manage_low_temp.analyze(t)


