%global srcname flask_webpackext
%global srcnamenu flask-webpackext

Name:           python-%{srcnamenu}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Webpack integration for Flask

License:        BSD-3-Clause
URL:            https://flask-webpackext.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-werkzeug gcc make
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Flask-WebpackExt makes it easy to interface with your existing Webpack 
project from Flask and does not try to manage Webpack for you. }

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
%doc CHANGES.rst
%license LICENSE

%check
%pyproject_check_import

%changelog
* Wed Apr 22 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 2.1.0-1
- First version of 2.1.0 for Fedora
