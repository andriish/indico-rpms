#!/bin/bash

export PATH=$PATH:$(pwd)

set -x 
declare -a BUILDLIST=(
#flask-limiter:3.5.0
#flask-multipass:0.5.2
#flask-pluginengine:0.5
#flask-url-map-serializer:0.0.1
#flask-webpackext:1.0.2
#marshmallow-dataclass:8.6.0
#marshmallow-oneofschema:3.1.0
#node-semver:0.9.0
pynpm:0.2.0:pynpm
wtforms-dateutil:0.1:WTForms-dateutil
wtforms-sqlalchemy:0.4.1:WTForms-SQLAlchemy
)
TTOP=$(pwd)
mkdir -p logs/
for a in "${BUILDLIST[@]}" 
do
P=$(echo $a | cut -f3 -d: )
p=$(echo $a | cut -f1 -d: )
v=$(echo $a | cut -f2 -d: )
#mkdir -p PACKAGES/$p/$v
#cp -r PACKAGES/captcha/0.5.0/debian  PACKAGES/$p/$v
#sed -i 's/captcha/'$p'/g' PACKAGES/$p/$v/debian/*
#sed -i 's/0\.5\.0/'$v'/g' PACKAGES/$p/$v/debian/*
mkdir -p  logs
(sh mydb.sh $p $v $P  &> logs/$p$v".log" || echo "$p $v build failed" &)
done
wait
exit