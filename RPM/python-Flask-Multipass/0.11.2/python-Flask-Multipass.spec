%global srcname Flask-Multipass
%global srcnamenu flask_multipass

Name:           python-%{srcname}
Version:        0.11.2
Release:        1%{?dist}
Summary:        Flask with a user authentication/identity system

License:        BSD-3-Clause
URL:            https://flask-multipass.readthedocs.io/en/latest/
Source:         https://github.com/indico/flask-multipass/releases/download/v%{version}/flask_multipass-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-hatchling

%global _description %{expand:
Flask-Multipass provides Flask with a user authentication/identity 
system which can use different backends (such as local users, LDAP and OAuth) simultaneously.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcnamenu}-%{version}
sed -i 's/hatchling==1.28.0/hatchling>=1.28.0/g' pyproject.toml

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
* Thu Sep 29 2022 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.11.2-1
- Initial version for Fedora
