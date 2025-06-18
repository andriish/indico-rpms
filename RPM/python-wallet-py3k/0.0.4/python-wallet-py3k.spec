%global srcname wallet-py3k
%global srcnamenu wallet_py3k

Name:           python-%{srcname}
Version:        0.0.4
Release:        2%{?dist}
Summary:        Python library to read/write [Apple Wallet]

License:        BSD
URL:            https://captcha.lepture.com/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel


%global _description %{expand:
Python library to read/write [Apple Wallet]}

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

%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/wallet/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
