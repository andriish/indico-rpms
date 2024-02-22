#!bin/bash

export PATH=$PATH:$(pwd)

set -x 
declare -a BUILDLIST=(
indico-mpp:3.2
python-indico:3.2.9
indico-devel:3.2.9
python-Flask-Limiter:3.5.0
python-Flask-Multipass:0.5.3
python-Flask-PluginEngine:0.5
python-PyPDF2:2.11.0
python-WTForms-dateutil:0.1
python-captcha:0.5.0
python-email_validator:1.2.1
python-flask-marshmallow:0.15.0
python-flask-url-map-serializer:0.1.0
python-flask-webpackext:1.0.2
python-hiredis:2.3.2
python-indico-fonts:1.2
python-iso_4217:0.4.220401
python-marshmallow_oneofschema:3.0.1
python-marshmallow_sqlalchemy:0.29.0
python-marshmallow-dataclass:8.6.0
python-pynpm:0.2.0
python-pywebpack:1.2.0
python-webargs:8.3.0
)

for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
mkdir -p  logs
(sh srpmsbuild.sh $p $v --build  &> logs/$p$v".log" || echo "$p $v build failed" &)
done
wait
exit
