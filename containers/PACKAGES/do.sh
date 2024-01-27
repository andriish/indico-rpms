#!/bin/bash

export PATH=$PATH:$(pwd)




mkdir -p  logs
p=flask-url-map-serializer
v=0.1.0
P=js-flask-urls-babel-plugin-flask-urls
(
u=https://github.com/indico/js-flask-urls/archive/refs/tags/babel-plugin-flask-urls@0.1.0.tar.gz
cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/flask-cli/* ./
rm -rf $P-$v
dpkg-buildpackage -us -uc
) &> logs/$p$v".log" || echo "$p $v build failed"
#exit 0

set -x 
declare -a BUILDLIST=(
#flask-limiter:3.5.0:Flask-Limiter
#flask-multipass:0.5.2:Flask-Multipass
#flask-pluginengine:0.5:Flask-PluginEngine
# flask-url-map-serializer:0.0.1:flask-url-map-serializer
 flask-webpackext:1.0.2:flask-webpackext
#marshmallow-dataclass:8.6.0:marshmallow_dataclass
## marshmallow-oneofschema:3.1.0:marshmallow_oneofschema
 node-semver:0.9.0:node-semver
#pynpm:0.2.0:pynpm
#wtforms-dateutil:0.1:WTForms-dateutil
#wtforms-sqlalchemy:0.4.1:WTForms-SQLAlchemy
#feedgen:1.0.0:feedgen
#captcha:0.5.0:captcha
 pywebpack:1.2.0:pywebpack
#indico-fonts:1.2:indico-fonts
semver:3.0.2:semver
)

TTOP=$(pwd)
mkdir -p logs/
for a in "${BUILDLIST[@]}" 
do
P=$(echo $a | cut -f3 -d: )
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
#mkdir -p PACKAGES/$p/$v
#cp -r PACKAGES/captcha/0.5.0/debian  PACKAGES/$p/$v
#sed -i 's/captcha/'$p'/g' PACKAGES/$p/$v/debian/*
#sed -i 's/0\.5\.0/'$v'/g' PACKAGES/$p/$v/debian/*

mkdir -p  logs
(sh mydb.sh $p $v $P  &> logs/$p$v".log" || echo "$p $v build failed" &)
done
wait


















exit