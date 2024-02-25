%global srcname email_validator
%global srcnamenu email_validator

Name:           python-%{srcname}
Version:        1.2.1
Release:        3%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://github.com/JoshData/python-email-validator
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel

%global _description %{expand:
A robust email address syntax and deliverability validation library for Python by Joshua Tauberer.}

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
%{_bindir}/email_validator

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
