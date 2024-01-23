FROM debian:12
RUN apt-get -y upgrade
RUN apt update

RUN apt install -y lsb-release wget curl gnupg
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt update
RUN apt install -y --install-recommends postgresql-13 libpq-dev apache2 libapache2-mod-proxy-uwsgi libapache2-mod-xsendfile libxslt1-dev libxml2-dev libffi-dev libpcre3-dev libyaml-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev xz-utils liblzma-dev uuid-dev build-essential redis-server
RUN apt install -y --install-recommends libxslt1-dev libxml2-dev libffi-dev libpcre3-dev libyaml-dev build-essential redis-server postgresql libpq-dev

RUN apt install -y libjpeg62-turbo-dev
RUN apt install -y python3-pip
RUN apt install -y python3-semver python3-alembic python3-amqp  python3-asttokens \
#python3-attrs \
python3-authlib \
python3-babel \
python3-backcall \
 python3-bcrypt \
 python3-billiard \
 python3-bleach \
 python3-blinker \
 python3-celery \
 python3-certifi \
 python3-cffi \
 python3-charset-normalizer \
 python3-click \
 python3-click-didyoumean \
 python3-click-plugins \
 python3-click-repl \
 python3-cryptography \
 python3-decorator \
 python3-distro \
 python3-dns 

RUN apt install -y \
# python3-email_validator \
 python3-executing \
# python3-feedgen \
 python3-flask \
 python3-flask-babel \
 python3-flask-caching \
# python3-Flask-Limiter \
 python3-flask-marshmallow \
 python3-flask-migrate \
# python3-Flask-Multipass \
# python3-Flask-PluginEngine \
 python3-flask-sqlalchemy \
# python3-flask-webpackext \
# python3-flask-wtf \
 python3-greenlet \
 python3-greenlet \
 python3-hiredis \
 python3-hiredis \
 python3-html2text \
 python3-html5lib \
 python3-icalendar \
 python3-idna


RUN apt install -y \
# python3-indico-fonts \
# python3-indico-fonts \
 python3-ipython \
 python3-itsdangerous \
 python3-jedi \
 python3-jinja2 \
 python3-jsonschema \
 python3-kombu \
 python3-limits \
 python3-lxml \
 python3-mako \
 python3-markdown \
 python3-markupsafe \
 python3-marshmallow \
 python3-marshmallow-enum \
# python3-marshmallow-oneofschema \
 python3-marshmallow-sqlalchemy \
 python3-matplotlib-inline \
# python3-mypy_extensions \
# python3-node-semver \
 python3-packaging \
 python3-parso \
 python3-pexpect \
 python3-pickleshare \
 python3-pillow \
 python3-prompt-toolkit \
 python3-psycopg2 \
 python3-ptyprocess \
 python3-pycountry \
 python3-pycparser \
 python3-pygments \
# python3-pynpm \
 python3-pyparsing \
# python3-PyPDF2  \
 python3-pyrsistent \
 python3-dateutil \
# python3-pytz \
# python3-pywebpack \
# python3-pyyaml \
# python3-qrcode-core \
 python3-redis \
 python3-reportlab \
 python3-requests \
 python3-sentry-sdk \
 python3-simplejson \
 python3-six \
 python3-speaklater \
 python3-sqlalchemy \
 python3-terminaltables \
 python3-traitlets \
 python3-translitcodec \
 python3-typing-extensions \
 python3-typing-inspect \
 python3-ua-parser \
 python3-urllib3 \
 python3-vine \
 python3-wcwidth \
 python3-webargs \
 python3-webencodings \
 python3-werkzeug \
 python3-wtforms \
# python3-WTForms-dateutil \
# python3-wtforms-sqlalchemy \
 python3-zipp


RUN apt install -y  unzip \
python3-email-validator \
python3-feedgenerator \
python3-mypy-extensions 


RUN wget https://github.com/indico/indico/archive/refs/tags/v3.2.8.zip && \
 wget  https://github.com/indico/indico-plugins/archive/refs/tags/v3.2.2.tar.gz && \
 unzip v3.2.8.zip && tar zxfv v3.2.2.tar.gz && ls && ls indico-plugins-3.2.2



RUN mkdir -p plugins &&  \
cd indico-3.2.8 && mkdir -p plugins && mv ../indico-plugins-3.2.2 plugins/base  &&  \
rm -rf plugins/base/piwik  &&  \
rm -rf plugins/base/themes_legacy  &&  \
rm -rf plugins/base/ursh  &&  \
rm -rf plugins/base/vc_zoom  &&  \
rm -rf plugins/base/cloud_captchas  &&  \
rm -rf plugins/base/owncloud  &&  \
rm -rf plugins/base/previewer_jupyter  


RUN set -x && cd indico-3.2.8  && pwd && ls  &&  \
sed -i "s/python_requires.*/python_requires\ =\ \~="%{python3_version}"/g" plugins/base/*/setup.cfg  &&  \
sed -i 's/Programming\ Language\ ::\ Python ::\ .*/Programming\ Language\ ::\ Python\ ::\ '%{python3_version}'/g' plugins/base/*/setup.cfg  &&  \
sed -i 's/iso4217\=\=.*$/iso4217/g'     plugins/base/*/setup.cfg  &&  \
sed -i 's/nbconvert\=\=.*$/nbconvert/g' plugins/base/*/setup.cfg  &&  \
sed -i 's/indico-plugin-piwik.*$//g'    plugins/base/_meta/setup.cfg  &&  \
sed -i 's/indico-plugin-ursh.*$//g'     plugins/base/_meta/setup.cfg  &&  \
sed -i 's/indico-plugin-vc-zoom.*$//g'  plugins/base/_meta/setup.cfg  &&  \
sed -i 's/indico-plugin-cloud-captchas.*$//g'  plugins/base/_meta/setup.cfg  &&  \
sed -i 's/indico-plugin-owncloud.*$//g'  plugins/base/_meta/setup.cfg  &&  \
sed -i 's/indico-plugin-previewer-jupyter.*$//g'  plugins/base/_meta/setup.cfg  &&  \
sed -i 's/\=\=.*$//g' requirements.*  &&  \
sed -i 's/tzdata/#tzdata/g' requirements.*  &&  \
sed -i 's/pypdf/#pypdf/g' requirements.*  &&  \
sed -i 's/importlib/#importlib/g' requirements.*


RUN  apt install -y nodejs npm

RUN  cd indico-3.2.8  &&  export NODE_OPTIONS="--max-old-space-size=5120"  && \
export PYTHONPATH=$(pwd):$PYTHONPATH  && \
mkdir -p indico/web/client  && \
cd indico/web/client  && \
npm config delete proxy  && \
npm config delete http-proxy  && \
npm config delete https-proxy  && \
npm instal

RUN apt install -y  \
python3-png python3-xlsxwriter python3-colorclass python3-qrcode python3-ordered-set  python3-wtforms python3-importlib-metadata \
python3-flaskext.wtf


#RUN  cd indico-3.2.8  && pip install -r requirements.txt --break-system-packages --upgrade-strategy only-if-needed
RUN  cd indico-3.2.8  && \ 
pip install node-semver indico-fonts pynpm marshmallow-oneofschema marshmallow-dataclass \
            flask-multipass feedgen captcha wtforms-sqlalchemy wtforms-dateutil pywebpack \
             flask-webpackext flask-pluginengine flask-limiter   flask-url-map-serializer \
 --break-system-packages --upgrade-strategy only-if-needed


RUN  cd indico-3.2.8  && wget https://raw.githubusercontent.com/andriish/indico-rpms/indico328debian/python-indico/3.2.8/indico-patch.txt && \
patch -p 1 < indico-patch.txt

RUN  cd indico-3.2.8  && ./bin/maintenance/build-wheel.py indico       --ignore-unclean 
RUN  cd indico-3.2.8  && ./bin/maintenance/build-wheel.py all-plugins  --ignore-unclean  plugins/base 

#alembic-1.13.1 captcha-0.5.0 colorclass-2.2.2 feedgen-1.0.0 flask-limiter-3.5.0 flask-multipass-0.5.2 
#flask-pluginengine-0.5 flask-webpackext-1.0.2 flask-wtf-1.2.1 importlib-metadata-7.0.1 indico-fonts-1.2 
#marshmallow-dataclass-8.6.0 marshmallow-oneofschema-3.1.0 node-semver-0.9.0 ordered-set-4.1.0 pynpm-0.2.0 
#pypng-0.20220715.0 pywebpack-1.2.0 qrcode-7.4.2 wtforms-3.1.2 wtforms-dateutil-0.1 wtforms-sqlalchemy-0.4.1 xlsxwriter-3.1.9


#alembic-1.13.1 captcha-0.5.0 feedgen-1.0.0 flask-limiter-3.5.0 flask-multipass-0.5.2 flask-pluginengine-0.5
# flask-webpackext-1.0.2 flask-wtf-1.2.1 importlib-metadata-7.0.1 indico-fonts-1.2 marshmallow-dataclass-8.6.0 
#marshmallow-oneofschema-3.1.0 node-semver-0.9.0 pynpm-0.2.0 pywebpack-1.2.0 wtforms-3.1.2 wtforms-dateutil-0.1 wtforms-sqlalchemy-0.4.1
