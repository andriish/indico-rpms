#!bin/bash

export PATH=$PATH:$(pwd)

set -x 
declare -a BUILDLIST=(
#python-ua-parser:0.10.0
#pyparsing:3.0.8
#Rivet:3.1.4
python-indico-fonts:1.1
)

for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
(sh srpmsbuild.sh $p $v --build &)
done
wait
exit
