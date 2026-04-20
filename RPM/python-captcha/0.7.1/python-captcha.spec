%global srcname captcha
%global srcnamenu captcha

Name:           python-%{srcname}
Version:        0.7.1
Release:        1%{?dist}
Summary:        A captcha library that generates audio and image CAPTCHAs.

License:        BSD-3-Clause
URL:            https://captcha.lepture.com/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
A captcha library that generates audio and image CAPTCHAs.}

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
%license LICENSE

%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Mon Apr 20 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.7.1-1
- Initial version for Fedora
