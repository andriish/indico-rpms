%global srcname WTForms-dateutil
%global srcnamenu wtforms_dateutil

Name:           python-%{srcname}
Version:        0.1
Release:        1%{?dist}
Summary:        WTForms integration for dateutil

License:        BSD-3-Clause
URL:            https://github.com/wtforms/wtforms-dateutil/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
WTForms integration for dateutil.}

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
%license LICENSE.md

%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Mon Apr 20 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.1-1
- Initial version for Fedora
