#!/usr/bin/python

import os, sys
sys.path.append(os.path.dirname(__file__) + "/../Lib")
import send_sms

send_sms.send("bonjour a tous")

