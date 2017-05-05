#!/usr/bin/python
#
# Script for sending an SMS
#
import sys
import os

usr = "16559683"
pwd = "6TNE9v50GEEWyL"
url = "https://smsapi.free-mobile.fr/sendmsg?user=" + usr + "\&pass=" + pwd + "\&msg="

def send(msg_brut):
    msg = ""
    n = 0
    for w in msg_brut.split():
        msg += w + "%20"
    #print msg

    os.system('curl ' + url + msg)

    return

