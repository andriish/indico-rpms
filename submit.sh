#!bin/bash

export PATH=$PATH:$(pwd)
copr-cli create --enable-net=on --chroot fedora-38-x86_64 --chroot fedora-39-x86_64 I328
#find ./ | grep '.spec$' | cut -f 2,3 -d'/'  | sed 's/\//:/g' | sort
declare -a BUILDLIST=( 
indico-mpp:3.2
python-indico:3.2.8
indico-devel:3.2.8
python-Flask-Limiter:2.4.0
python-Flask-Multipass:0.4.6
python-Flask-PluginEngine:0.4
python-PyPDF2:2.11.0
python-WTForms-SQLAlchemy:0.3
python-WTForms-dateutil:0.1
python-captcha:0.4
python-email_validator:1.2.1
python-flask-marshmallow:0.14.0
python-flask-url-map-serializer:0.0.1
python-flask-webpackext:1.0.2
python-hiredis:2.3.2
python-indico-fonts:1.1
python-iso_4217:0.4.220401
python-marshmallow-oneofschema:3.0.1
python-marshmallow-sqlalchemy:0.28.0
python-marshmallow_dataclass:8.5.3
python-pynpm:0.1.2
python-pywebpack:1.2.0
python-rich:12.2.0
python-typing-inspect:0.7.1
python-webargs:8.1.0

)
declare -a BUILDLIST2=( 
#indico-devel:3.1
#indico-devel:3.2
indico-devel:3.2.8
#indico-mpp:3.1
indico-mpp:3.2
#is in F
python-authlib:1.0.1
#python-bleach:4.0.0
#is in F
python-bleach:5.0.1
python-captcha:0.4
#python-email_validator:1.1.3
#F is old
python-email_validator:1.2.1
python-Flask-Limiter:2.4.0
python-flask-marshmallow:0.14.0
python-Flask-Multipass:0.4.6
python-Flask-PluginEngine:0.4
python-flask-url-map-serializer:0.0.1
python-flask-webpackext:1.0.2
python-hiredis:2.0.0
#python-indico:3.1
#python-indico:3.1.1
#python-indico:3.2
python-indico:3.2.3
python-indico-fonts:1.1
python-iso_4217:0.4.220401
#is in F
python-limits:2.5.2
python-marshmallow-dataclass:8.5.3
python-marshmallow_oneofschema:3.0.1
python-marshmallow_sqlalchemy:0.28.0
#is in F
python-matplotlib-inline:0.1.2
#is in F
python-pure-eval:0.2.2
python-pynpm:0.1.2
#F is old
python-PyPDF2:2.11.0
#is in F
python-pytest-localserver:0.7.0
python-pywebpack:1.2.0
#is in F
python-rich:12.2.0
#python-sentry-sdk:0.19.5
#is in F
python-sentry-sdk:1.5.7
#is in F
python-stack-data:0.5.0
#F is old
python-typing-inspect:0.7.1
#is in F
python-ua-parser:0.10.0
python-webargs:8.1.0
#is in F
python-wtforms:3.0.1
python-WTForms-dateutil:0.1
python-WTForms-SQLAlchemy:0.3
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
