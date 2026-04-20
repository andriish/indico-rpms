%global srcname pywebpack
%global srcnamenu pywebpack

Name:           python-%{srcname}
Version:        2.2.1
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

%files -n python3-%{srcname}
%license LICENSE

%{python3_sitelib}/%{srcnamenu}-*.egg-info/
%{python3_sitelib}/%{srcnamenu}/


%changelog
* Mon Apr 20 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 2.2.1- 1
- First version of 2.2.1 for Fedora
