%global srcname marshmallow-oneofschema
%global srcnamenu marshmallow_oneofschema

Name:           python-%{srcname}
Version:        3.2.0
Release:        1%{?dist}
Summary:        An extension to marshmallow to support schema (de)multiplexing.

License:        MIT
URL:            http://marshmallow.readthedocs.org/en/latest/
Source:         https://github.com/marshmallow-code/marshmallow-oneofschema/archive/refs/tags/3.2.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel

%global _description %{expand:
This library adds a special kind of schema that actually multiplexes 
other schemas based on object type. When serializing values, it uses 
get_obj_type() method to get object type name. Then it uses type_schemas 
name-to-Schema mapping to get schema for that particular object type, 
serializes object using that schema and adds an extra field with name
 of object type. Deserialization is reverse..}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools  python3-hatchling

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

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
