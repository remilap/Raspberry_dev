#!/bin/sh
#
# See https://raspberry-pi.fr/installer-serveur-web-raspberry-lamp/
# https://httpd.apache.org/docs/2.4/fr/howto/cgi.html
# https://httpd.apache.org/docs/2.4/fr/howto/auth.html
# https://ardamis.com/2008/05/26/a-php-script-for-testing-a-mysql-database-connection/
#


step() {
  echo $1 > install_step.txt
  shift
  echo "===== $* ====="
}

htmlDir=/var/www/html/
apache_conf_dir=/etc/apache2

step 1 Update the Linux system
sudo apt update
[ $? = 0 ] || exit 1
sudo apt upgrade
[ $? = 0 ] || exit 1

step 2 Install apache2
sudo apt install apache2
[ $? = 0 ] || exit 1

[ -d $htmlDir ] || exit 1
step 3 Configure html directory ($htmlDir)
sudo chown -R pi:www-data $htmlDir
sudo chmod -R 770 $htmlDir

step 4 Check if apache2 is well installed
wget -O verif_apache.html http://127.0.0.1
[ $? = 0 ] || exit 1

step 5 Install php
sudo apt install php php-mbstring
[ $? = 0 ] || exit 1

step 6 Install MySQL
sudo apt install mariadb-server php-mysql
[ $? = 0 ] || exit 1

step 7 Configure MySQL root password
cat << EOF | sudo mysql --user=root
DROP USER 'root'@'localhost';
CREATE USER 'root'@'localhost' IDENTIFIED BY 'rem000';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
EOF
[ $? = 0 ] || exit 1

step 8 Install phpmyadmin
sudo apt install phpmyadmin
[ $? = 0 ] || exit 1

step 9 Configure mysqli extension
sudo phpenmod mysqli
[ $? = 0 ] || exit 1
sudo ln -s /usr/share/phpmyadmin $htmlDir/phpmyadmin
[ $? = 0 ] || exit 1
#sudo service apache2 restart (will be done below)
#[ $? = 0 ] || exit 1

step 10 Install mod_perl
sudo apt install libapache2-mod-perl2
[ $? = 0 ] || exit 1

step 11 Configure cgi and perl scripts
cd $apache_conf_dir/mods-enabled
sudo ln -s ../mods-available/cgid.conf .
[ $? = 0 ] || exit 1
sudo ln -s ../mods-available/cgid.load .
[ $? = 0 ] || exit 1
sudo ln -s ../mods-available/perl.load .
[ $? = 0 ] || exit 1

step 12 Configure restrict access
sudo cp apache2.conf $apache_conf_dir
[ $? = 0 ] || exit 1
cp .htaccess $htmlDir
[ $? = 0 ] || exit 1
mkdir -p $htmlDir/admin
[ $? = 0 ] || exit 1
cp .main.htpasswd $htmlDir/admin/
[ $? = 0 ] || exit 1
sudo service apache2 restart
[ $? = 0 ] || exit 1

