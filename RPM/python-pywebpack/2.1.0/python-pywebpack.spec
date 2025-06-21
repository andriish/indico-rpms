%global srcname pywebpack
%global srcnamenu pywebpack

Name:           python-%{srcname}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Webpack integration layer for Python.

License:        MIT
URL:            https://pywebpack.readthedocs.io/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel python-pytest-runner
BuildRequires: python3-werkzeug gcc make

%global _description %{expand:
Webpack integration layer for Python.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p 1

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
