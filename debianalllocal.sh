#!/bin/bash

export PATH=$PATH:$(pwd)

#set -x 
declare -a BUILDLIST=(
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
)

#declare -a BUILDLIST=(
#)
TTOP=$(pwd)
mkdir -p logs/
for a in "${BUILDLIST[@]}" 
do
P=$(echo $a | cut -f3 -d: )
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )

(
u=https://pypi.io/packages/source/$(echo $p | head -c 1)/$p/$P-$v.tar.gz
if [ "$p" = "flask-url-map-serializer" ]; then
u=https://github.com/indico/js-flask-urls/archive/refs/tags/babel-plugin-flask-urls@$v.tar.gz
fi
cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
if [ "$p" = "flask-url-map-serializer" ]; then
mv js-flask-urls-babel-plugin-flask-urls-$v/* ./
else
mv $P-$v/* ./
fi
dpkg-buildpackage -us -uc
cd $TTOP
apt-get -y install ./$p/$v/mydbtop/*deb
)  &> logs/$p$v".log" || (echo "$p $v build failed"  && cat logs/$p$v".log" )
done
wait

exit
(
p=indico
v=3.2.9
P=indico


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget https://github.com/indico/indico/archive/refs/tags/v$v.tar.gz -O ../$p"_"$v.orig.tar.gz     
wget https://github.com/indico/indico-plugins/archive/refs/tags/v3.2.2.tar.gz -O  ../v3.2.2.tar.gz

tar zxf ../$p"_"$v.orig.tar.gz 
tar zxf ../v3.2.2.tar.gz 


mv $P-$v/* ./

 mkdir -p plugins
           mv indico-plugins-3.2.2/ plugins/base
           rm -rf plugins/base/piwik
           rm -rf plugins/base/themes_legacy
           rm -rf plugins/base/ursh
           rm -rf plugins/base/vc_zoom
           rm -rf plugins/base/cloud_captchas
           rm -rf plugins/base/owncloud
           rm -rf plugins/base/previewer_jupyter
           sed -i 's/iso4217\=\=.*$/iso4217/g'     plugins/base/*/setup.cfg
           sed -i 's/nbconvert\=\=.*$/nbconvert/g' plugins/base/*/setup.cfg
           sed -i 's/indico-plugin-piwik.*$//g'    plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-ursh.*$//g'     plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-vc-zoom.*$//g'  plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-cloud-captchas.*$//g'  plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-owncloud.*$//g'  plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-previewer-jupyter.*$//g'  plugins/base/_meta/setup.cfg
           sed -i 's/\=\=.*$//g' requirements.*
           sed -i 's/tzdata/#tzdata/g' requirements.*
           sed -i 's/pypdf/#pypdf/g' requirements.*
           sed -i 's/importlib/#importlib/g' requirements.*

dpkg-buildpackage -us -uc
cd $TTOP
apt-get -y install ./$p/$v/mydbtop/*deb
)   > logs/$p$v".log" || (echo "$p $v build failed"  && cat logs/$p$v".log" )



exit