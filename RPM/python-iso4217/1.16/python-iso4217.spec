%global srcname iso4217
%global srcnamenu iso4217

Name:           python-%{srcname}
Version:        1.16
Release:        1%{?dist}
Summary:        ISO 4217 currency data package for Python 

License:        LicenseRef-Fedora-Public-Domain
URL:            https://github.com/dahlia/iso4217
Source:         https://github.com/dahlia/iso4217/archive/refs/tags/1.16.tar.gz
BuildArch:      noarch

%global _description %{expand:
ISO 4217 currency data package for Python.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
echo "Distributed under Public Domain." > LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{srcnamenu}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%check
%pyproject_check_import

%changelog
* Tue Apr 21 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 1.16-1
- First version of 1.16 for Fedora
