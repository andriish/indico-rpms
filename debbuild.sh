#!/bin/bash
p=$1
v=$2
P=$3
u=https://pypi.io/packages/source/$(echo $p | head -c 1)/$p/$P-$v.tar.gz
cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop
cd mydbtop
rm ./*tar.gz
if [ -f $TOP/get.sh ]; 
then
bash $TOP/get.sh
else
wget $u -O $p"_"$v.orig.tar.gz
fi
mkdir -p BUILD
cd BUILD
cp -r $TOP/debian ./
tar zxfv ../$p"_"$v.orig.tar.gz --strip-components 1
dpkg-buildpackage -us -uc
cd $TTOP




