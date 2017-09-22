#!/usr/bin/python

import os, sys
d = os.path.dirname(__file__)
d = d if d else '.'
sys.path.append(d + "/../Lib")
import send_sms

cmde="wget http://checkip.dyndns.org/ -O - -o /dev/null | cut -d: -f 2 | cut -d\< -f 1"
sortie=os.popen(cmde, "r").read()

fnIPaddr="$HOME/latest_external_IP_addr.txt"

try:
    fm = open(fnIPaddr, 'r')
    contenu = fm.read()
#    print('contenu du fichier ' + fnIPaddr + ' : ' + contenu)
    fm.close()
except:
    contenu = 0
#    print('fichier ' + fnIPaddr + ' inexistant => contenu = 0')

if sortie != contenu:
    # write last IP addr in a file
    fo = open(fnIPaddr, 'w')
    fo.write(sortie + '\n')
    fo.close()

    send_sms.send("Nouvelle adresse IP externe : " + sortie)

