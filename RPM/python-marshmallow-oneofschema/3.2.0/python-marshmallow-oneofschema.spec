%global srcname marshmallow_oneofschema
%global srcnamenu marshmallow-oneofschema

Name:           python-%{srcnamenu}
Version:        3.2.0
Release:        1%{?dist}
Summary:        An extension to marshmallow to support schema (de)multiplexing

License:        MIT
URL:            http://marshmallow.readthedocs.org/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
This library adds a special kind of schema that actually multiplexes 
other schemas based on object type. When serializing values, it uses 
get_obj_type() method to get object type name. Then it uses type_schemas 
name-to-Schema mapping to get schema for that particular object type, 
serializes object using that schema and adds an extra field with name
 of object type. Deserialization is reverse.}

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
%doc CHANGELOG.rst
%doc README.rst
%license LICENSE

%check
%pytest

%changelog
* Tue Apr 21 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 3.2.0-1
- First version of 3.2.0 for Fedora
