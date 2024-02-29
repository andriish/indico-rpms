%global srcname webargs
%global srcnamenu webargs

Name:           python-%{srcname}
Version:        8.3.0
Release:        1%{?dist}
Summary:        A Python library for parsing and validating HTTP request objects

License:        MIT
URL:            https://webargs.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel
BuildRequires: python3-werkzeug

%global _description %{expand:
webargs is a Python library for parsing and validating HTTP request 
objects, with built-in support for popular web frameworks, including 
Flask, Django, Bottle, Tornado, Pyramid, Falcon, and aiohttp..}

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
