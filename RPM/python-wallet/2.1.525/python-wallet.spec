%global srcname wallet
%global srcnamenu wallet

Name:           python-%{srcname}
Version:         2.1.525
Release:        1%{?dist}
Summary:        OpenAPI compliant library to access resources on the Wallet Inc. Platform

License:         MIT
URL:            https://pynpm.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel python-pytest-runner
BuildRequires: python3-werkzeug gcc make

%global _description %{expand:
Python interface to your NPM and package.json.}

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
