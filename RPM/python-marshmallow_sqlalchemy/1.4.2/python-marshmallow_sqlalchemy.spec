%global srcname marshmallow-sqlalchemy
%global srcnamenu marshmallow_sqlalchemy

Name:           python-%{srcname}
Version:        1.4.2
Release:        1%{?dist}
Summary:        SQLAlchemy integration with the marshmallow (de)serialization library.

License:        MIT
URL:            https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/1d/8c/861ed468b99773866d59e315a73a02538f503c99167d24b3b3f1c8e0242c/marshmallow_sqlalchemy-1.4.2.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel

%global _description %{expand:
SQLAlchemy integration with the marshmallow (de)serialization library.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools  python3-hatchling  python-flit-core

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcnamenu}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*.dist-info/
%{python3_sitelib}/%{srcnamenu}/


%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
