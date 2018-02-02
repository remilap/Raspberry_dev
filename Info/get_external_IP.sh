#!/bin/sh

touch $HOME/latest_external_IP_addr.txt
cd /home/pi/Raspberry_dev/Info
python get_external_IP.py

