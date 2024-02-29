%global srcname Flask-Multipass
%global srcnamenu flask_multipass

Name:           python-%{srcname}
Version:        0.5.3
Release:        1%{?dist}
Summary:        Flask with a user authentication/identity system

License:        BSD
URL:            https://flask-multipass.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel 

%global _description %{expand:
Flask-Multipass provides Flask with a user authentication/identity 
system which can use different backends (such as local users, LDAP and OAuth) simultaneously.}

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

%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
