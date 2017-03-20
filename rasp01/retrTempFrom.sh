#!/bin/sh

client=rasp02
if [ "$1" != "" ]; then
  client=$1
fi

file=/home/pi/last_temp

# Check if the client host is reachable
ping -q -c 3 -i 1 ${client} > /dev/null 2>&1
if [ $? = 0 ]; then
  ssh ${client} "tail -n 1 temps.csv" > ${file}.tmp
  nl=`wc -l ${file}.tmp | awk '{print $1}'`
  if [ ${nl} -gt 0 ]; then
    mv ${file}.tmp ${file}
  fi
else
  echo "ERROR: ${client} is not reachable"
fi

