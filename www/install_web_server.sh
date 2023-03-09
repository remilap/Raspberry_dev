#!/bin/sh
#
# See https://raspberry-pi.fr/installer-serveur-web-raspberry-lamp/
# https://httpd.apache.org/docs/2.4/fr/howto/cgi.html
# https://httpd.apache.org/docs/2.4/fr/howto/auth.html
# https://ardamis.com/2008/05/26/a-php-script-for-testing-a-mysql-database-connection/
#


htmlDir=/var/www/html/
apache_conf_dir=/etc/apache2
step_file=~/install_step.txt

step() {
  echo $1 > ${step_file}
  echo
  echo "===== step $* ====="
  echo
}

step=0
if [ -f ${step_file} ]; then
  echo step_file
  step=`cat ${step_file}`
  echo "Start again at step ${step} (Y/N) ?"
  read ans
  [ "${ans}" = "" -o "${ans}" = "y" -o "${ans}" = "o" -o "${ans}" = "O" ] && ans="Y"
  [ "${ans}" != "Y" ] && exit
fi

if [ ${step} -le 1 ]; then
  step 1 Update the Linux system
  sudo apt update -y
  [ $? = 0 ] || exit 1
  sudo apt upgrade -y
  [ $? = 0 ] || exit 1
fi

if [ ${step} -le 2 ]; then
  step 2 Install apache2
  sudo apt install apache2 -y
  [ $? = 0 ] || exit 1
  [ -d ${htmlDir} ] || exit 1
fi

if [ ${step} -le 3 ]; then
  step 3 Configure html directory ${htmlDir}
  sudo chown -R pi:www-data ${htmlDir}
  sudo chmod -R 770 ${htmlDir}
fi

if [ ${step} -le 4 ]; then
  step 4 Check if apache2 is well installed
  wget -O verif_apache.html http://127.0.0.1
  [ $? = 0 ] || exit 1
fi

if [ ${step} -le 5 ]; then
  step 5 Install php
  sudo apt install php php-mbstring -y
  [ $? = 0 ] || exit 1
fi

if [ ${step} -le 6 ]; then
  step 6 Install MySQL
  sudo apt install mariadb-server php-mysql -y
  [ $? = 0 ] || exit 1
fi

if [ ${step} -le 7 ]; then
  step 7 Configure MySQL root password
  cat << EOF | sudo mysql --user=root
DROP USER 'root'@'localhost';
CREATE USER 'root'@'localhost' IDENTIFIED BY 'rem000';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
EOF
  [ $? = 0 ] || exit 1
fi

if [ ${step} -le 8 ]; then
  step 8 Install phpmyadmin
  sudo apt install phpmyadmin -y
  [ $? = 0 ] || exit 1
fi

if [ ${step} -le 9 ]; then
  step 9 Configure mysqli extension
  sudo phpenmod mysqli
  [ $? = 0 ] || exit 1
  sudo ln -s /usr/share/phpmyadmin ${htmlDir}/phpmyadmin
  [ $? = 0 ] || exit 1
  #sudo service apache2 restart (will be done below)
  #[ $? = 0 ] || exit 1
fi

if [ ${step} -le 10 ]; then
  step 10 Install mod_perl
  sudo apt install libapache2-mod-perl2 -y
  [ $? = 0 ] || exit 1
fi

if [ ${step} -le 11 ]; then
  step 11 Configure cgi and perl scripts
  cd ${apache_conf_dir}/mods-enabled
  sudo ln -s ../mods-available/cgid.conf .
  [ $? = 0 ] || exit 1
  sudo ln -s ../mods-available/cgid.load .
  [ $? = 0 ] || exit 1
  sudo ln -s ../mods-available/perl.load .
  [ $? = 0 ] || exit 1
fi

if [ ${step} -le 12 ]; then
  step 12 Configure restrict access
  sudo cp apache2.conf ${apache_conf_dir}
  [ $? = 0 ] || exit 1
  cp .htaccess ${htmlDir}
  [ $? = 0 ] || exit 1
  mkdir -p ${htmlDir}/admin
  [ $? = 0 ] || exit 1
  cp .main.htpasswd ${htmlDir}/admin/
  [ $? = 0 ] || exit 1
  sudo service apache2 restart
  [ $? = 0 ] || exit 1
fi

rm -f ${step_file}

