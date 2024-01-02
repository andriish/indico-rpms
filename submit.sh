#!bin/bash

export PATH=$PATH:$(pwd)
copr-cli create --enable-net=on --chroot fedora-38-x86_64 --chroot fedora-39-x86_64 I328
#find ./ | grep '.spec$' | cut -f 2,3 -d'/'  | sed 's/\//:/g' | sort
declare -a BUILDLIST=( 
indico-mpp:3.2
python-indico:3.2.8
indico-devel:3.2.8
#python-Flask-Limiter:2.4.0
python-Flask-Limiter:3.5.0
#python-Flask-Multipass:0.4.6
python-Flask-Multipass:0.5.2
#python-Flask-PluginEngine:0.4
python-Flask-PluginEngine:0.5
python-PyPDF2:2.11.0
python-WTForms-SQLAlchemy:0.3
python-WTForms-dateutil:0.1
#python-captcha:0.4
python-captcha:0.5.0
python-email_validator:1.2.1
#python-flask-marshmallow:0.14.0
python-flask-marshmallow:0.15.0
#python-flask-url-map-serializer:0.0.1
python-flask-url-map-serializer:0.1.0
python-flask-webpackext:1.0.2
python-hiredis:2.3.2
#python-indico-fonts:1.1
python-indico-fonts:1.2
python-iso_4217:0.4.220401
python-marshmallow_oneofschema:3.0.1
#python-marshmallow_sqlalchemy:0.28.0
python-marshmallow_sqlalchemy:0.29.0
#python-marshmallow-dataclass:8.5.3
python-marshmallow-dataclass:8.6.0
#python-pynpm:0.1.2
python-pynpm:0.2.0
python-pywebpack:1.2.0
python-rich:12.2.0
python-typing-inspect:0.7.1
#python-webargs:8.1.0
python-webargs:8.3.0
)

mkdir -p log
for a in "${BUILDLIST[@]}" 
do
export name=$(echo $a | cut -f1 -d: )
export version=$(echo $a | cut -f2 -d: )
envsubst <<EOF > temp.sh
#!/bin/bash
git clone --depth 3 https://github.com/andriish/indico-rpms.git -b indico328
cd indico-rpms
sh srpmsbuild.sh  $name $version
EOF
copr add-package-custom I328 \
        --name $name \
        --script temp.sh \
        --script-resultdir indico-rpms/$name/$version/rpmbuild/SOURCES/ \
        --script-builddeps 'git rpmdevtools wget' \
        --script-chroot fedora-38-x86_64
mv temp.sh log/$name$version
done
