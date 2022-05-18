#!bin/bash

export PATH=$PATH:$(pwd)

set -x 
declare -a BUILDLIST=(
python-indico:3.1.1
#python-ua-parser:0.10.0
#pyparsing:3.0.8
#Rivet:3.1.4
#python-webargs:8.1.0
#python-hiredis:2.0.0
### python-pywebpack:1.2.0
#python-flask-webpackext:1.0.2
#python-flask-marshmallow:0.14.0
#indico-devel:3.1
#python-WTForms-SQLAlchemy:0.3
### python-pynpm:0.1.2
#python-email_validator:1.1.3
#python-Flask-PluginEngine:0.4
#python-Flask-Multipass:0.4.6
#python-marshmallow_dataclass:8.5.3
#python-limits:2.5.2
#python-indico:3.1.1
#python-iso_4217:0.4.220401
#python-marshmallow-dataclass:8.5.3
)

for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
(sh srpmsbuild.sh $p $v --build &)
done
wait
exit
