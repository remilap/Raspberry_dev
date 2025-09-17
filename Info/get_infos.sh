#!/bin/bash
#
# infos from https://elinux.org/RPI_vcgencmd_usage
# and https://www.raspberrypi.com/documentation/computers/os.html
#

infos_file=/tmp/infos.txt
cat << EOF > ${infos_file}
all:all information:
vcgencmd measure_clock:clock frequency:arm core h264 isp v3d uart pwm emmc pixel vec hdmi dpi
vcgencmd measure_volts:sdram voltage:core sdram_c sdram_i sdram_p
vcgencmd measure_temp:temperature of processor SoC:
vcgencmd codec_enabled:enabled codec:H263 H264 MPG2 WVC1 MPG4 AGIF MJPA MJPB MJPG WMV9 MVC0
vcgencmd bootloader_config:bootloader configuration:
vcgencmd bootloader_version:bootloader version:
vcgencmd get_config:Raspberry configuration:int str
vcgencmd get_mem:CPU and GPU memory:arm gpu
vcgencmd get_rsts:restart status:
vcgencmd get_throttled:throttled state of the system:
vcgencmd version:firmware version:
vcgencmd otp_dump:contents of the OTP memory:
vcgencmd get_lcd_info:display framebuffer:
vcgencmd get_camera:camera information:
vcgencmd power_monitor:unknown option:
vcgencmd hdmi_status_show:HDMI status:
vcgencmd hdmi_ntsc_freqs:HDMI NTSC frequency
vcgencmd pm_get_status:pm get status:
vcgencmd mem_oom:Out Of Memory:
cat /proc/cpuinfo:CPU information:
cat /proc/version:OS version:
cat /etc/os-release:OS release:
lsb_release -a:Linux Standard Base information:
hostnamectl:Operating System version:
cat /etc/issue:OS version from /etc/issue:
uname -a:system information:
cat /proc/meminfo:memory information:
free -h:memory information summary:
vcgencmd vcos log status:some system log status:
EOF

min_opt=0
max_opt=`wc -l ${infos_file} | awk '{print $1}'`

myexit() {
  rm -f ${infos_file} 2> /dev/null
  exit $1
}

menu=3
if [ "$1" = "" ]; then
  echo "Choose an option:"
  awk -F: 'BEGIN {n=0} {printf"%2s: %s\n",n++,$2}' ${infos_file}
  read rep
  [ "${rep}" = "" ] && myexit 0
  expr ${rep} + 1 > /dev/null 2>&1
  if [ $? != 0 ]; then
    echo "The answer is not a number"
    myexit 1
  fi
  menu=${rep}
else
  menu=$1
fi

if [ ${menu} -lt ${min_opt} -o ${menu} -gt ${max_opt} ]; then
  echo "The chosen option should be between ${min_opt} and ${max_opt}"
  myexit 1
fi


get_info() {
  num_line=`expr $1 + 1`
  command=`head -n ${num_line} ${infos_file} | tail -n 1 | cut -d: -f1`
  args=`head -n ${num_line} ${infos_file} | tail -n 1 | cut -d: -f3`
  head -n ${num_line} ${infos_file} | tail -n 1 | cut -d: -f2
echo "===TRACE=== command=${command}, args=${args}"
  if [ "${args}" = "" ]; then
    ${command}
  else
    for arg in ${args}; do
      echo "${arg}:"
      ${command} ${arg}
      echo "---"
      echo
    done
  fi
  echo
}

if [ ${menu} = 0 ]; then
  min_opt=1
  for i in `seq ${min_opt} ${max_opt}`; do
    get_info ${i}
  done
else
  get_info ${menu}
fi


