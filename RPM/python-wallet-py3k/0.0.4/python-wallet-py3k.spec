%global srcname wallet-py3k
%global srcnamenu wallet_py3k

Name:           python-%{srcname}
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

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcnamenu}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.txt
%doc CHANGES.txt


%changelog
* Fri Apr 17 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.0.4-1
- Initial version for Fedora
