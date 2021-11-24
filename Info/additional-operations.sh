#!/bin/sh

echo === Add alias ll
sed -i "/alias ll/s/^#//" ~/.bashrc

echo
echo === Add WIFI configuration
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
  echo "Please neter the password for Wifi ${chosen_wifi}"
  read wifi_pwd

  wfile=/etc/wpa_supplicant/wpa_supplicant.conf
  sudo grep -q "ssid=.${chosen_wifi}" ${wfile}
  if [ $? != 0 ]; then
    cat << EOF | sudo tee -a ${wfile}
network={
    ssid="${chosen_wifi}"
    psk="${wifi_pwd}"
}
EOF
  fi
fi

echo
echo === Add some packages
list="python3-pip git python3-dev sshpass byobu"
sudo apt-get install ${list}

rasp_dev_dir=Raspberry_dev
echo
echo === Add ${rasp_dev_dir} git project
if [ ! -d ~/${rasp_dev_dir} ]; then
  cd
  git clone https://github.com/remilap/${rasp_dev_dir}.git
fi

echo
echo === Configure git
git config --global user.email "remi.lapointe@gmail.com"
git config --global user.name "remilap"
git config --global core.editor "vi"
git config --global push.default "simple"

echo
echo === Gener ssh key
ssh_dir=~/.ssh
ssh_rsa_file=${ssh_dir}/id_rsa
ssh_rsa_pub_file=${ssh_rsa_file}.pub
ssh_auth_file=${ssh_dir}/authorized_keys
if [ ! -f ${ssh_rsa_file} ]; then
  ssh-keygen -b 2048 -t rsa
  touch ${ssh_auth_file}
  #cat ~/.ssh/id_rsa.pub | ssh -p 22 pi@192.168.1.21 'cat >> .ssh/authorized_keys'
  chmod 700 ${ssh_dir}
  chmod 600 ${ssh_auth_file}
fi

public_IP=$(curl ifconfig.me)
hosts_file=/etc/hosts
if [ "${public_IP}" = "88.164.35.239" ]; then
  echo
  echo === Configure ${hosts_file} for Nantes
  grep -q rasp03 ${hosts_file}
  if [ $? != 0 ]; then
    cat << EOF | sudo tee -a ${hosts_file}
192.168.0.23    rasp03
192.168.0.25    rasp05
192.168.0.26    rasp06
192.168.0.27    rasp07
EOF
  fi
fi

if [ "$public_IP" = "77.192.99.60" ]; then
  echo
  echo === Configure ${hosts_file} for Perros
  grep -q rasp02 ${hosts_file}
  if [ $? != 0 ]; then
    cat << EOF | sudo tee -a ${hosts_file}
192.168.1.21    rasp01
192.168.1.22    rasp02
EOF
  fi
fi

echo
echo === Add symbolic links
ln -sf ~/${rasp_dev_dir}/Info/get_external_IP.sh ~/get_external_IP.sh 
ln -sf ~/${rasp_dev_dir}/Camera/cleanup.sh ~/cleanup.sh 
ln -sf ~/${rasp_dev_dir}/Camera/get_image.sh ~/get_image.sh 
[ "`hostname`" = "rasp01" ] && ln -sf ~/${rasp_dev_dir}/rasp01/retrTempFrom.sh ~/retrTempFrom.sh

