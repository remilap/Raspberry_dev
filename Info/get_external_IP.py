#!/usr/bin/python

import os, sys, time
d = os.path.dirname(__file__)
d = d if d else '.'
sys.path.append(d + "/../Lib")
import send_sms
from datetime import datetime, timedelta

debug = 0

cmde = "wget http://checkip.dyndns.org/ -O - -o /dev/null | cut -d: -f 2 | cut -d\< -f 1 | awk '{print $1}' | head -n 1"
sortie = os.popen(cmde, "r").read().rstrip()
if debug:
    print("Resultat: >{0:s}<".format(sortie))

if not sortie:
    print("Resultat vide, on ne fait rien")
    exit()

fnIPaddr = "/home/pi/latest_external_IP_addr.txt"

try:
    fm = open(fnIPaddr, 'r')
    contenu = fm.read()
    fm.close()
    if debug:
        print("contenu du fichier {0:s}: >{1:s}<".format(fnIPaddr, contenu))
except:
    contenu = 0
    if debug:
        print("fichier {0:s} inexistant => contenu = 0".format(fnIPaddr))

if sortie != contenu:
    # write last IP addr in a file
    if debug:
        print('Nouvelle adresse IP => write to file and send sms')
    fo = open(fnIPaddr, 'w')
    fo.write(sortie)
    fo.close()

    send_sms.send('Nouvelle adresse IP externe : ' + sortie)

else:
    dat = os.path.getmtime(fnIPaddr)
    past = ( datetime.now() - timedelta(days=30) - datetime(1970,1,1) ).total_seconds()
    if debug:
        print("dat: {0:f}, past: {1:f}".format(dat, past))
    if dat < past:
        if debug:
            print('Adresse IP externe inchangee depuis un mois : ' + sortie)
        send_sms.send('Adresse IP externe inchangee depuis un mois : ' + sortie)

