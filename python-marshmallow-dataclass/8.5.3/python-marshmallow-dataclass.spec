%global srcname marshmallow_dataclass
%global srcnamenu marshmallow_dataclass

Name:           python-%{srcname}
Version:        8.5.3
Release:        3%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel python3-marshmallow-enum

%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description
#pyproject_extras_subpkg -n python3-marshmallow-dataclass enum

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
