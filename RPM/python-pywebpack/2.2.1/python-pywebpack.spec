%global srcname pywebpack
%global srcnamenu pywebpack

Name:           python-%{srcname}
Version:        2.2.1
Release:        1%{?dist}
Summary:        Webpack integration layer for Python

License:        MIT
URL:            https://pywebpack.readthedocs.io/
Source:         %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Webpack integration layer for Python.}

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
%license LICENSE
%doc README.rst
%doc CHANGES.rst

%check
%pyproject_check_import

%changelog
* Mon Apr 20 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 2.2.1-1
- First version of 2.2.1 for Fedora
