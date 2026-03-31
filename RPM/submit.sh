#!bin/bash

export PATH=$PATH:$(pwd)
copr-cli create --enable-net=on --chroot fedora-44-x86_64 --chroot fedora-rawhide-x86_64 I3312
declare -a BUILDLIST=( 
python-wallet-py3k:0.0.4
python-limits:5.4.0
python-Flask-Limiter:3.12
python-Flask-Multipass:0.11.2
python-Flask-PluginEngine:0.5
python-WTForms-dateutil:0.1
python-captcha:0.7.1
python-flask-marshmallow:1.4.0
python-flask-url-map-serializer:0.1.0
python-indico-fonts:1.2
python-iso4217:1.16
python-marshmallow_oneofschema:3.2.0
python-marshmallow_sqlalchemy:1.4.2
python-marshmallow-dataclass:8.7.1
python-pynpm:0.3.0
python-pywebpack:2.2.1
python-flask-webpackext:2.1.0
python-webargs:8.7.1
python-wtforms-sqlalchemy:0.3.0
python-indico:3.3.12
python-indico-mpp-configuration:3.3
python-pytest-runner:4.0
python-marshmallow-enum:1.5.1
python-pyrsistent:0.21.0
)

mkdir -p log
for a in "${BUILDLIST[@]}" 
do
export name=$(echo $a | cut -f1 -d: )
export version=$(echo $a | cut -f2 -d: )
envsubst <<EOF > temp.sh
#!/bin/bash
git clone --depth 3 https://github.com/andriish/indico-rpms.git -b indico3312
cd indico-rpms/RPM
sh srpmsbuild.sh  $name $version
EOF
copr add-package-custom I3312 \
        --name $name \
        --script temp.sh \
        --script-resultdir indico-rpms/RPM/$name/$version/rpmbuild/SOURCES/ \
        --script-builddeps 'git rpmdevtools wget' \
        --script-chroot fedora-44-x86_64
mv temp.sh log/$name$version
done
