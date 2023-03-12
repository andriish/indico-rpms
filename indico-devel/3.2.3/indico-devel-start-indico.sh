#!/bin/bash
systemctl restart httpd.service postgresql.service redis.service indico-celery.service indico-uwsgi.service
