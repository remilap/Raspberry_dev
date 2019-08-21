#!/bin/sh

cd /home/pi/Raspberry_dev/Camera
python cam01.py

cd /home/pi/Raspberry_dev/Camera
imgFile=`/bin/ls image*`
if [ "$imgFile" != "" ]; then
  mv $imgFile /var/lib/motion
fi

