#!/bin/bash

TTOP=$(pwd)

#pip3 download --no-deps --no-binary :all:
#https://pypi.io/packages/source/p/ppci/ppci-0.5.4.tar.gz
#

###BROKEN
p=node-semver
v=0.9.0
P=node-semver
u=https://pypi.io/packages/source/$(echo $p | head -c 1)/$p/$p-$v.tar.gz


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP

exit 0


##BROKEN!
u=https://files.pythonhosted.org/packages/7b/be/0a363bbb78db3995862283f5490bc5b30fa9a84affd80bd35c821edbe9ef/marshmallow_oneofschema-3.1.0.tar.gz
p=marshmallow-oneofschema
v=3.1.0
P=marshmallow_oneofschema


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP




exit 0

u=https://files.pythonhosted.org/packages/cd/41/5ebe6c04be47dfb84dc834385c913e35464d33b790576d4cb28042bf0669/marshmallow_dataclass-8.6.0.tar.gz
p=marshmallow-dataclass
v=8.6.0
P=marshmallow_dataclass


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP




exit 0

u=https://files.pythonhosted.org/packages/af/68/3350b8553eaedcf8c48aa0f79404a7a332f4630715b566d4e2475d888350/flask-webpackext-1.0.2.tar.gz
p=flask-webpackext
v=1.0.2
P=flask-webpackext


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP




exit 0

##BROKEN!!!
u=https://files.pythonhosted.org/packages/f5/1a/4b8ac7071b973e7f9f664dea58ee42f9fbba3a33234eadfa139f140eb7ca/flask-url-map-serializer-0.5.tar.gz
p=flask-url-map-serializer
v=0.0.1
P=flask-url-map-serializer


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP




exit 0



u=https://files.pythonhosted.org/packages/f5/1a/4b8ac7071b973e7f9f664dea58ee42f9fbba3a33234eadfa139f140eb7ca/Flask-PluginEngine-0.5.tar.gz
p=flask-pluginengine
v=0.5
P=Flask-PluginEngine


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP




exit 0

u=https://files.pythonhosted.org/packages/9c/74/d69d9e3f0eafa97393d32fd19eed781ea0852a2bfadecbf11974f639eea0/Flask-Multipass-0.5.2.tar.gz
p=flask-multipass
v=0.5.2
P=Flask-Multipass


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP




exit 0


u=https://files.pythonhosted.org/packages/7f/03/dae2279d45982b603ea001dcc1a4d0d6cc7f383c9f52a2e1563fcff6d1c4/Flask-Limiter-3.5.0.tar.gz
p=flask-limiter
v=3.5.0
P=Flask-Limiter


cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP




exit 0





u=https://files.pythonhosted.org/packages/6b/59/be0a6f852b5dfbf19e6c8e962c8f41407697f9f52a7902250ed98683ae89/feedgen-1.0.0.tar.gz
p=feedgen
v=1.0.0



cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $p-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP




exit 0


u=https://files.pythonhosted.org/packages/9d/e8/f41cd8879c3368fbc7297b463674d5d6439a80c61e089dbcee195c143fb7/captcha-0.5.0.tar.gz
p=captcha
v=0.5.0



cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $p-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP



u=https://files.pythonhosted.org/packages/b4/61/2585725d98a7cbd34ea9e745fba53b271cd43e11c4777321f67f6dd95372/pywebpack-1.2.0.tar.gz
p=pywebpack
v=1.2.0



cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz
mv $p-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP



u=https://files.pythonhosted.org/packages/4f/1c/5092b7ca637a24190d24893eb0888d5350a804e89307ca625b16c18c83b5/indico-fonts-1.2.tar.gz
p=indico-fonts
v=1.2



cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz
mv $p-$v/* ./
dpkg-buildpackage -us -uc
cd $TTOP



