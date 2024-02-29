%global srcname marshmallow-sqlalchemy
%global srcnamenu marshmallow_sqlalchemy

Name:           python-%{srcname}
Version:        0.29.0
Release:        1%{?dist}
Summary:        SQLAlchemy integration with the marshmallow (de)serialization library.

License:        MIT
URL:            https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel

%global _description %{expand:
SQLAlchemy integration with the marshmallow (de)serialization library.}

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

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*.egg-info/
%{python3_sitelib}/%{srcnamenu}/


%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
