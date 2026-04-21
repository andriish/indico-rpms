%global srcname pynpm
%global srcnamenu pynpm

Name:           python-%{srcname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Python interface to your NPM and package.json.

License:        BSD-3-Clause
URL:            https://pynpm.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel python-pytest-runner
BuildRequires:  python3-werkzeug gcc make
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%global _description %{expand:
Python interface to your NPM and package.json.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*.egg-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Mon Apr 21 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 0.3.0-1
- First version of 0.3.0 for Fedora