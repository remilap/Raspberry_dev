#!/usr/bin/python

# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature

# Import Libraries
import os, sys
import glob
import time
from time import localtime, strftime
from subprocess import check_output
d = os.path.dirname(__file__)
d = d if d else '.'
sys.path.append(d + "/../Lib")
import send_sms


# write temperature in a csv file
fncsv = '/home/pi/temps.csv'

def write_csv(t):
    # retrieve internal temperature
    internal_temp = check_output("vcgencmd measure_temp | cut -d= -f2 | cut -d\\' -f1", shell=True)
    int_t = float(internal_temp.strip())
    cor_t = t - int_t / 6.1

    # write last temp in a file
    fo = open(fncsv, 'a')
    #fo.write(strftime('%Y%m%d%H%M%S', localtime()) + ',' + str(t) + '\n')
    fo.write('{0},{1:.1f},{2:.1f},{3:.1f}\n'.format(strftime('%Y%m%d%H%M%S', localtime()), t, int_t, cor_t))
    fo.close()

    return


# send SMS if temperature is too low or comes back normal
fnlow = '/home/pi/sms_low_temp_date.txt'

def analyze(t):
    try:
        fm = open(fnlow, 'r')
        contenu = fm.read()
        print('contenu du fichier ' + fnlow + ' : ' + contenu)
        fm.close()
    except:
        contenu = 0
        print('fichier ' + fnlow + ' inexistant => contenu = 0')

    if t < 15:
        now = time.time()
        ecoule = (now - float(contenu)) / 3600
        h = int(time.strftime('%H'))
        print('now=' + str(now) + ', ecoule=' + str(ecoule) + ', h=' + str(h))
        if ecoule > 8 and h <= 22 and h >= 6:
            msg = "Temperature\%20basse\%20:\%20" + str(t)
            print('msg to send: ' + msg)
#            os.system('curl ' + url + msg)
            send_sms.send(msg)
            fm = open(fnlow, 'w')
            fm.write(str(now))
            fm.close()

    if t > 18 and contenu > 0:
        msg = "Temperature\%20revenue\%20correcte\%20:\%20" + str(t)
        print('msg to send: ' + msg)
#        os.system('curl ' + url + msg)
        send_sms.send(msg)
        os.remove(fnlow)

    return


