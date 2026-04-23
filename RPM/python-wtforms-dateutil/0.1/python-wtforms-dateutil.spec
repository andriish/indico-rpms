%global srcname WTForms-dateutil
%global srcnamenu wtforms_dateutil

Name:           python-%{srcname}
Version:        0.1
Release:        1%{?dist}
Summary:        WTForms integration for dateutil

License:        BSD-3-Clause
URL:            https://github.com/wtforms/wtforms-dateutil/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
WTForms integration for dateutil.}

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
%license LICENSE.md

%check
%pyproject_check_import

%changelog
* Mon Apr 20 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.1-1
- Initial version for Fedora
