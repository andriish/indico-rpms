%global srcname Flask-PluginEngine
%global srcnamenu flask_pluginengine

Name:           python-%{srcname}
Version:        0.4
Release:        1%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
Source:         https://github.com/indico/flask-pluginengine/archive/refs/tags/v0.4.tar.gz
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel 

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
%autosetup -n flask-pluginengine-0.4

%build
%py3_build

%install
%py3_install

%check
#{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{srcnamenu}/
#{_bindir}/email_validator
