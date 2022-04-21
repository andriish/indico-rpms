#URL:            https://github.com/ua-parser/uap-python
#Source:         https://files.pythonhosted.org/packages/source/u/{_pkgname}/{_pkgname}-{version}.tar.gz

%global srcname indico
%global srcnamenu indico

Name:           python-%{srcname}
Version:        3.1
Release:        1%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
#Source:         {pypi_source}
Source:         https://github.com/indico/indico/archive/refs/tags/v3.1.zip
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel



#alembic
#authlib>=1.0.0a1  # new oauth provider needs this prerelease authlib
#babel
BuildRequires:  babel
#bcrypt
BuildRequires:  python3-bcrypt
#bleach
BuildRequires:  python3-bleach
#blinker
#celery[redis]!=5.2.3  # 5.2.3 pins setuptools which is a mess
#certifi
BuildRequires:  python3-certifi
#click
#distro
#email-validator
BuildRequires:  python3-email_validator
#feedgen
#flask-babel
#flask-caching
#flask-limiter
#flask-marshmallow
#flask-migrate
#flask-multipass
#flask-pluginengine
#flask-sqlalchemy
#flask-webpackext
#flask-wtf
#flask
#html2text
#icalendar
#indico-fonts
#ipython!=8.0.*  # 8.0 auto-blacks the code and has kind of broken autocompletion
#itsdangerous
#jinja2
#jsonschema
#lxml[html5]
#markdown
#markupsafe
#marshmallow-dataclass[enum]
#marshmallow-enum
#marshmallow-oneofschema
#marshmallow-sqlalchemy
#marshmallow
#packaging
#pillow
#prompt-toolkit
#psycopg2
#pycountry
#pygments
#pypdf2
#python-dateutil
#pytz
#pywebpack
#pyyaml
#qrcode
#redis[hiredis]
#reportlab
#requests
#sentry-sdk[flask,celery,sqlalchemy,pure_eval]
#simplejson
#speaklater
#sqlalchemy
#terminaltables
#translitcodec
#ua-parser
#webargs
#werkzeug
#wtforms[email]
#wtforms-dateutil
#wtforms-sqlalchemy
#xlsxwriter
BuildRequires: python3-xlsxwriter



%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n v3.1

%build
%py3_build

%install
%py3_install

%check
#{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
#license COPYING
#doc README.rst
%{python3_sitelib}/%{srcnamenu}-*.egg-info/
%{python3_sitelib}/%{srcnamenu}/
#{_bindir}/sample-exec
