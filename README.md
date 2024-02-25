# indico-rpms
RPMS for Indico


To install:

```
yum install indico-mpp indico-devel python3-indico
```

After the installation, as root:

```
su  indico 
bash-5.2$ indico user create
Email: 
First name: 
Last name: 
Affiliation []: 

Enter username: 
Password: 
Repeat for confirmation: 
User info:
  ID: 1
  First name: 
  Family name: 
  Email: 
  Affiliation: 

Create the new user? [Y/n]: Y
New user created successfully with ID: 1
bash-5.2$ indico  user grant-admin 1
User info:
  ID: 1
  First name: 
  Family name: 
  Email: 
  Affiliation: 

Grant administration rights to this user? [y/N]: y
Administration rights granted successfully
bash-5.2$ 
```

To run

```
/usr/bin/indico-devel-start-indico.sh
```








# Plan for the upgrade: 
# 1) Install everything
#  dnf -y copr enable averbyts/IR
#  dnf -y install  indico-mpp
# 2) Edit configs /etc/indico.conf to setup passwords
#    systemctl restart httpd.service indico-celery.service indico-uwsgi.service

# 3) Copy the information
#DB treatment
# stop redis.
# drop db
# create db
# import dump
# indico db upgrade


# export OLD=
# export NEW=

#@ OLD  pg_dump indico > indico_dump.txt
#@ OLD scp /mnt/home/indico/indico/indico_dump.txt $NEW:

#systemctl stop redis.service
#systemctl stop httpd.service indico-celery.service indico-uwsgi.service
#su - postgres  psql -c "drop database indico;"
#su - postgres  createdb -O indico indico
#su - postgres  psql indico < indico_dump.txt
#su - indico    indico db upgrade
#systemctl start redis.service

#scp -r $OLD:/mnt/home/indico/indico/archive ./A
#mv ./A/* /opt/indico/archive/
#chown indico -R /opt/indico/archive/ 
#chgrp apache -R /opt/indico/archive/
#mkdir -p /opt/indico/indico-legacy/

#scp -r $OLD:/mnt/home/indico/indico-legacy/archive  ./B
#mv ./B/* /opt/indico/indico-legacy/
#chown indico -R /opt/indico/indico-legacy/
#chgrp apache -R /opt/indico/indico-legacy/

#PACEMAKER:
#systemctl stop pacemaker
#rm -rf  /opt/pgsql* /opt/indico
#rpm -e $(rpm -qa | grep postgresql) indico-mpp python3-indico --nodeps
#yum install  postgresql-server -y postgresql
#yum -y install python3-indico
#yum -y install indico-mpp
#edit /etc/httpd/conf/httpd.conf!!!!!



