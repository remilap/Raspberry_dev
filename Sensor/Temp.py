#!/usr/bin/python

# Import Libraries
import sys
import get_temp_envirophat
import add_value_initState
import manage_low_temp
from subprocess import check_output


t = get_temp_envirophat.read_temp()

internal_temp = check_output("vcgencmd measure_temp | cut -d= -f2 | cut -d\\' -f1", shell=True)
int_t = float(internal_temp.strip())
cor_t = t - int_t / 6.1
print '{0:.1f} {1:.1f} {2:.1f}'.format(t, int_t, cor_t)

if (len(sys.argv) > 1):
    # Send value to initialstate.com
    add_value_initState.send_value(t)

    manage_low_temp.analyze(t)


