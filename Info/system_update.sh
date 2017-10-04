#!/bin/sh
################################################################################
# 
#-------------------------------------------------------------------------------
# HISTORY:
# 2017-09-04 - R. Lapointe    - Inverse upgrade and dist-upgrade
# 2017-10-04 3 R. Lapointe    - Group all apt-get commands in a list and add purge-old-kernels
################################################################################

cmd_list="update dist-upgrade upgrade autoremove clean"
for cmd in ${cmd_list}; do
  echo "===== sudo apt-get ${cmd}"
  sudo apt-get ${cmd}
done

sudo purge-old-kernels --keep 2

