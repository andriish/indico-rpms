%global srcname pynpm
%global srcnamenu pynpm

Name:           python-%{srcname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Python interface to your NPM and package.json

License:        BSD-3-Clause
URL:            https://pynpm.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-werkzeug gcc make

%global _description %{expand:
Python interface to your NPM and package.json.}

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

%pyproject_save_files -l %{srcnamenu}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%doc CHANGES.rst
%license LICENSE

%check
%pyproject_check_import

%changelog
* Wed Apr 22 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 0.3.0-1
- First version of 0.3.0 for Fedora
