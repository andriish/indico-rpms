#!bin/bash

export PATH=$PATH:$(pwd)
set -x 
declare -a BUILDLIST=(
python-exceptiongroup:1.2.0
python-Flask-Limiter:3.5.0
python-Flask-Multipass:0.5.3
python-Flask-PluginEngine:0.5
python-pypdf:4.0.1
python-WTForms-dateutil:0.1
python-captcha:0.5.0
python-flask-marshmallow:0.15.0
python-flask-url-map-serializer:0.1.0
python-indico-fonts:1.2
python-iso4217:1.11.20220401
python-marshmallow_oneofschema:3.0.1
python-marshmallow_sqlalchemy:0.29.0
python-marshmallow-dataclass:8.6.0
python-pynpm:0.2.0
python-pywebpack:1.2.0
python-flask-webpackext:1.0.2
python-webargs:8.3.0
python-indico:3.3.0
python-indico-mpp-configuration:3.3
)
mkdir -p python-indico/3.3.0/rpmbuild/RPMS/noarch
touch python-indico/3.3.0/rpmbuild/RPMS/noarch/1.rpm
exit 0
#declare -a BUILDLIST=(
#python-pypdf:4.0.1
#python-indico-mpp-configuration:3.3
#python-iso4217:1.11.20220401
#python-indico:3.3.0
#)
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
