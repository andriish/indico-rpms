%global srcname indico
%global srcnamenu indico
%global igittag 1a4ed25f80ffd3b93b804036c4d593e087f9f055
%global pgittag bece9eec553ee0cec9667c6dcef6ef6498e1093c
%define iplugin()  \
%%package -n python3-indico-%1-plugin \
Summary:        Indico plugin %1  \
Requires: python3-indico \
%%description -n python3-indico-%1-plugin \
Indico plugin %1 

%define filesinplugin() \
%%files -n python3-indico-%1-plugin \
%{python3_sitelib}/indico_%1/* \
%{python3_sitelib}/indico_plugin_%1-3.3.dev0.dist-info/*



Name:           python-%{srcname}
Version:        3.3.0
Release:        10%{?dist}
Summary:        Indico package

License:        MIT
URL:            https://getindico.io/
Source0:        https://github.com/indico/indico/archive/%{igittag}.zip
Source1:        https://github.com/indico/indico-plugins/archive/%{pgittag}.tar.gz
Patch0:         indico-patch.txt
BuildArch:      noarch

BuildRequires: nodejs-npm
BuildRequires: python-build
BuildRequires: python3-pip python3-wheel
BuildRequires: python3-rpm-macros
BuildRequires: gcc-c++ git gcc make 
BuildRequires: rpm-build git wget python3-rpm-macros
BuildRequires: pyproject-rpm-macros python-srpm-macros 
BuildRequires: npm

BuildRequires: tzdata
Requires: tzdata
Requires: postfix
Requires: postgresql postgresql-server postgresql-libs postgresql-devel postgresql-contrib
Requires: redis httpd mod_proxy_uwsgi mod_ssl mod_xsendfile

BuildRequires: libjpeg-turbo-devel libxslt-devel libxml2-devel libffi-devel pcre-devel libyaml-devel 
BuildRequires: zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils libuuid-devel
Requires: zlib bzip2 readline sqlite xz libffi findutils libuuid

Requires: uwsgi
Requires: uwsgi-plugin-python3
Requires: uwsgi-plugin-python3-gevent 

Requires: tex(adjustbox.sty)
Requires: tex(amsmath.sty)
Requires: tex(amssymb.sty)
Requires: tex(babel.sty)
Requires: tex(enumitem.sty)
Requires: tex(fancyhdr.sty)
Requires: tex(float.sty)
Requires: tex(fontspec.sty)
Requires: tex(geometry.sty)
Requires: tex(microtype.sty)
Requires: tex(needspace.sty)
Requires: tex(parskip.sty)
Requires: tex(scrextend.sty)
Requires: tex(sectsty.sty)
Requires: tex(tcolorbox.sty)
Requires: tex(truncate.sty)
Requires: tex(xcolor.sty)
Requires: tex(xstring.sty)



Requires: python3
Requires: python3-alembic
Requires: python3-amqp
Requires: python3-asttokens
Requires: python3-attrs
Requires: python3-authlib
Requires: python3-babel
Requires: python3-backcall
Requires: python3-bcrypt
Requires: python3-billiard
Requires: python3-bleach
Requires: python3-blinker
Requires: python3-boto3
Requires: python3-build
Requires: python3-cachelib
Requires: python3-captcha
Requires: python3-celery
Requires: python3-certifi
Requires: python3-cffi
Requires: python3-charset-normalizer
Requires: python3-click
Requires: python3-click-didyoumean
Requires: python3-click-plugins
Requires: python3-click-repl
Requires: python3-colorclass
Requires: python3-cryptography
Requires: python3-dateutil
Requires: python3-decorator
Requires: python3-devel
Requires: python3-distro
Requires: python3-dns
Requires: python3-email-validator
#Requires: python3-exceptiongroup
Requires: python3-executing
Requires: python3-feedgen
Requires: python3-flask
Requires: python3-flask-babel
Requires: python3-flask-caching
Requires: python3-flask-cors 
Requires: python3-Flask-Limiter
Requires: python3-flask-marshmallow
Requires: python3-flask-migrate
Requires: python3-Flask-Multipass
Requires: python3-Flask-PluginEngine
Requires: python3-flask-sqlalchemy
Requires: python3-flask-url-map-serializer
Requires: python3-flask-webpackext
Requires: python3-flask-wtf
Requires: python3-flit-core 
Requires: python3-google-api-client  
Requires: python3-greenlet
Requires: python3-greenlet
Requires: python3-hiredis
Requires: python3-hiredis
Requires: python3-html2text
Requires: python3-html5lib
Requires: python3-icalendar
Requires: python3-idna
Requires: python3-indico-fonts
Requires: python3-indico-fonts
Requires: python3-ipython
Requires: python3-itsdangerous
Requires: python3-jedi
Requires: python3-jinja2
Requires: python3-jsonschema
Requires: python3-jwt
Requires: python3-kombu
Requires: python3-ldap
Requires: python3-limits
Requires: python3-lxml
Requires: python3-mako
Requires: python3-markdown
Requires: python3-markupsafe
Requires: python3-marshmallow
Requires: python3-marshmallow_dataclass
Requires: python3-marshmallow-enum
Requires: python3-marshmallow-oneofschema
Requires: python3-marshmallow-sqlalchemy
Requires: python3-matplotlib-inline
Requires: python3-mypy_extensions
Requires: python3-nbconvert 
Requires: python3-node-semver
Requires: python3-packaging
Requires: python3-parso
Requires: python3-pexpect
Requires: python3-pickleshare
Requires: python3-pillow
Requires: python3-prompt-toolkit
Requires: python3-psycopg2
Requires: python3-ptyprocess
Requires: python3-pure-eval
Requires: python3-pycountry
Requires: python3-pycparser
Requires: python3-pygments
Requires: python3-pynpm
Requires: python3-pyparsing
Requires: python3-pypdf >= 4.0
Requires: python3-pyrsistent
Requires: python3-pytz
Requires: python3-pywebpack
Requires: python3-pyyaml
Requires: python3-qrcode-core
Requires: python3-redis
Requires: python3-reportlab
Requires: python3-requests
Requires: python3-rpm-macros 
Requires: python3-semver
Requires: python3-semver
Requires: python3-sentry-sdk
Requires: python3-simplejson
Requires: python3-six
Requires: python3-speaklater
Requires: python3-sqlalchemy
Requires: python3-stack-data
Requires: python3-terminaltables
Requires: python3-tinycss2
Requires: python3-traitlets
Requires: python3-translitcodec
Requires: python3-typing-extensions
Requires: python3-typing-inspect
Requires: python3-ua-parser
Requires: python3-urllib3
Requires: python3-vine
Requires: python3-wcwidth
Requires: python3-weasyprint
Requires: python3-webargs
Requires: python3-webencodings
Requires: python3-werkzeug
Requires: python3-wheel
Requires: python3-wtforms >= 3.0.0
Requires: python3-WTForms-dateutil
Requires: python3-wtforms-sqlalchemy
Requires: python3-xlsxwriter
Requires: python3-zipp


########################
BuildRequires: python3
BuildRequires: python3-alembic
BuildRequires: python3-amqp
BuildRequires: python3-asttokens
BuildRequires: python3-attrs
BuildRequires: python3-authlib
BuildRequires: python3-babel
BuildRequires: python3-backcall
BuildRequires: python3-bcrypt
BuildRequires: python3-billiard
BuildRequires: python3-bleach
BuildRequires: python3-blinker
BuildRequires: python3-boto3
BuildRequires: python3-build
BuildRequires: python3-cachelib
BuildRequires: python3-captcha
BuildRequires: python3-celery
BuildRequires: python3-certifi
BuildRequires: python3-cffi
BuildRequires: python3-charset-normalizer
BuildRequires: python3-click
BuildRequires: python3-click-didyoumean
BuildRequires: python3-click-plugins
BuildRequires: python3-click-repl
BuildRequires: python3-colorclass
BuildRequires: python3-cryptography
BuildRequires: python3-dateutil
BuildRequires: python3-decorator
BuildRequires: python3-devel
BuildRequires: python3-distro
BuildRequires: python3-dns
BuildRequires: python3-email-validator
#BuildRequires: python3-exceptiongroup
BuildRequires: python3-executing
BuildRequires: python3-feedgen
BuildRequires: python3-flask
BuildRequires: python3-flask-babel
BuildRequires: python3-flask-caching
BuildRequires: python3-flask-cors 
BuildRequires: python3-Flask-Limiter
BuildRequires: python3-flask-marshmallow
BuildRequires: python3-flask-migrate
BuildRequires: python3-Flask-Multipass
BuildRequires: python3-Flask-PluginEngine
BuildRequires: python3-flask-sqlalchemy
BuildRequires: python3-flask-url-map-serializer
BuildRequires: python3-flask-webpackext
BuildRequires: python3-flask-wtf
BuildRequires: python3-flit-core 
BuildRequires: python3-google-api-client  
BuildRequires: python3-greenlet
BuildRequires: python3-greenlet
BuildRequires: python3-hiredis
BuildRequires: python3-hiredis
BuildRequires: python3-html2text
BuildRequires: python3-html5lib
BuildRequires: python3-icalendar
BuildRequires: python3-idna
BuildRequires: python3-indico-fonts
BuildRequires: python3-indico-fonts
BuildRequires: python3-ipython
BuildRequires: python3-itsdangerous
BuildRequires: python3-jedi
BuildRequires: python3-jinja2
BuildRequires: python3-jsonschema
BuildRequires: python3-jwt
BuildRequires: python3-kombu
BuildRequires: python3-ldap
BuildRequires: python3-limits
BuildRequires: python3-lxml
BuildRequires: python3-mako
BuildRequires: python3-markdown
BuildRequires: python3-markupsafe
BuildRequires: python3-marshmallow
BuildRequires: python3-marshmallow_dataclass
BuildRequires: python3-marshmallow-enum
BuildRequires: python3-marshmallow-oneofschema
BuildRequires: python3-marshmallow-sqlalchemy
BuildRequires: python3-matplotlib-inline
BuildRequires: python3-mypy_extensions
BuildRequires: python3-nbconvert 
BuildRequires: python3-node-semver
BuildRequires: python3-packaging
BuildRequires: python3-parso
BuildRequires: python3-pexpect
BuildRequires: python3-pickleshare
BuildRequires: python3-pillow
BuildRequires: python3-prompt-toolkit
BuildRequires: python3-psycopg2
BuildRequires: python3-ptyprocess
BuildRequires: python3-pure-eval
BuildRequires: python3-pycountry
BuildRequires: python3-pycparser
BuildRequires: python3-pygments
BuildRequires: python3-pynpm
BuildRequires: python3-pyparsing
BuildRequires: python3-pypdf >= 4.0
BuildRequires: python3-pyrsistent
BuildRequires: python3-pytz
BuildRequires: python3-pywebpack
BuildRequires: python3-pyyaml
BuildRequires: python3-qrcode-core
BuildRequires: python3-redis
BuildRequires: python3-reportlab
BuildRequires: python3-requests
BuildRequires: python3-rpm-macros 
BuildRequires: python3-semver
BuildRequires: python3-semver
BuildRequires: python3-sentry-sdk
BuildRequires: python3-simplejson
BuildRequires: python3-six
BuildRequires: python3-speaklater
BuildRequires: python3-sqlalchemy
BuildRequires: python3-stack-data
BuildRequires: python3-terminaltables
BuildRequires: python3-tinycss2
BuildRequires: python3-traitlets
BuildRequires: python3-translitcodec
BuildRequires: python3-typing-extensions
BuildRequires: python3-typing-inspect
BuildRequires: python3-ua-parser
BuildRequires: python3-urllib3
BuildRequires: python3-vine
BuildRequires: python3-wcwidth
BuildRequires: python3-weasyprint
BuildRequires: python3-webargs
BuildRequires: python3-webencodings
BuildRequires: python3-werkzeug
BuildRequires: python3-wheel
BuildRequires: python3-wtforms >= 3.0.0
BuildRequires: python3-WTForms-dateutil
BuildRequires: python3-wtforms-sqlalchemy
BuildRequires: python3-xlsxwriter
BuildRequires: python3-zipp
#######################


%global _description %{expand:
Indico event management system.
}
%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%description -n python3-%{srcname} %_description

#package -n python3-#{srcname}-plugins
#Summary:        #{summary}
#Requires: python3-#{srcname}
#description -n python3-#{srcname}-plugins #_description

%package -n python3-%{srcname}-dummy
Summary:        %{summary}
Requires: python3-%{srcname}
%description -n python3-%{srcname}-dummy %_description


%iplugin citadel
%iplugin cloud_captchas
%iplugin livesync
#iplugin livesync_debug
%iplugin owncloud
%iplugin payment_manual
%iplugin payment_paypal
%iplugin payment_sixpay
%iplugin piwik
%iplugin previewer_code
%iplugin previewer_jupyter
%iplugin prometheus
%iplugin storage_s3
%iplugin themes_legacy
%iplugin ursh
%iplugin vc_dummy
%iplugin vc_zoom


%prep
%autosetup  -n indico-%{igittag} -p 1
%setup -q -T -D -a 1 -n indico-%{igittag}
mkdir -p plugins
mv indico-plugins-%{pgittag} plugins/base
rm -rf plugins/base/livesync_debug

sed -i "s/python_requires.*/python_requires\ =\ \~="%{python3_version}"/g" plugins/base/*/setup.cfg
sed -i 's/iso4217\=\=.*$/iso4217/g'     plugins/base/*/setup.cfg
sed -i 's/nbconvert\=\=.*$/nbconvert/g' plugins/base/*/setup.cfg

sed -i '/# BEGIN GENERATED REQUIREMENTS/,/# END GENERATED REQUIREMENTS/d' plugins/base/_meta/setup.cfg

%py3_shebang_fix ./

sed -i 's/\=\=.*$//g' requirements.*
sed -i 's/tzdata/#tzdata/g' requirements.*
sed -i 's/pypdf/#pypdf/g' requirements.*
sed -i 's/importlib/#importlib/g' requirements.*
sed -i 's/exceptiongroup/#exceptiongroup/g' requirements.*


%build
export NODE_OPTIONS="--max-old-space-size=5120"
export PYTHONPATH=$(pwd):$PYTHONPATH
mkdir -p indico/web/client
cd indico/web/client

npm config delete proxy
npm config delete http-proxy
npm config delete https-proxy

npm install
cd ../../../
npm install
export INDICO_NO_GIT=True
./bin/maintenance/build-wheel.py indico      --no-git  --ignore-unclean 
#Temporarily install Indico
export TMPINSTALL=$(pwd)
%{__python3} -m pip install dist/indico-3*-py3-none-any.whl  --root=%{buildroot} --no-dependencies --no-warn-script-location
export PYTHONPATH=%{buildroot}/%{python3_sitelib}:$PYTHONPATH
# Install all plugins 
%{__python3} -m pip install plugins/base/owncloud --root=%{buildroot} --no-dependencies
%{__python3} -m pip install plugins/base/themes_legacy --root=%{buildroot} --no-dependencies
%{__python3} -m pip install plugins/base/ursh --root=%{buildroot} --no-dependencies
%{__python3} -m pip install plugins/base/previewer_jupyter --root=%{buildroot} --no-dependencies
%{__python3} -m pip install plugins/base/piwik --root=%{buildroot} --no-dependencies
%{__python3} -m pip install plugins/base/cloud_captchas --root=%{buildroot} --no-dependencies
%{__python3} -m pip install plugins/base/vc_zoom --root=%{buildroot} --no-dependencies

# Create proper wheels for plugins
./bin/maintenance/build-wheel.py all-plugins --no-git  --ignore-unclean  plugins/base

%install
%{__python3} -m pip install dist/indico-3*-py3-none-any.whl  --root=%{buildroot} --no-dependencies --no-warn-script-location --force-reinstall
%{__python3} -m pip install dist/indico_plugin*-py3-none-any.whl     --root=%{buildroot} --no-dependencies --no-warn-script-location --force-reinstall
rm -rf  %{buildroot}/%{python3_sitelib}/indico_plugins-3.3.dev0.dist-info

%post 
indico i18n compile-catalog
indico i18n compile-catalog-react

# Note that there is no files section for the unversioned python module
%files -n python3-%{srcname}
%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/%{srcnamenu}/
%{_bindir}/indico
%exclude %{python3_sitelib}/%{srcnamenu}/web/static/images/globe.png
%exclude %{python3_sitelib}/%{srcnamenu}/web/static/images/logo_indico_bw.svg
%exclude %{python3_sitelib}/%{srcnamenu}/web/static/robots.txt
%exclude %{python3_sitelib}/%{srcnamenu}/modules/auth/templates/login_page.html
%exclude %{python3_sitelib}/%{srcnamenu}/modules/auth/templates/register.html

%files -n python3-%{srcname}-dummy
%{python3_sitelib}/%{srcnamenu}/web/static/images/globe.png
%{python3_sitelib}/%{srcnamenu}/web/static/images/logo_indico_bw.svg
%{python3_sitelib}/%{srcnamenu}/web/static/robots.txt
%{python3_sitelib}/%{srcnamenu}/modules/auth/templates/login_page.html
%{python3_sitelib}/%{srcnamenu}/modules/auth/templates/register.html


%filesinplugin citadel
%filesinplugin cloud_captchas
%filesinplugin livesync
#filesinplugin livesync_debug
%filesinplugin owncloud
%filesinplugin payment_manual
%filesinplugin payment_paypal
%filesinplugin payment_sixpay
%filesinplugin piwik
%filesinplugin previewer_code
%filesinplugin previewer_jupyter
%filesinplugin prometheus
%filesinplugin storage_s3
%filesinplugin themes_legacy
%filesinplugin ursh
%filesinplugin vc_dummy
%filesinplugin vc_zoom


%changelog
* Wed Feb 28 2024 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.3.0dev
- Version 3.3.0dev 
* Thu Feb 22 2024 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2.9
- Version 3.2.9 
* Mon May 15 2023 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2.3
- Version 3.2.3
* Thu Sep 01 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2
- Version 3.2
