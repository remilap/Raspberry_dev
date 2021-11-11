#!/bin/sh
################################################################################
# 
#-------------------------------------------------------------------------------
# HISTORY:
# 2017-09-04 - R. Lapointe    - Inverse upgrade and dist-upgrade
# 2017-10-04 - R. Lapointe    - Group all apt-get commands in a list and add purge-old-kernels
# 2017-10-05 - R. Lapointe    - Add option -y for avoiding tasks to be blocked
# 2017-10-05 - R. Lapointe    - Remove purge-old-kernels command (not found)
# 2021-08-24 - R. Lapointe    - Replace apt-get by apt
# 2021-08-24 - R. Lapointe    - Manage the OS upgrade to Debian buster
# 2021-11-09 - R. Lapointe    - Manage the OS upgrade to Debian bullseye
################################################################################

sfile=/etc/apt/sources.list
rel="bullseye"
cur=$(grep "^deb.*raspbian" $sfile | awk '{print $3}')
if [ "$cur" = "" ]; then
  echo "===== ERROR: unable to find the current version of Debian"
  echo "please see current content of $sfile"
  cat $sfile
  exit 1
fi
echo "===== Current Debian version is $cur"

if [ "$cur" != "$rel" ]; then
  echo "===== Upgrade Debian version from $cur to $rel"
  find /etc/apt -type f -exec grep $cur {} \; -exec sudo sed -i s/$cur/$rel/ {} \; -print
fi

cmd_list="update dist-upgrade upgrade autoremove clean"
for cmd in ${cmd_list}; do
  echo "===== sudo apt ${cmd}"
  sudo apt -y ${cmd}
done

