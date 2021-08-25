#!/bin/bash
#
# Current Revision bit fields explanation
# https://raspberrypi.stackexchange.com/questions/100076/what-revisions-does-cat-proc-cpuinfo-return-on-the-new-pi-4-1-2-4gb
#
# Bit NOs  3322 2222 2222 1111 1111 1100 0000 0000
# Decimal  1098 7654 3210 9876 5432 1098 7654 3210
# Fields   uuuu uuHG FMMM CCCC PPPP TTTT TTTT RRRR
#  WarrantyVoidNew/| |Mem Manu Proc ModelName PCB
#   WarrantyVoidOld/ |Siz fact                Rev
#          EncodedFlag
# 
#   bits  contains        values
# R 00-03
          PCBRevision=('0' '1' '2' '3' '4' '5' '6' '7' '8' '9' '10' '11' '12' '13' '14' '15')
# T 04-11
          ModelName=('A' 'B' 'A+' 'B+' 'Pi2B' 'Alpha' 'CM1' 'unknown' 'Pi3B' 'Zero' 'CM3' 'unknown' 'Zero W' 'Pi3B+' 'Pi3A+' 'internal use only' 'CM3+' '4B')
# P 12-15
          Processor=('BCM2835' 'BCM2836' 'BCM2837' 'BCM2711')
# C 16-19
          Manufacturer=('Sony UK' 'Egoman' 'Embest' 'Sony Japan' 'Embest' 'Stadium')
# M 20-22
          MemorySize=('256 MB' '512 MB' '1 GB' '2 GB' '4 GB' '8 GB')
# F 23-23
          EncodedFlag=('' 'revision is a encoded bit field')
# G 24-24
          WarrantyVoidOld=('' 'warranty void - Pre Pi2')
# H 25-25
          WarrantyVoidNew=('' 'warranty void - Post Pi2')
# u 26-31 unused
#

tool_dir=`dirname $0`
cd ${tool_dir}

Hardware=$(cat /proc/cpuinfo | grep 'Hardware' | awk '{print $3}')
Revision=$(cat /proc/cpuinfo | grep 'Revision' | awk '{print $3}')
rev=$(echo $Revision | sed 's/^1000//')
echo "Revision        : "$Revision
#echo "rev=$rev"
Serial=$(cat /proc/cpuinfo|grep 'Serial'|awk '{print $3}')
echo "Serial          : "$Serial
MACs=$(ifconfig | grep ether | awk '{print $2}')
echo "MAC address(es) : "$MACs
Encoded=$((0x$Revision >> 23 & 1))

if [ $Encoded = 1 ]; then
  echo 'ModelName       : '${ModelName[$((0x$Revision>>4&0xff))]}
  echo 'PCBRevision     : '$((0x$Revision&0xf))
  echo 'MemorySize      : '${MemorySize[$((0x$Revision>>20&7))]}
  echo 'Manufacturer    : '${Manufacturer[$((0x$Revision>>16&0xf))]}
  echo 'Processor       : '${Processor[$((0x$Revision>>12&0xf))]}' (given by documentation)'
  if [ $((0x$Revision>>23&1)) = 1 ]; then
    echo 'EncodedFlag     : '${EncodedFlag[1]}
  fi
  if [ $((0x$Revision>>24&1)) = 1 ]; then
    echo 'WarrantyVoidOld : '${WarrantyVoidOld[1]}
  fi
  if [ $((0x$Revision>>25&1)) = 1 ]; then
    echo 'WarrantyVoidNew : '${WarrantyVoidNew[1]}
  fi
else
  echo "Old model where the revision does not provide encoded information"
fi
echo

awk -F\; -v rev=$rev '{
  if (NR<=5) {
    split($0,hd,";")
  }
  if ($1~rev) {
    for (i=1;i<=NF;i++) {
      printf"%-16s: %s\n",hd[i],$i
    }
  }
}' raspberry_hardware_versions.csv 
echo 'Processor       : '${Hardware}' (given by /proc/cpuinfo)'
echo

