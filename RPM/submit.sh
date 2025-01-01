#!bin/bash

export PATH=$PATH:$(pwd)
copr-cli create --enable-net=on --chroot fedora-41-x86_64 --chroot fedora-rawhide-x86_64 I335
declare -a BUILDLIST=( 
python-indico-mpp-configuration:3.3
python-indico:3.3.5
python-Flask-Limiter:3.5.0
python-Flask-Multipass:0.5.3
python-Flask-PluginEngine:0.5
python-pypdf:4.0.1
python-WTForms-dateutil:0.1
python-captcha:0.5.0
python-flask-marshmallow:0.15.0
python-flask-url-map-serializer:0.1.0
python-flask-webpackext:1.0.2
python-indico-fonts:1.2
python-iso4217:1.11.20220401
python-marshmallow_oneofschema:3.0.1
python-marshmallow_sqlalchemy:0.29.0
python-marshmallow-dataclass:8.6.0
python-pynpm:0.2.0
python-pywebpack:2.0.0
python-webargs:8.3.0
python-wtforms-sqlalchemy:0.3.0
)

mkdir -p log
for a in "${BUILDLIST[@]}" 
do
export name=$(echo $a | cut -f1 -d: )
export version=$(echo $a | cut -f2 -d: )
envsubst <<EOF > temp.sh
#!/bin/bash
git clone --depth 3 https://github.com/andriish/indico-rpms.git -b indico335
cd indico-rpms/RPM
sh srpmsbuild.sh  $name $version
EOF
copr add-package-custom I335 \
        --name $name \
        --script temp.sh \
        --script-resultdir indico-rpms/RPM/$name/$version/rpmbuild/SOURCES/ \
        --script-builddeps 'git rpmdevtools wget' \
        --script-chroot fedora-41-x86_64
mv temp.sh log/$name$version
done
