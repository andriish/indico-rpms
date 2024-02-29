%global srcname flask-marshmallow
%global srcnamenu flask_marshmallow

Name:           python-%{srcname}
Version:        0.15.0
Release:        1%{?dist}
Summary:        Flask + marshmallow for beautiful APIs

License:        MIT
URL:            https://flask-marshmallow.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel
BuildRequires: python3-werkzeug gcc make

%global _description %{expand:
Flask-Marshmallow is a thin integration layer for Flask (a Python web 
framework) and marshmallow (an object serialization/deserialization 
library) that adds additional features to marshmallow, including URL 
and Hyperlinks fields for HATEOAS-ready APIs. It also (optionally) 
integrates with Flask-SQLAlchemy.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
#{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*.egg-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
