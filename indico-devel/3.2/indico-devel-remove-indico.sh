#!/bin/bash
systemctl stop httpd.service postgresql.service redis.service indico-celery.service indico-uwsgi.service
systemctl disable indico-celery.service indico-uwsgi.service
rpm -e $(rpm -qa | grep indico)
systemctl restart httpd.service postgresql.service redis.service
