#!/bin/sh

infos_file=/tmp/infos.txt
cat << EOF > ${infos_file}
0:all:all information:
1:measure_clock:clock frequency:arm core h264 isp v3d uart pwm emmc pixel vec hdmi dpi
2:measure_volts:sdram voltage:core sdram_c sdram_i sdram_p
3:measure_temp:temperature of BCM2835 SoC:
4:codec_enabled:enabled codec:H264 MPG2 WVC1 MPG4 MJPG WMV9
5:get_config:Raspberry configuration:
6:get_mem:CPU and GPU memory:arm gpu
7:version:firmware version:
8:otp_dump:contents of the OTP memory:
9:get_lcd_info:display framebuffer:
EOF

min_opt=`head -n 1 ${infos_file} | cut -d: -f1`
max_opt=`tail -n 1 ${infos_file} | cut -d: -f1`

menu=3
if [ "$1" = "" ]; then
  echo "Choose an option:"
  awk -F: '{printf"%2s: %s\n",$1,$3}' ${infos_file}
  read rep
  [ "${rep}" = "" ] && exit 0
  expr ${rep} + 0 > /dev/null 2>&1
  if [ $? != 0 ]; then
    echo "The answer is not a number"
    exit 1
  fi
  menu=${rep}
else
  menu=$1
fi

if [ ${menu} -lt ${min_opt} -o ${menu} -gt ${max_opt} ]; then
  echo "The chosen option should be between ${min_opt} and ${max_opt}"
  exit 1
fi


get_info() {
  num_line=`expr $1 + 1`
  command=`head -n ${num_line} ${infos_file} | tail -n 1 | cut -d: -f2`
  args=`head -n ${num_line} ${infos_file} | tail -n 1 | cut -d: -f4`
  head -n ${num_line} ${infos_file} | tail -n 1 | cut -d: -f3
  if [ "${args}" = "" ]; then
    vcgencmd ${command}
  else
    for arg in ${args}; do
      echo "${arg}:\t$(vcgencmd ${command} ${arg})"
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


