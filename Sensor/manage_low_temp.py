#!/usr/bin/python

# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature

# Import Libraries
import os
import glob
import time
from time import localtime, strftime
import send_sms



# send SMS si temperature trop basse
fnlow = '/home/pi/sms_low_temp_date.txt'
fncsv = '/home/pi/temps.csv'

def analyze(t):
    # write last temp in a file
    fo = open(fncsv, 'a')
    fo.write(strftime('%Y%m%d%H%M%S', localtime()) + ',' + str(t) + '\n')
    fo.close()

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


