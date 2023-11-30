#!/bin/bash
#jdbc:mysql://192.168.1.235:3306/dbname?allowPublicKeyRetrieval=true&useSSL=false
# Set database credentials
DBHOST="localhost"
DBNAME="dbname"
DBUSER="dbuser"
DBPASSWD="userpass"
MYSQL_USER="root"

# Update the package index
sudo apt update

# Install essential packages
sudo apt install vim curl build-essential python3-software-properties git joe

# Set MySQL root password and security options
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password $DBPASSWD"
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $DBPASSWD"
sudo apt install -y mysql-server
sudo systemctl start mysql.service

mysql -u$MYSQL_USER -p$DBPASSWD -e "CREATE DATABASE $DBNAME;"
mysql -u$MYSQL_USER -p$DBPASSWD -e "CREATE USER '$DBUSER'@'%' IDENTIFIED BY '$DBPASSWD';"
mysql -u$MYSQL_USER -p$DBPASSWD -e "GRANT ALL PRIVILEGES ON $DBNAME.* TO '$DBUSER'@'%' WITH GRANT OPTION;"
mysql -u$MYSQL_USER -p$DBPASSWD -e "FLUSH PRIVILEGES"
sudo sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/g" /etc/mysql/mysql.conf.d/mysqld.cnf
sudo service mysql restart