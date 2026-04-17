%global srcname flask-marshmallow
%global srcnamenu flask_marshmallow

Name:           python-%{srcname}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Flask + marshmallow for beautiful APIs

License:        MIT
URL:            https://flask-marshmallow.readthedocs.io/en/latest/
Source:         https://github.com/marshmallow-code/flask-marshmallow/archive/refs/tags/1.4.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel pyproject-rpm-macros
BuildRequires:  python3-werkzeug gcc make
BuildRequires:  python3-devel pyproject-rpm-macros
BuildRequires:  python3-setuptools  python3-hatchling python-flit-core


%global _description %{expand:
Flask-Marshmallow is a thin integration layer for Flask (a Python web 
framework) and marshmallow (an object serialization/deserialization 
library) that adds additional features to marshmallow, including URL 
and Hyperlinks fields for HATEOAS-ready APIs. It also (optionally) 
integrates with Flask-SQLAlchemy.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
#{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*.dist-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
