#!/bin/sh -l
set -x
uname -a 
cat /etc/issue

dnf -y install dnf* rpm-build git wget sed createrepo
dnf -y copr enable averbyts/IR 
dnf -y install indico-devel
export PATH=$PATH:$(pwd)
set -x 
mkdir -p /github/home/.npm
chown -R 1001:121 "/github/home/.npm"
sh srpmsbuild.sh  python-indico 3.2 --build 
yum -y install wget  python-indico/3.2/rpmbuild/RPMS/*/*.rpm --skip-broken

out=$?
echo ::set-output name=out::$out
