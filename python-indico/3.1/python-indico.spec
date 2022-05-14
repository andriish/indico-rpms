%global srcname indico
%global srcnamenu indico

Name:           python-%{srcname}
Version:        3.1
Release:        5%{?dist}
Summary:        Indico package

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
#Source:        {pypi_source}
Source:         https://github.com/indico/indico/archive/refs/tags/v%{version}.zip
Patch0:         indico-patch.txt
BuildArch:      noarch
BuildRequires:  npm
BuildRequires:  git
BuildRequires:  redis
BuildRequires:  indico-devel
BuildRequires:  python3-pip python3-wheel

BuildRequires:  babel
BuildRequires:  python3-bcrypt
BuildRequires:  python3-bleach
BuildRequires:  python3-certifi
BuildRequires:  python3-email_validator
BuildRequires:  python3-xlsxwriter

BuildRequires: python3-celery
BuildRequires: python3-lxml
BuildRequires: python3-marshmallow-enum
BuildRequires: python3-redis
BuildRequires: python3-wtforms

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
%autosetup -n indico-%{version} -p 1
sed -i 's/\=\=.*$//g' requirements.*

%build
export NODE_OPTIONS="--max-old-space-size=5120"
export PYTHONPATH=$(pwd):$PYTHONPATH
mkdir -p indico/web/client
cd indico/web/client
npm install
cd ../../../
npm install
./bin/maintenance/build-wheel.py indico  --ignore-unclean 
#--no-assets --add-version-suffix
#./bin/maintenance/build-assets.py indico 
#--add-version-suffix --ignore-unclean --no-assets
#py3_build

%install
#py3_install
python3 -m pip install dist/indico-%{version}-py3-none-any.whl  --root=%{buildroot} --no-dependencies

%check
#{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/%{srcnamenu}/
%{_bindir}/indico
