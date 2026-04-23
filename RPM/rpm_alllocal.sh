#!bin/bash

export PATH=$PATH:$(pwd)
set -x 
declare -a BUILDLIST=(
python-wallet-py3k:0.0.4
python-limits:5.8.0
python-flask-limiter:3.12
python-flask-multipass:0.11.2
python-flask-pluginengine:0.5
python-wtforms-dateutil:0.1
python-captcha:0.7.1
python-flask-marshmallow:1.4.0
python-flask-url-map-serializer:0.1.0
python-iso4217:1.16
python-marshmallow-oneofschema:3.2.0
python-marshmallow-sqlalchemy:1.4.2
python-marshmallow-dataclass:8.7.1
python-pynpm:0.3.0
python-pywebpack:2.2.1
python-flask-webpackext:2.1.0
python-webargs:8.7.1
python-wtforms:3.2.1
python-wtforms-sqlalchemy:0.4.2
python-marshmallow-enum:1.5.1
python-indico:3.3.12
)


declare -a BUILDLIST=(
#python-wtforms:3.2.1
#python-pyrsistent:0.21.0
#python-marshmallow-dataclass:8.7.1
#python-pynpm:0.3.0
#python-WTForms-dateutil:0.1
#python-captcha:0.7.1
#python-Flask-Multipass:0.11.2
#python-flask-url-map-serializer:0.1.0
#python-pyrsistent:0.21.0
#python-webargs:8.7.1
#python-wallet-py3k:0.0.4
#python-flask-marshmallow:1.4.0
#python-limits:5.8.0
#python-flask-limiter:4.1.1
#python-marshmallow-enum:1.5.1
#python-indico:3.3.12
#OK python-marshmallow-sqlalchemy:1.4.2
#python-wtforms-dateutil:0.1
#python-flask-pluginengine:0.5
#python-flask-multipass:0.11.2
#python-wallet-py3k:0.0.4
#python-flask-marshmallow:1.4.0
python-marshmallow-oneofschema:3.2.0
)


for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
mkdir -p  logs
(sh srpmsbuild.sh $p $v --build &> logs/$p$v".log"  && sleep 2 && yum -y install ./$p/$v/rpmbuild/RPMS/*/*.rpm  )  || cat logs/$p$v".log"
#&> logs/$p$v".log" || echo "$p $v build failed" 
done
wait
exit
