%define debug_package %{nil}
%global srcname indico-devel
%global srcnamenu indico-devel

Name:           indico-devel
Version:        3.1
Release:        5%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
Source:         indico-devel-3.1.tar.gz

#BuildArch:      noarch

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
Requires: python3-celery
Requires: python3-certifi
Requires: python3-cffi
Requires: python3-charset-normalizer
Requires: python3-click
Requires: python3-click-didyoumean
Requires: python3-click-plugins
Requires: python3-click-repl
Requires: python3-cryptography
Requires: python3-decorator
Requires: python3-distro
Requires: python3-dns
Requires: python3-email_validator
Requires: python3-executing
Requires: python3-feedgen
Requires: python3-flask
Requires: python3-flask-babel
Requires: python3-flask-caching
Requires: python3-Flask-Limiter
Requires: python3-flask-marshmallow
Requires: python3-flask-migrate
Requires: python3-Flask-Multipass
Requires: python3-Flask-PluginEngine
Requires: python3-flask-sqlalchemy
Requires: python3-flask-webpackext
Requires: python3-flask-wtf
Requires: python3-greenlet
Requires: python3-greenlet
Requires: python3-hiredis
Requires: python3-hiredis
Requires: python3-html2text
Requires: python3-html5lib
Requires: python3-icalendar
Requires: python3-idna
Requires: python3-importlib-metadata
Requires: python3-indico-fonts
Requires: python3-indico-fonts
Requires: python3-ipython
Requires: python3-itsdangerous
Requires: python3-jedi
Requires: python3-jinja2
Requires: python3-jsonschema
Requires: python3-kombu
Requires: python3-limits
Requires: python3-lxml
Requires: python3-mako
#Requires: python3-markdown_2
Requires: python3-markdown
Requires: python3-markupsafe
Requires: python3-marshmallow
Requires: python3-marshmallow-enum
Requires: python3-marshmallow-oneofschema
Requires: python3-marshmallow-sqlalchemy
Requires: python3-matplotlib-inline
Requires: python3-mypy_extensions
Requires: python3-node-semver
Requires: python3-packaging
Requires: python3-parso
Requires: python3-pexpect
Requires: python3-pickleshare
Requires: python3-pillow
Requires: python3-prompt-toolkit
Requires: python3-psycopg2
Requires: python3-ptyprocess
Requires: python3-pycountry
Requires: python3-pycparser
Requires: python3-pygments
Requires: python3-pynpm
Requires: python3-pyparsing
Requires: python3-PyPDF2
Requires: python3-pyrsistent
Requires: python3-dateutil
Requires: python3-pytz
Requires: python3-pywebpack
Requires: python3-pyyaml
Requires: python3-qrcode-core
Requires: python3-redis
Requires: python3-reportlab
Requires: python3-requests
Requires: python3-sentry-sdk
Requires: python3-simplejson
Requires: python3-six
Requires: python3-speaklater
#Requires: python3-sqlalchemy1.3
Requires: python3-sqlalchemy
Requires: python3-terminaltables
Requires: python3-traitlets
Requires: python3-translitcodec
Requires: python3-typing-extensions
Requires: python3-typing-inspect
Requires: python3-ua-parser
Requires: python3-urllib3
Requires: python3-vine
Requires: python3-wcwidth
Requires: python3-webargs
Requires: python3-webencodings
Requires: python3-werkzeug
Requires: python3-wtforms >= 3.0.0
Requires: python3-WTForms-dateutil
Requires: python3-WTForms-SQLAlchemy
Requires: python3-zipp
Requires: uwsgi
Requires: uwsgi-plugin-python3
Requires: uwsgi-plugin-python3-gevent 

Requires: python3-pure-eval
Requires: python3-marshmallow_dataclass

Requires: postgresql postgresql-server postgresql-libs postgresql-devel postgresql-contrib
Requires: git gcc make redis httpd mod_proxy_uwsgi mod_ssl mod_xsendfile
Requires: libjpeg-turbo-devel libxslt-devel libxml2-devel libffi-devel pcre-devel libyaml-devel zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils libuuid-devel


Requires: rpm-build git wget python3-rpm-macros
Requires: npm

Requires: python3-xlsxwriter

Requires: python-flask-url-map-serializer
 
%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

%description %_description

#package -n {srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools



%prep
%setup -q  -c

%build

%install
mkdir -p %{buildroot}/bin/
install -m 755  indico-devel-version %{buildroot}/bin/

%files -n %{srcname}
/bin/indico-devel-version
