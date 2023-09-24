#!/bin/bash

###################################################################
# API for retrieving Mpjpeg URLs from NX server.                  #                                                                                                                                                                                     
# Author: JL                                                      #                            
###################################################################

sudo apt update
echo
if [ $(dpkg-query -W -f='${Status}' python3-pip 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo
  echo "###################################################################"
  echo "Installing Python3"
  echo "###################################################################"
  echo
  sudo apt-get -y install python3-pip;
fi
echo
if [ $(dpkg-query -W -f='${Status}' wget 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo
  echo "###################################################################"
  echo "Installing Wget"
  echo "###################################################################"
  echo
  sudo apt install wget;
fi
echo
echo
echo "###################################################################"
echo "Installing Flask"
echo "###################################################################"
echo
sudo pip3 install flask
echo
echo
echo "###################################################################"
echo "Installing Application"
echo "###################################################################"
echo
mkdir /opt/nxurl
mkdir /opt/nxurl/templates

wget -P /opt/nxurl https://raw.githubusercontent.com/leenperjasknegt/mpjpegcloudurl/main/url.py
wget -P /opt/nxurl/templates https://raw.githubusercontent.com/leenperjasknegt/mpjpegcloudurl/main/templates/index.html
wget -P /opt/nxurl/templates https://raw.githubusercontent.com/leenperjasknegt/mpjpegcloudurl/main/templates/urls.html

python3 /opt/nxurl/url.py
