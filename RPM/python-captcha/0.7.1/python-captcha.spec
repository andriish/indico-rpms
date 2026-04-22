%global srcname captcha
%global srcnamenu captcha

Name:           python-%{srcname}
Version:        0.7.1
Release:        1%{?dist}
Summary:        A captcha library that generates audio and image CAPTCHAs

License:        BSD-3-Clause
URL:            https://captcha.lepture.com/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
A captcha library that generates audio and image CAPTCHAs.}

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
%license LICENSE

%check
%pytest

%changelog
* Mon Apr 20 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.7.1-1
- Initial version for Fedora
