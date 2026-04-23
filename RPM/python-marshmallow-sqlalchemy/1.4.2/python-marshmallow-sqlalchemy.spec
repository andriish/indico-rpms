%global srcname marshmallow_sqlalchemy
%global srcnamenu marshmallow-sqlalchemy

Name:           python-%{srcnamenu}
Version:        1.4.2
Release:        1%{?dist}
Summary:        SQLAlchemy integration with the marshmallow (de)serialization library

License:        MIT
URL:            https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
SQLAlchemy integration with the marshmallow (de)serialization library.}

%description %_description

%package -n python3-%{srcnamenu}
Summary:        %{summary}

%description -n python3-%{srcnamenu} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{srcname}

%files -n python3-%{srcnamenu} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%check
%pyproject_check_import

%changelog
* Thu Apr 23 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 1.4.2-1
- Initial version for Fedora
