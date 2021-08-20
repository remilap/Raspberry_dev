#!/bin/bash
#
# See https://www.tomshardware.com/how-to/stream-live-video-raspberry-pi
#
# To view the stream, you launch VLC and "Media -> Open Network Stream"
# then fill the URL with: tcp/h264://<IP_address>:5000
#

array[0]="none"
array[1]="negative"
array[2]="solarise"
array[3]="sketch"
array[4]="denoise"
array[5]="emboss"
array[6]="oilpant"
array[7]="hatch"
array[8]="gpen"
array[9]="pastel"
array[10]="watercolour"
array[11]="film"
array[12]="blur"
array[13]="saturation"
array[14]="colourswap"
array[15]="washedout"
array[16]="posterise"
array[17]="colourpoint"
array[18]="colourbalance"
array[19]="cartoon"
size=${#array[@]}
index=$(($RANDOM % $size))
index=0
#echo ${array[$index]}
#sleep 1

raspivid -t 0 -w 800 -h 600 -ifx ${array[$index]} -fps 15 -l -o tcp://0.0.0.0:5000

