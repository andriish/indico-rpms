%global srcname captcha
%global srcnamenu captcha

Name:           python-%{srcname}
Version:        0.5.0
Release:        1%{?dist}
Summary:        A captcha library that generates audio and image CAPTCHAs.

License:        BSD
URL:            https://captcha.lepture.com/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel


%global _description %{expand:
A captcha library that generates audio and image CAPTCHAs.}

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
