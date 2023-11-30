#!/bin/bash
#https://linux.how2shout.com/how-to-install-vsftpd-to-setup-ftp-server-on-ubuntu-22-04/
USER=deivit

# Update the package index and install essential packages
sudo apt update -y
sudo apt install -y vsftpd joe

# Create the user and the ftp directory
sudo adduser --disabled-password --gecos "" $USER
sudo mkdir -p /home/$USER/ftp/upload
sudo chown -R $USER:$USER /home/$USER/ftp

sudo mkdir -p /home/$USER/.ssh
sudo chown -R $USER:$USER /home/$USER/.ssh


sudo chmod a-w /home/$USER/ftp
sudo mv /tmp/vsftpd.conf /etc/vsftpd.conf
sudo cat /tmp/vagrant.pub >> /home/$USER/.ssh/authorized_keys

# Add the user to the userlist file
echo "$USER" | sudo tee -a /etc/vsftpd.userlist

# Allow the FTP ports in the firewall
sudo ufw allow 20,21,990,30000:31000/tcp

# Restart the vsftpd service
sudo systemctl restart vsftpd
