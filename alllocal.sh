#!bin/bash

export PATH=$PATH:$(pwd)

set -x 
declare -a BUILDLIST=(
#Rivet:3.1.4
)

for a in "${BUILDLIST[@]}" 
do
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
(sh srpmsbuild.sh $p $v --build &)
done
wait
exit
