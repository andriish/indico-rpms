%global srcname iso4217
%global srcnamenu iso4217

Name:           python-%{srcname}
Version:        1.16
Release:        1%{?dist}
Summary:        ISO 4217 currency data package for Python 

License:        Public Domain
URL:            https://github.com/dahlia/iso4217
Source:         https://github.com/dahlia/iso4217/archive/refs/tags/1.16.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel

%global _description %{expand:
ISO 4217 currency data package for Python.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides: python%{python3_version}dist(iso4217)

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
* Tue Apr 21 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 1.16-1
- First version of 1.16 for Fedora
