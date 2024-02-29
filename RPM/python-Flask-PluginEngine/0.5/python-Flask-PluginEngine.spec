%global srcname Flask-PluginEngine
%global srcnamenu flask_pluginengine

Name:           python-%{srcname}
Version:        0.5
Release:        1%{?dist}
Summary:        A simple plugin system for Flask applications. 

License:        BSD
URL:            https://flask-pluginengine.readthedocs.io/
Source:         https://github.com/indico/flask-pluginengine/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel 

%global _description %{expand:
 Flask-PluginEngine is an extension that provides interfaces to 
 create plugins and handle them within a Flask application. }

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n flask-pluginengine-%{version}

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
