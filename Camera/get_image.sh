#!/bin/sh

devCameraDir=/home/pi/Raspberry_dev/Camera
destImageDir=/var/lib/motion
destImageDir=/home/pi/maison

cd $devCameraDir
python cam01.py

cd $devCameraDir
imgFile=`/bin/ls image*`
if [ "$imgFile" != "" ]; then
  if [ ! -d $destImageDir ]; then
    sudo mkdir $destImageDir
  fi
  mv $imgFile $destImageDir
fi

