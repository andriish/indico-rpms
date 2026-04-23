%global srcname flask_limiter
%global srcnamenu flask-limiter

Name:           python-%{srcnamenu}
Version:        4.1.1
Release:        1%{?dist}
Summary:        Provides rate limiting features to Flask applications

License:        MIT
URL:            https://flask-limiter.readthedocs.io/en/stable/
Source:         %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Flask-Limiter provides rate limiting features to Flask applications.}

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

%pyproject_save_files -l %{srcname}

%files -n python3-%{srcnamenu} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%check
%pyproject_check_import

%changelog
* Thu Apr 23 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 4.1.1-1
- First Fedora package release for python-flask_limiter 4.1.1
