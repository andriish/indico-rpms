%global srcname webargs
%global srcnamenu webargs

Name:           python-%{srcname}
Version:        8.7.1
Release:        1%{?dist}
Summary:        A Python library for parsing and validating HTTP request objects

License:        MIT
URL:            https://webargs.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-werkzeug 

%global _description %{expand:
webargs is a Python library for parsing and validating HTTP request 
objects, with built-in support for popular web frameworks, including 
Flask, Django, Bottle, Tornado, Pyramid, Falcon, and aiohttp..}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE



%changelog
* Fri Apr 17 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 8.7.1-1
- Initial version for Fedora
