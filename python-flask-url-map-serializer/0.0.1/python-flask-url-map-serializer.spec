%global srcname flask-url-map-serializer
%global srcnamenu flask_url_map_serializer

Name:           python-%{srcname}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
Source:         https://github.com/indico/js-flask-urls/archive/refs/tags/babel-plugin-flask-urls@0.0.1.tar.gz
#{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel
BuildRequires: python3-werkzeug gcc make

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
%autosetup -n js-flask-urls-babel-plugin-flask-urls-0.0.1/flask-cli

%build
%py3_build

%install
%py3_install

%check
#{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

#{python3_sitelib}/#{srcnamenu}-*.egg-info/
%{python3_sitelib}/*

