#!/bin/bash

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
dpkg-buildpackage -us -uc
