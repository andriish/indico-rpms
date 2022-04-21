#!bin/bash

export PATH=$PATH:$(pwd)

set -x 
declare -a BUILDLIST=(
#python-ua-parser:0.10.0
#pyparsing:3.0.8
#Rivet:3.1.4
#python-webargs:8.1.0
#python-hiredis:2.0.0
### python-pywebpack:1.2.0
### python-pynpm:0.1.2
#python-email_validator:1.1.3
python-Flask-PluginEngine:0.4
#python-limits:2.5.2
#python-indico-fonts:1.1
)

for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
(sh srpmsbuild.sh $p $v --build &)
done
wait
exit
