%global srcname indico
%global srcnamenu indico

Name:           python-%{srcname}
Version:        3.1.1
Release:        1%{?dist}
Summary:        Indico package

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
Source:         https://github.com/indico/indico/archive/refs/tags/v%{version}.zip
Patch0:         indico-patch.txt
BuildArch:      noarch
BuildRequires:  git
BuildRequires:  indico-devel
BuildRequires:  python3-pip python3-wheel
Requires:       indico-devel

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
#sed -i 's/\=\=.*$//g' requirements.*
#sed -i 's/PREFERRED_PYTHON_VERSION_SPEC =.*/PREFERRED_PYTHON_VERSION_SPEC = \'~='{python3_version}'\'/g' indico/__init__.py
#sed -i 's/python_requires.*/python_requires \'~='{python3_version}'\'/g' setup.cfg
#sed -i 's/Programming\ Language\ ::\ Python ::\ .*/Programming\ Language\ ::\ Python\ ::\ '{python3_version}'/g' setup.cfg

%build
export NODE_OPTIONS="--max-old-space-size=5120"
export PYTHONPATH=$(pwd):$PYTHONPATH
mkdir -p indico/web/client
cd indico/web/client
npm install
cd ../../../
npm install
./bin/maintenance/build-wheel.py indico  --ignore-unclean 

%install
%{__python3} -m pip install dist/indico-%{version}-py3-none-any.whl  --root=%{buildroot} --no-dependencies --no-warn-script-location

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/%{srcnamenu}/
%{_bindir}/indico
