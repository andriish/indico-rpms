## Upgrade: 
1) Install everything
```
dnf -y copr enable averbyts/IR
dnf -y install  indico- ...
```
2) Edit configs /etc/indico.conf to setup passwords
```
systemctl restart httpd.service indico-celery.service indico-uwsgi.service
```

3) Copy the information
DB treatment
-  stop redis.
-  drop db
-  create db
-  import dump
-  indico db upgrade


# export OLD=
# export NEW=

#@ OLD su indico  pg_dump indico > indico_dump.txt
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
