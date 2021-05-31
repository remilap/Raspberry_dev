#!/bin/sh

file=/sys/class/leds/led0/trigger
grep -q "\[" ${file}
if [ $? = 1 ]; then
  sudo sh -c "echo none > ${file}"
fi

fn=`basename $0`
led=`echo ${fn} | cut -c1-4`
bright_file=/sys/class/leds/${led}/brightness
echo ${fn} | grep -q "_off"
# if the script name contains _off, the return code is 0, so we turn the light off
# if the script name does not contain _off, the return code is 1, so we turn the light on
sudo sh -c "echo $? > ${bright_file}"

