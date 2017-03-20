#!/bin/sh

cd /home/pi/Raspberry_dev/Camera
python cam01.py

sudo mv image* /var/www/html/motion

