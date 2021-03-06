%global srcname indico
%global srcnamenu indico

Name:           python-%{srcname}
Version:        3.1.1
Release:        13%{?dist}
Summary:        Indico package

License:        MIT
URL:            https://getindico.io/
Source0:        https://github.com/indico/indico/archive/refs/tags/v%{version}.zip
Source1:        https://github.com/indico/indico-plugins/archive/refs/tags/v%{version}.tar.gz
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

%package -n python3-%{srcname}-plugins
Summary:        %{summary}
Requires:  python3-%{srcname}

%description -n python3-%{srcname}-plugins %_description

%package -n python3-%{srcname}-dummy
Summary:        %{summary}
Requires:  python3-%{srcname}

%description -n python3-%{srcname}-dummy %_description


%prep
%autosetup  -n indico-%{version} -p 1
%setup -q -T -D -a 1 -n indico-%{version} 
mkdir -p plugins
mv indico-plugins-%{version} plugins/base
rm -rf plugins/base/piwik
rm -rf plugins/base/themes_legacy
rm -rf plugins/base/ursh
rm -rf plugins/base/vc_zoom
set -x
sed -i "s/python_requires.*/python_requires\ =\ \~="%{python3_version}"/g" plugins/base/*/setup.cfg
sed -i 's/Programming\ Language\ ::\ Python ::\ .*/Programming\ Language\ ::\ Python\ ::\ '%{python3_version}'/g' plugins/base/*/setup.cfg
sed -i 's/iso4217\=\=.*$/iso4217/g'     plugins/base/*/setup.cfg
sed -i 's/nbconvert\=\=.*$/nbconvert/g' plugins/base/*/setup.cfg
sed -i 's/indico-plugin-piwik.*$//g'    plugins/base/_meta/setup.cfg
sed -i 's/indico-plugin-ursh.*$//g'     plugins/base/_meta/setup.cfg
sed -i 's/indico-plugin-vc-zoom.*$//g'  plugins/base/_meta/setup.cfg
#exit

sed -i 's/\=\=.*$//g' requirements.*
#sed -i 's/PREFERRED_PYTHON_VERSION_SPEC =.*/PREFERRED_PYTHON_VERSION_SPEC = \'~='{python3_version}'\'/g' indico/__init__.py


%build
export NODE_OPTIONS="--max-old-space-size=5120"
export PYTHONPATH=$(pwd):$PYTHONPATH
#exit
mkdir -p indico/web/client
cd indico/web/client
npm install
cd ../../../
npm install
./bin/maintenance/build-wheel.py indico       --ignore-unclean 
./bin/maintenance/build-wheel.py all-plugins  --ignore-unclean  plugins/base

%install
%{__python3} -m pip install dist/indico-%{version}-py3-none-any.whl  --root=%{buildroot} --no-dependencies --no-warn-script-location
%{__python3} -m pip install dist/indico_plugin*-py3-none-any.whl     --root=%{buildroot} --no-dependencies --no-warn-script-location

#/usr/lib/python3.10/site-packages/indico/web/static/images/globe.png

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/%{srcnamenu}/
%{_bindir}/indico
%exclude %{python3_sitelib}/%{srcnamenu}/web/static/images/globe.png
%exclude %{python3_sitelib}/%{srcnamenu}/web/static/images/logo_indico_bw.png
%exclude %{python3_sitelib}/%{srcnamenu}/modules/auth/templates/login_page.html
%exclude %{python3_sitelib}/%{srcnamenu}/modules/auth/templates/register.html
%exclude %{python3_sitelib}/%{srcnamenu}/modules/auth/forms.py
%exclude %{python3_sitelib}/%{srcnamenu}/modules/auth/__pycache__/forms*pyc

%files -n python3-%{srcname}-dummy
%{python3_sitelib}/%{srcnamenu}/web/static/images/globe.png
%{python3_sitelib}/%{srcnamenu}/web/static/images/logo_indico_bw.png
%{python3_sitelib}/%{srcnamenu}/modules/auth/templates/login_page.html
%{python3_sitelib}/%{srcnamenu}/modules/auth/templates/register.html
%{python3_sitelib}/%{srcnamenu}/modules/auth/forms.py
%{python3_sitelib}/%{srcnamenu}/modules/auth/__pycache__/forms*pyc


%files -n python3-%{srcname}-plugins
%{python3_sitelib}/%{srcnamenu}_*/
