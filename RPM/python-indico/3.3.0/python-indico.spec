%global srcname indico
%global srcnamenu indico
%global igittag 1a4ed25f80ffd3b93b804036c4d593e087f9f055
%global pgittag bece9eec553ee0cec9667c6dcef6ef6498e1093c

Name:           python-%{srcname}
Version:        3.3.0
Release:        8%{?dist}
Summary:        Indico package

License:        MIT
URL:            https://getindico.io/
Source0:        https://github.com/indico/indico/archive/%{igittag}.zip
Source1:        https://github.com/indico/indico-plugins/archive/%{pgittag}.tar.gz
Patch0:         indico-patch.txt
BuildArch:      noarch

BuildRequires: indico-devel
BuildRequires: nodejs-npm
BuildRequires: python-build
BuildRequires: python3-pip python3-wheel
Requires: indico-devel==3.3.0
BuildRequires: python3-rpm-macros
BuildRequires: gcc-c++ git gcc make 
BuildRequires: rpm-build git wget python3-rpm-macros
BuildRequires: npm


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
#Requires: tex(rawlatex.sty)
Requires: tex(microtype.sty)
Requires: tex(needspace.sty)
Requires: tex(parskip.sty)
Requires: tex(scrextend.sty)
Requires: tex(sectsty.sty)
Requires: tex(tcolorbox.sty)
Requires: tex(truncate.sty)
Requires: tex(xcolor.sty)
Requires: tex(xstring.sty)

%global _description %{expand:
Indico event management system.
}
%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%description -n python3-%{srcname} %_description

%package -n python3-%{srcname}-plugins
Summary:        %{summary}
Requires: python3-%{srcname}
%description -n python3-%{srcname}-plugins %_description

%package -n python3-%{srcname}-dummy
Summary:        %{summary}
Requires: python3-%{srcname}
%description -n python3-%{srcname}-dummy %_description


%prep
%autosetup  -n indico-%{igittag} -p 1
%setup -q -T -D -a 1 -n indico-%{igittag}
mkdir -p plugins
mv indico-plugins-%{pgittag} plugins/base

set -x
sed -i "s/python_requires.*/python_requires\ =\ \~="%{python3_version}"/g" plugins/base/*/setup.cfg
sed -i 's/iso4217\=\=.*$/iso4217/g'     plugins/base/*/setup.cfg
sed -i 's/nbconvert\=\=.*$/nbconvert/g' plugins/base/*/setup.cfg

sed -i '/# BEGIN GENERATED REQUIREMENTS/,/# END GENERATED REQUIREMENTS/d' plugins/base/_meta/setup.cfg

%py3_shebang_fix ./

sed -i 's/\=\=.*$//g' requirements.*
sed -i 's/tzdata/#tzdata/g' requirements.*
sed -i 's/pypdf/#pypdf/g' requirements.*
sed -i 's/importlib/#importlib/g' requirements.*


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

%files -n python3-%{srcname}-plugins
%{python3_sitelib}/%{srcnamenu}_*/

%changelog
* Wed Feb 28 2024 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.3.0dev
- Version 3.3.0dev 
* Thu Feb 22 2024 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2.9
- Version 3.2.9 
* Mon May 15 2023 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2.3
- Version 3.2.3
* Thu Sep 01 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2
- Version 3.2
