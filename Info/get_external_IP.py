#!/usr/bin/python

import os, sys
sys.path.append(os.path.dirname(__file__) + "/../Lib")
import send_sms

cmde="wget http://checkip.dyndns.org/ -O - -o /dev/null | cut -d: -f 2 | cut -d\< -f 1"
sortie=os.popen(cmde, "r").read()

send_sms.send("Adresse IP externe : " + sortie)

