#!/bin/sh
#
# See https://raspberry-pi.fr/installer-serveur-web-raspberry-lamp/
# https://httpd.apache.org/docs/2.4/fr/howto/cgi.html
# https://ardamis.com/2008/05/26/a-php-script-for-testing-a-mysql-database-connection/
#


step() {
  echo $1 > install_step.txt
  shift
  echo "===== $* ====="
}

step 1 Update the Linux system
sudo apt update
[ $? = 0 ] || exit 1
step 2 Upgrade the Linux system
sudo apt upgrade
[ $? = 0 ] || exit 1
step 3 Update the Linux system
sudo apt update
[ $? = 0 ] || exit 1

step 4 Install apache2
sudo apt install apache2
[ $? = 0 ] || exit 1

htmlDir=/var/www/html/
[ -d $htmlDir ] || exit 1
step 5 Configure html directory ($htmlDir)
sudo chown -R pi:www-data $htmlDir
sudo chmod -R 770 $htmlDir

step 6 Check if apache2 is well installed
wget -O verif_apache.html http://127.0.0.1
[ $? = 0 ] || exit 1

step 7 Install php
sudo apt install php php-mbstring
[ $? = 0 ] || exit 1

step 8 Install MySQL
sudo apt install mariadb-server php-mysql
[ $? = 0 ] || exit 1

step 9 Configure MySQL root password
cat << EOF | sudo mysql --user=root
DROP USER 'root'@'localhost';
CREATE USER 'root'@'localhost' IDENTIFIED BY 'rem000';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
EOF
[ $? = 0 ] || exit 1

step 10 Install phpmyadmin
sudo apt install phpmyadmin
[ $? = 0 ] || exit 1

step 11 Configure mysqli extension
sudo phpenmod mysqli
[ $? = 0 ] || exit 1
sudo /etc/init.d/apache2 restart
[ $? = 0 ] || exit 1
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin
[ $? = 0 ] || exit 1

step 12 Install mod_perl
sudo apt install libapache2-mod-perl2
[ $? = 0 ] || exit 1

step 13 Configure cgi and perl scripts
cd /etc/apache2/mods-enabled
sudo ln -s ../mods-available/cgid.conf .
[ $? = 0 ] || exit 1
sudo ln -s ../mods-available/cgid.load .
[ $? = 0 ] || exit 1
sudo ln -s ../mods-available/perl.load .
[ $? = 0 ] || exit 1


