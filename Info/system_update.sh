#!/bin/sh
################################################################################
# 
#-------------------------------------------------------------------------------
# HISTORY:
# 2017-09-04 - R. Lapointe    - Inverse upgrade and dist-upgrade
# 2017-10-04 - R. Lapointe    - Group all apt-get commands in a list and add purge-old-kernels
# 2017-10-05 - R. Lapointe    - Add option -y for avoiding tasks to be blocked
# 2017-10-05 - R. Lapointe    - Remove purge-old-kernels command (not found)
################################################################################

cmd_list="update dist-upgrade upgrade autoremove clean"
for cmd in ${cmd_list}; do
  echo "===== sudo apt-get ${cmd}"
  sudo apt-get -y ${cmd}
done

