#!/bin/sh

force=0
if [ "$1" = "-f" ]; then
  force=1
  shift
fi
client=rasp02
if [ "$1" != "" ]; then
  client=$1
fi

file=/home/pi/last_temp

# Check if the client host is reachable
ping -q -c 3 -i 1 ${client} > /dev/null 2>&1
if [ $? = 0 -o ${force} = 1 ]; then
  ssh ${client} "tail -n 1 temps.csv" > ${file}.tmp
  nl=`wc -l ${file}.tmp | awk '{print $1}'`
  if [ ${nl} -gt 0 ]; then
    if [ "${client}" = "rasp03" ]; then
      dat=`cut -d, -f1 ${file}.tmp`
      temp=`cut -d, -f2 ${file}.tmp`
      temp=`echo "${temp} - 6.8" | bc`
      echo "${dat},${temp}" > ${file}
    else
      mv ${file}.tmp ${file}
    fi
  fi
else
  echo "ERROR: ${client} is not reachable"
fi

