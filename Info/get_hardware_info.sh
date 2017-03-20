#!/bin/sh

rev=`cat /proc/cpuinfo | grep 'Revision' | awk '{print $3}' | sed 's/^1000//'`
echo "rev=$rev"

awk -F\; -v rev=$rev '{
  if (NR==1) {
    split($0,hd,";")
  }
  if ($1~rev) {
    for (i=1;i<=NF;i++) {
      printf"%-12s: %s\n",hd[i],$i
    }
  }
}' raspberry_hardware_versions.csv 

