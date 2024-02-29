#!/bin/bash
export PATH=$PATH:$(pwd)
#set -x 
declare -a BUILDLIST=(
#bleach:6.1.0:bleach
flask-limiter:3.5.0:Flask-Limiter
flask-pluginengine:0.5:Flask-PluginEngine
marshmallow-dataclass:8.6.0:marshmallow_dataclass
marshmallow-oneofschema:3.1.0:marshmallow_oneofschema
node-semver:0.9.0:node-semver
pynpm:0.2.0:pynpm
feedgen:1.0.0:feedgen
captcha:0.5.0:captcha
pywebpack:1.2.0:pywebpack
indico-fonts:1.2:indico-fonts
semver:3.0.2:semver
flask-multipass:0.5.2:Flask-Multipass
flask-url-map-serializer:0.1.0:flask-url-map-serializer
flask-webpackext:1.0.2:flask-webpackext
wtforms-dateutil:0.1:WTForms-dateutil
wtforms-sqlalchemy:0.4.1:WTForms-SQLAlchemy
indico:3.3.0:indico
)

#declare -a BUILDLIST=(
#bleach:6.1.0:bleach
#flask-pluginengine:0.5:Flask-PluginEngine
#flask-webpackext:1.0.2:flask-webpackext
#indico:3.2.9:indico
#)
TTOP=$(pwd)
mkdir -p logs/
for a in "${BUILDLIST[@]}" 
do
P=$(echo $a | cut -f3 -d: )
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
(
mkdir -p  logs && bash debbuild.sh $p $v  $P && apt-get -y install ./$p/$v/mydbtop/*deb
)  &> logs/$p$v".log" || (echo "$p $v build failed"  
&& cat logs/$p$v".log" 
)
done
wait
