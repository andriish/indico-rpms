#!/bin/sh -l
set -x
uname -a 
cat /etc/issue
dnf -y install rpm-build git wget sed

export PATH=$PATH:$(pwd)
#dnf list installed | grep @cop | tr -s ' '| cut -f 1,2 -d' ' | sed 's/\.noarch//g' | sed 's/\.x86_64//g' | sed 's/\-[123456789]*\.fc36//g'  | sed 's/\ /:/g' |  sed 's/python3/python/g' | grep -v plugin | sed 's/marshmallow-/marshmallow_/g' | sed 's/iso-/iso_/g'   | sed 's/-SQLAlchemy/_SQLAlchemy/g'  | sed 's/-validator/_validator/g' 

set -x 
declare -a BUILDLIST=(
indico-devel:3.2
indico-mpp:3.2
python-Flask-Limiter:2.4.0
python-Flask-Multipass:0.4.6
python-Flask-PluginEngine:0.4
python-PyPDF2:2.11.0
python-WTForms_SQLAlchemy:0.3
python-WTForms-dateutil:0.1
python-bleach:5.0.1
python-captcha:0.4
python-flask-marshmallow:0.14.0
python-flask-url-map-serializer:0.0.1
python-flask-webpackext:1.0.2
python-hiredis:2.0.0
python-indico:3.2
python-indico-fonts:1.1
python-iso_4217:0.4.220401
python-limits:2.5.2
python-marshmallow_oneofschema:3.0.1
python-marshmallow_sqlalchemy:0.28.0
python-marshmallow_dataclass:8.5.3
python-pynpm:0.1.2
python-pywebpack:1.2.0
python-stack-data:0.5.0
python-typing-inspect:0.7.1
python-webargs:8.1.0
)

for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
yum -y install wget $(rpmspec -P $p/$v/$p.spec | grep BuildRequires | cut -d' ' -f2 | xargs) --skip-broken
done

touch BUILD.LOG
for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
(sh srpmsbuild.sh $p $v --build || echo  "Build of "$p$v" failed" >> BUILD.LOG)
yum -y install wget  $p/$v/rpmbuild/RPMS/*/*.rpm --skip-broken
#(sh srpmsbuild.sh $p $v --build || echo  "Build of "$p$v" failed" >> BUILD.LOG&)
done
wait

cat BUILD.LOG

exit


out=$?
echo ::set-output name=out::$out
