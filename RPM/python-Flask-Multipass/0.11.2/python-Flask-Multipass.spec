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

# -------------------------
# BuildRequires for extras
# -------------------------

# authlib extra
BuildRequires:  python3-authlib >= 0.14.1
BuildRequires:  python3-requests

# ldap extra
BuildRequires:  python3-flask-wtf
BuildRequires:  python3-ldap >= 3.3.1

# saml extra
BuildRequires:  python3-saml >= 1.10.1

# sqlalchemy extra
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-flask-wtf

%global _description %{expand:
Flask-Multipass provides Flask with a user authentication/identity 
system which can use different backends (such as local users, LDAP and OAuth) simultaneously.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

# -------------------------
# Optional dependency extras
# -------------------------

# authlib extra
%package -n python3-%{srcname}+authlib
Summary:        Authlib support for Flask-Multipass
Requires:       python3-authlib >= 0.14.1
Requires:       python3-requests

%description -n python3-%{srcname}+authlib
Optional Authlib authentication backend for Flask-Multipass.

# ldap extra
%package -n python3-%{srcname}+ldap
Summary:        LDAP support for Flask-Multipass
Requires:       python3-flask-wtf
Requires:       python3-ldap >= 3.3.1

%description -n python3-%{srcname}+ldap
Optional LDAP authentication backend for Flask-Multipass.

# saml extra
%package -n python3-%{srcname}+saml
Summary:        SAML support for Flask-Multipass
Requires:       python3-saml >= 1.10.1

%description -n python3-%{srcname}+saml
Optional SAML authentication backend for Flask-Multipass.

# sqlalchemy extra
%package -n python3-%{srcname}+sqlalchemy
Summary:        SQLAlchemy support for Flask-Multipass
Requires:       python3-sqlalchemy
Requires:       python3-flask-wtf

%description -n python3-%{srcname}+sqlalchemy
Optional SQLAlchemy integration for Flask-Multipass.


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

# -------------------------
# Files for extras
# -------------------------

%files -n python3-%{srcname}+authlib
# No files — this subpackage only adds Requires:

%files -n python3-%{srcname}+ldap
# No files — this subpackage only adds Requires:

%files -n python3-%{srcname}+saml
# No files — this subpackage only adds Requires:

%files -n python3-%{srcname}+sqlalchemy
# No files — this subpackage only adds Requires:

%check
%pyproject_check_import

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.11.2-1
- Initial version for Fedora
