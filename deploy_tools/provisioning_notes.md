Provisioning a new website with Django
======================================

## Required Packages
* nginx
* python 3
* git
* virtualenv

eg on obuntu 
* sudo apt-get install nginx python3 python3-pip
* sudo pip3 install virtualenv

For purposes of following examples in book i used a custom-built version of python (3.4) and specified that when creating the virtualenv's

## Nginx virtual host config
* see nginx.template.conf
* replace SITENAME token with superliststaging.ca for eg.

## Systemd startup script for gunicorn
* see gunicorn_systemd_startup.template.conf
* replace SITENAME token
* Commands to register systemd startup scripts for gunicorn python http servers:
$ sudo systemctl enable gunicorn_superliststaging.ca
$ sudo systemctl enable gunicorn_superlistlive.ca


## folder structure
/home
  L /username
      L /sites
          L /SITENAME 
              L database 
              L source 
              L static
              L virtualenv

