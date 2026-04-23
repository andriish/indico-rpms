%global srcname marshmallow_dataclass
%global srcnamenu marshmallow-dataclass

Name:           python-%{srcnamenu}
Version:        8.7.1
Release:        1%{?dist}
Summary:        Automatic generation of marshmallow schemas from dataclasses

License:        MIT
URL:            https://github.com/lovasoa/marshmallow_dataclass
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Python library to convert dataclasses into marshmallow schemas.}

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
%doc README.md
%license LICENSE

%check
%pytest --ignore tests/test_class_schema.py --ignore tests/test_collection.py

%changelog
* Tue Apr 21 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 8.7.1-1
- First version of 8.7.1 for Fedora
