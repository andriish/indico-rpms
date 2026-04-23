%global srcname wallet-py3k
%global modname wallet
%global srcnamenu wallet-py3k

Name:           python-%{srcnamenu}
Version:        0.0.4
Release:        1%{?dist}
Summary:        Python library to read/write [Apple Wallet]

License:        BSD-3-Clause
URL:            https://github.com/pretix/wallet-py3k
Source:         %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Python library to read/write [Apple Wallet]}

%description %_description

%package -n python3-%{srcnamenu}
Summary:        %{summary}

%description -n python3-%{srcnamenu} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%files -n python3-%{srcnamenu} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md
%doc CHANGES.txt


%changelog
* Fri Apr 17 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.0.4-1
- Initial version for Fedora
