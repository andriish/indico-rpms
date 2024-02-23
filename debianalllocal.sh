#!/bin/bash

export PATH=$PATH:$(pwd)
cd DEB
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
indico:3.2.9:indico
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
mkdir -p mydbtop
cd mydbtop
rm ./*tar.gz
if [ "$p" = "indico" ]; then

wget https://github.com/indico/indico/archive/refs/tags/v$v.tar.gz -O $p"_"$v.orig-main.tar.gz     
wget https://github.com/indico/indico-plugins/archive/refs/tags/v3.2.2.tar.gz -O  $p"_"$v.orig-plugins-base.tar.gz
rm -rf $p-$v
mkdir -p $p-$v/$p-$v/plugins
tar zxf  $p"_"$v.orig-main.tar.gz -C $p-$v 
tar zxf   $p"_"$v.orig-plugins-base.tar.gz -C $p-$v/$p-$v/plugins/
mv $p-$v/$p-$v/plugins/indico-plugins-3.2.2 $p-$v/$p-$v/plugins/base
rm -rf $p"_"$v.orig-plugins-base.tar.gz $p"_"$v.orig-main.tar.gz     
cd $p-$v/$p-$v
tar -zcf ../../$p"_"$v.orig.tar.gz  .
cd ../../
else
wget $u -O $p"_"$v.orig.tar.gz
fi
mkdir -p BUILD

cd BUILD
cp -r $TOP/debian ./
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
cd ../



exit