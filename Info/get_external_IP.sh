#!/bin/sh

touch ${HOME}/latest_external_IP_addr.txt
cd ${HOME}/Raspberry_dev/Info
python get_external_IP.py

