#!/bin/sh

NB_DAYS_TO_KEEP=3
if [ "$1" != "" ]; then
  expr $1 + 0 > /dev/null 2>&1
  if [ $? = 0 ]; then
    if [ $1 -gt 2 -a $1 -lt 20 ]; then
      NB_DAYS_TO_KEEP=$1
    fi
  fi
fi
destDir=/var/www/html/motion
destDir=/var/www/html/maison
dat=`date +"%Y-%m-%d %T"`
echo "----------------------------------------------------------------"
echo "Today: ${dat}"

filesList=`find -H ${destDir} -daystart -mtime +${NB_DAYS_TO_KEEP}`
if [ "${filesList}" = "" ]; then
  echo "${dat} No file to remove"
  exit 0
fi

for f in ${filesList}; do
  echo "${dat} File to remove: ${f}"
  sudo rm ${f}
done

