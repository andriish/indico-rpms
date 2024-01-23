#!/bin/bash

TTOP=$(pwd)




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



