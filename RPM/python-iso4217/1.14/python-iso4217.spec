%global srcname iso4217
%global srcnamenu iso4217

Name:           python-%{srcname}
Version:        1.14
Release:        1%{?dist}
Summary:        ISO 4217 currency data package for Python 

License:        Public Domain
URL:            https://github.com/dahlia/iso4217
Source:         https://github.com/dahlia/iso4217/archive/refs/tags/1.14.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel

%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

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

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*.egg-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
