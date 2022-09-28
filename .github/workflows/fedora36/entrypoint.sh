#!/bin/sh -l
set -x
uname -a 
cat /etc/issue
dnf -y install rpm-build git spectool sed

export PATH=$PATH:$(pwd)
#dnf list installed | grep @cop | tr -s ' '| cut -f 1,2 -d' ' | sed 's/\.noarch//g' | sed 's/\.x86_64//g' | sed 's/\-[123456789]*\.fc36//g'  | sed 's/\ /:/g'

set -x 
declare -a BUILDLIST=(
indico-devel:3.2
indico-mpp:3.2
python3-Flask-Limiter:2.4.0
python3-Flask-Multipass:0.4.6
python3-Flask-PluginEngine:0.4
python3-PyPDF2:2.11.0
python3-WTForms-SQLAlchemy:0.3
python3-WTForms-dateutil:0.1
python3-bleach:5.0.1
python3-captcha:0.4
python3-flask-marshmallow:0.14.0
python3-flask-url-map-serializer:0.0.1
python3-flask-webpackext:1.0.2
python3-hiredis:2.0.0
python3-indico:3.2
python3-indico-fonts:1.1
python3-indico-plugins:3.2
python3-iso_4217:0.4.220401
python3-limits:2.5.2
python3-marshmallow-oneofschema:3.0.1
python3-marshmallow-sqlalchemy:0.28.0
python3-marshmallow_dataclass:8.5.3
python3-pynpm:0.1.2
python3-pywebpack:1.2.0
python3-stack-data:0.5.0
python3-typing-inspect:0.7.1
python3-webargs:8.1.0
)

for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
yum -y install $(rpmspec -P $p/$v/$p.spec | grep BuildRequires | cut -d' ' -f2 | xargs) --skip-broken
done

touch BUILD.LOG
for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
(sh srpmsbuild.sh $p $v --build || echo  "Build of "$p$v" failed" >> BUILD.LOG&)
done
wait

cat BUILD.LOG

exit


out=$?
echo ::set-output name=out::$out
