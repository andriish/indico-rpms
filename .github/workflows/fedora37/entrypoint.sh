#!/bin/sh -l
set -x
uname -a 
cat /etc/issue

dnf -y install dnf* rpm-build git wget sed createrepo
dnf -y copr enable averbyts/IR 

export PATH=$PATH:$(pwd)
#dnf list installed | grep @cop | tr -s ' '| cut -f 1,2 -d' ' | sed 's/\.noarch//g' | sed 's/\.x86_64//g' | sed 's/\-[123456789]*\.fc36//g'  | sed 's/\ /:/g' |  sed 's/python3/python/g' | grep -v plugin | sed 's/marshmallow-o/marshmallow_o/g' | sed 's/marshmallow-s/marshmallow_s/g' | sed 's/iso-/iso_/g'     | sed 's/-validator/_validator/g' 

set -x 
yum -y install wget $(rpmspec -P python-indico/3.2/*.spec | grep BuildRequires | tr -s ' ' |cut -d: -f2 | xargs) --skip-broken
yum -y install wget $(rpmspec -P python-indico/3.2/*.spec | grep BuildRequires | tr -s ' ' |cut -d: -f2 | xargs) --skip-broken
chown -R 1001:121 "/github/home/.npm"
sh srpmsbuild.sh  python-indico 3.2 --build 
yum -y install wget  python-indico/3.2/rpmbuild/RPMS/*/*.rpm --skip-broken


out=$?
echo ::set-output name=out::$out
