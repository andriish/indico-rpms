%global srcname marshmallow_dataclass
%global srcnamenu marshmallow_dataclass

Name:           python-%{srcname}
Version:        8.6.0
Release:        1%{?dist}
Summary:        Automatic generation of marshmallow schemas from dataclasses.

License:        MIT
URL:            https://github.com/lovasoa/marshmallow_dataclass
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel python3-marshmallow-enum

%global _description %{expand:
Python library to convert dataclasses into marshmallow schemas.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}


%build
sed -i 's/3\.13\.0/3\.0\.0/g' marshmallow_dataclass.egg-info/requires.txt setup.py
#cat marshmallow_dataclass.egg-info/requires.txt
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
