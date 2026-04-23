%global srcname indico
%global srcnamenu indico
%global pluginsversion 3.3.6
%define iplugin()  \
%%package -n python3-indico-%1-plugin \
Summary:        Indico plugin %1  \
Requires: python3-indico \
%%description -n python3-indico-%1-plugin \
Indico plugin %1 

%define filesinplugin() \
%%files -n python3-indico-%1-plugin \
%{python3_sitelib}/indico_%1/* \
%{python3_sitelib}/indico_plugin_%1-3.*.dist-info/*


Name:           python-%{srcname}
Version:        3.3.12
Release:        1%{?dist}
Summary:        Indico event management system

License:        MIT
URL:            https://getindico.io/
Source0:        https://github.com/indico/indico/archive/refs/tags/v%{version}.zip
Source1:        https://github.com/indico/indico-plugins/archive/refs/tags/v%{pluginsversion}.tar.gz
BuildArch:      noarch

BuildRequires: nodejs-npm
BuildRequires: python-build
BuildRequires: gcc-c++ gcc make 
BuildRequires: git wget
BuildRequires: npm
BuildRequires: tzdata
BuildRequires: python3-rpm-macros
BuildRequires: libjpeg-turbo-devel libxslt-devel libxml2-devel libffi-devel libyaml-devel 
BuildRequires: zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils libuuid-devel
BuildRequires: uv ruff 
%if 0%{?fedora} < 44
BuildRequires: pcre-devel
%else
BuildRequires: pcre2-devel
%endif

BuildRequires:   python3-flask-url-map-serializer

%global _description %{expand:
Indico event management system.
}
%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

Requires: tzdata
Requires: zlib bzip2 readline sqlite xz libffi findutils libuuid
Requires: uwsgi
Requires: uwsgi-plugin-python3
Requires: uwsgi-plugin-python3-gevent 
Requires: liberation-mono-fonts
Requires: liberation-sans-fonts
Requires: liberation-serif-fonts
Requires: linux-libertine-biolinum-fonts
Requires: linux-libertine-fonts
Requires: google-noto-sans-cjk-vf-fonts 
Requires: google-noto-sans-cjk-fonts
Requires: sazanami-gothic-fonts
Requires: sazanami-mincho-fonts  
Requires: cjkuni-uming-fonts

%description -n python3-%{srcname} %_description

%package -n python3-indico-default-resources
Summary:  %{summary}
Requires: python3-%{srcname}

%description -n python3-indico-default-resources
Default configuration files for Indico


%iplugin citadel
%iplugin cloud_captchas
%iplugin livesync
%iplugin owncloud
%iplugin payment_manual
%iplugin payment_paypal
%iplugin payment_sixpay
%iplugin payment_stripe
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
%autosetup  -n indico-%{version} -p 1
%setup -q -T -D -a 1 -n indico-%{version}
mkdir -p plugins
mv indico-plugins-%{pluginsversion} plugins/base
rm -rf plugins/base/livesync_debug

%py3_shebang_fix ./

sed -i 's/\=\=.*$//g' requirements.*
sed -i 's/tzdata/#tzdata/g' requirements.*
sed -i 's/importlib/#importlib/g' requirements.*
sed -i 's/indico-fonts/#indico-fonts/g' requirements.*
sed -i 's/exceptiongroup/#exceptiongroup/g' requirements.*

sed -i -E "s/^requires-python[[:space:]]*=.*/requires-python = '>=3.12'/" pyproject.toml plugins/base/*/pyproject.toml
sed -i -E "s/Python :: 3.12/Python :: "%{python3_version}"/g" pyproject.toml plugins/base/*/pyproject.toml
sed -i -E "s/hatchling==/hatchling>=/g" pyproject.toml plugins/base/*/pyproject.toml
sed -i -E "s/hatch-requirements-txt==/hatch-requirements-txt>=/g" pyproject.toml plugins/base/*/pyproject.toml
sed -i -E "s/babel==/babel>=/g" pyproject.toml plugins/base/*/pyproject.toml


%generate_buildrequires
%pyproject_buildrequires

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
mkdir -p src
./bin/maintenance/build-wheel.py all-plugins --no-git  --ignore-unclean  plugins/base

%install
%{__python3} -m pip install dist/indico-3*-py3-none-any.whl  --root=%{buildroot} --no-dependencies --no-warn-script-location --force-reinstall
%{__python3} -m pip install dist/indico_plugin*-py3-none-any.whl     --root=%{buildroot} --no-dependencies --no-warn-script-location --force-reinstall
rm -rf  %{buildroot}/%{python3_sitelib}/indico_plugins-%{pluginsversion}.dist-info

%post 
indico i18n compile-catalog
indico i18n compile-catalog-react

%files -n python3-%{srcname}
%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/%{srcnamenu}/
%{_bindir}/indico
%exclude %{python3_sitelib}/%{srcnamenu}/web/static/images/logo_indico_bw.svg
%exclude %{python3_sitelib}/%{srcnamenu}/web/static/robots.txt
%exclude %{python3_sitelib}/%{srcnamenu}/modules/auth/templates/register.html

%files -n python3-indico-default-resources
%{python3_sitelib}/%{srcnamenu}/web/static/images/logo_indico_bw.svg
%{python3_sitelib}/%{srcnamenu}/web/static/robots.txt
%{python3_sitelib}/%{srcnamenu}/modules/auth/templates/register.html


%filesinplugin citadel
%filesinplugin cloud_captchas
%filesinplugin livesync
#filesinplugin livesync_debug
%filesinplugin owncloud
%filesinplugin payment_manual
%filesinplugin payment_paypal
%filesinplugin payment_sixpay
%filesinplugin payment_stripe
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
* Thu Mar 26 2026 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.3.12-1
- Version 3.3.12 for Fedora 

