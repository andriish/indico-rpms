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

systemctl stop redis.service
systemctl stop httpd.service indico-celery.service indico-uwsgi.service
su - postgres -c 'psql -c "drop database indico;"'
su - postgres -c 'createdb -O indico indico'
su - postgres -c 'psql indico < indico_dump.txt'
su - indico   -c 'indico db upgrade'
systemctl start redis.service

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


```
dnf -y install dnf-plu*
dnf -y copr enable averbyts/I330
rpm -e $(rpm -qa | grep indico)  $(rpm -qa | grep postgresql) 
yum clean all
rm -rf /opt/indico/ /opt/pgsql/
yum -y install python3-indico-mpp-configuration
sed -i 's/indico01/indico04/g' /opt/indico/etc/indico.conf 
sed -i 's/indico01/indico04/g' /etc/httpd/conf.d/indico.conf 
su  indico 
bash-5.2$ indico user create -a
....
systemctl restart httpd.service postgresql.service redis.service indico-celery.service indico-uwsgi.service
```

Fix postfix   mydestination =



#( drbdadm status to see it's status)
modprobe drbd
drbdadm up r0
drbdadm primary r0

mount /dev/drbd0 /opt

and back
umount /opt
drbdadm down r0








systemctl stop redis.service
systemctl stop httpd.service indico-celery.service indico-uwsgi.service
su - postgres -c 'createuser indico'
sleep 1
su - postgres -c 'createdb -O indico indico'
sleep 1
su - postgres -c 'psql indico -c "CREATE EXTENSION unaccent; CREATE EXTENSION pg_trgm;"'
sleep 1
su - indico -c 'indico db prepare'
sleep 1
su - postgres -c 'psql -c "drop database indico;"'
sleep 1
su - postgres -c 'createdb -O indico indico'
sleep 1
su - postgres -c 'psql indico < /opt/fromindico01/indico_dump_08032024.txt'
sleep 1
su - indico   -c 'indico db upgrade'
systemctl start redis.service
systemctl restart httpd.service postgresql.service redis.service indico-celery.service indico-uwsgi.service


cat /usr/lib/systemd/system/postgresql.service
/etc/systemd/system/postgresql.service.d/indicopostgresql.conf

tail  /opt/pgsql/data/log/postgresql-Sat.log  -n 200






systemctl stop redis.service
systemctl stop httpd.service indico-celery.service indico-uwsgi.service
systemctl daemon-reload
systemctl restart httpd.service postgresql.service redis.service indico-celery.service indico-uwsgi.service

