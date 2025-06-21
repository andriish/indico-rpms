#!bin/bash

export PATH=$PATH:$(pwd)
set -x 
declare -a BUILDLISTO=(
python-wallet-py3k:0.0.4
python-limits:3.9.0
python-Flask-Limiter:3.5.0
python-Flask-Multipass:0.5.3
python-Flask-PluginEngine:0.5
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
python-pywebpack:2.0.0
python-flask-webpackext:1.0.2
python-webargs:8.3.0
python-wtforms-sqlalchemy:0.3.0
python-indico:3.3.6
python-indico-mpp-configuration:3.3
)
declare -a BUILDLISTX=(
#python-limits:5.4.0  # etdc problems
#python-Flask-Multipass:0.10  # OK
#python-captcha:0.7.1  # OK
#python-Flask-Limiter:3.12 #OK
#python-flask-marshmallow:1.3.0 #OK
#python-iso4217:1.13.20250512 #OK
#python-marshmallow_oneofschema:3.2.0 #OK
#python-marshmallow_sqlalchemy:1.4.2 #OK
#python-marshmallow-dataclass:8.7.1 #OK
#python-pywebpack:2.1.0  #OK
#python-pynpm:0.3.0  #OK
#python-flask-webpackext:2.1.0 #OK
#python-webargs:8.7.0 #OK
python-wtforms-sqlalchemy:0.4.2
)
#python-wallet-py3k:0.0.4                # OK
#python-limits:3.9.0                     # 5.4.0
#python-Flask-Limiter:3.5.0                  # 3.12
#python-Flask-Multipass:0.5.3                # 0.10 
#python-Flask-PluginEngine:0.5               # OK
#python-WTForms-dateutil:0.1                 #OK
#python-captcha:0.5.0                        # 0.7.1
#python-flask-marshmallow:0.15.0             # 1.3.0
#python-flask-url-map-serializer:0.1.0       # OK, NOT ON PYPY
#python-indico-fonts:1.2
#python-iso4217:1.11.20220401                #1.13.20250512
#python-marshmallow_oneofschema:3.0.1        # 3.2.0  NOT ON PYPY
#python-marshmallow_sqlalchemy:0.29.0        # 1.4.2
#python-marshmallow-dataclass:8.6.0          # 8.7.1
#python-pynpm:0.2.0                          # 0.3.0
#python-pywebpack:2.0.0                      # 2.1.0
#python-flask-webpackext:1.0.2               # 2.1.0

#python-webargs:8.3.0                        # 8.7.0
#python-wtforms-sqlalchemy:0.3.0             # 0.4.2

#python-indico:3.3.6
#python-indico-mpp-configuration:3.3


declare -a BUILDLIST=(
python-wallet-py3k:0.0.4
python-limits:3.9.0
python-Flask-Limiter:3.12
python-Flask-Multipass:0.10 
python-Flask-PluginEngine:0.5
python-WTForms-dateutil:0.1
python-captcha:0.7.1
python-flask-marshmallow:1.3.0
python-flask-url-map-serializer:0.1.0
python-indico-fonts:1.2
python-iso4217:1.13.20250512
python-marshmallow_oneofschema:3.2.0
python-marshmallow_sqlalchemy:1.4.2
python-marshmallow-dataclass:8.7.1
python-pynpm:0.3.0
python-pywebpack:2.1.0
python-flask-webpackext:2.1.0
python-webargs:8.7.0
python-wtforms-sqlalchemy:0.3.0
python-indico:3.3.6
python-indico-mpp-configuration:3.3
)
BUILDLIST=(
python-limits:3.14.1
)

#mkdir -p python-indico/3.3.0/rpmbuild/RPMS/noarch
#touch python-indico/3.3.0/rpmbuild/RPMS/noarch/1.rpm
#exit 0
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
