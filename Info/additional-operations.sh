#!/bin/sh

# Add alias ll
sed -i "/alias ll/s/^#//" ~/.bashrc

# Add WIFI configuration
wifi_file=~/wifi_scan.txt
sudo iwlist wlan0 scan | grep ESSID | cut -d\" -f2 > ${wifi_file}
nbl=`wc -l ${wifi_file} | awk '{print $1}'`
rc=1
while [ ${rc} = 1 ]; do
  awk '{i++;printf"%2d: %s\n",i,$0}' ${wifi_file}
  echo "Choose the Wifi network number:"
  read r
  if [ "${r}" != "" ]; then
    res=`echo "${r}" | tr -d [0-9]`
    if [ "${res}" != "" ]; then
      echo "Your answer >${r}< must be a numeric value, please retry"
      continue
    fi
    if [ ${r} -lt 1 -o ${r} -gt ${nbl} ]; then
      echo "Your answer >${r}< must be in the range [1-${nbl}], please retry"
      continue
    fi
  fi
  rc=0
done
if [ "${r}" = "" ]; then
  echo "No configuration of Wifi"
else

  chosen_wifi="SFR_70D0"
  wifi_pwd="pij86fqux5buq22pcxs3"

  chosen_wifi=`awk -v r=${r} '{if(NR==r)print}' ${wifi_file}`
  read wifi_pwd

  wfile=/etc/wpa_supplicant/wpa_supplicant.conf
  sudo grep -q "ssid=.${chosen_wifi}" ${wfile}
  if [ $? != 0 ]; then
    sudo cat << EOF >> ${wfile}
network={
    ssid="${chosen_wifi}"
    psk="${wifi_pwd}"
}
EOF
  fi
fi

# Add Raspberry_dev git project
if [ ! -d ~/Raspberry_dev ]; then
  cd
  git clone https://github.com/remilap/Raspberry_dev.git
fi

# Gener ssh key
if [ ! -f ~/.ssh/id_rsa ]; then
  ssh-keygen -b 2048 -t rsa
  cat ~/.ssh/id_rsa.pub | ssh -p 22 pi@192.168.1.21 'cat >> .ssh/authorized_keys'
  chmod 700 ~/.ssh/
  chmod 600 ~/.ssh/authorized_keys
fi

# Add symbolic links
ln -sf ~/Raspberry_dev/Info/get_external_IP.sh ~/get_external_IP.sh 

# Add some packages
list="python-pip git python-dev sshpass byobu"

