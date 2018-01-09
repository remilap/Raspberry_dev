#!/usr/bin/python

# Import Libraries
import sys
import get_temp_envirophat
import add_value_initState
import manage_low_temp
from subprocess import check_output

# retrieve the home directory
from os.path import expanduser
home_dir = expanduser("~")
print 'home_dir=' + home_dir

# init default corrective temperature
t_cor = 6.8

# read properties file
import configparser
config = configparser.RawConfigParser()
config.read(home_dir + '/Temp.ini')
try:
    t_cor = float(config.get('TempSection', 'shift_derive'))
except:
    print "unable to find 'shift_derive'"

print 't_cor=' + str(t_cor)

t = get_temp_envirophat.read_temp()

internal_temp = check_output("vcgencmd measure_temp | cut -d= -f2 | cut -d\\' -f1", shell=True)
int_t = float(internal_temp.strip())
cor_t = t - int_t / 6.1
t -= t_cor
print '{0:.1f} {1:.1f} {2:.1f}'.format(t, int_t, cor_t)

if (len(sys.argv) > 1):
    # Send value to initialstate.com
    add_value_initState.send_value(t)

    t = round(t*10)/10
    manage_low_temp.analyze(t)


