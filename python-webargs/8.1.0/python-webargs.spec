%global srcname webargs
%global srcnamenu webargs

Name:           python-%{srcname}
Version:        8.1.0
Release:        1%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel
BuildRequires: python3-werkzeug

%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

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
