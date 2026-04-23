%global srcname flask_multipass
%global srcnamenu flask-multipass
%global modname flask_multipass

Name:           python-%{srcnamenu}
Version:        0.11.2
Release:        1%{?dist}
Summary:        Flask with a user authentication/identity system

License:        BSD-3-Clause
URL:            https://flask-multipass.readthedocs.io/en/latest/
Source:         %{pypi_source}
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

%package -n python3-%{srcnamenu}
Summary:        %{summary}

%description -n python3-%{srcnamenu} %_description

# -------------------------
# Optional dependency extras
# -------------------------

# authlib extra
%package -n python3-%{srcnamenu}+authlib
Summary:        Authlib support for Flask-Multipass
Requires:       python3-authlib >= 0.14.1
Requires:       python3-requests

%description -n python3-%{srcnamenu}+authlib
Optional Authlib authentication backend for Flask-Multipass.

# ldap extra
%package -n python3-%{srcnamenu}+ldap
Summary:        LDAP support for Flask-Multipass
Requires:       python3-flask-wtf
Requires:       python3-ldap >= 3.3.1

%description -n python3-%{srcnamenu}+ldap
Optional LDAP authentication backend for Flask-Multipass.

# saml extra
%package -n python3-%{srcnamenu}+saml
Summary:        SAML support for Flask-Multipass
Requires:       python3-saml >= 1.10.1

%description -n python3-%{srcnamenu}+saml
Optional SAML authentication backend for Flask-Multipass.

# sqlalchemy extra
%package -n python3-%{srcnamenu}+sqlalchemy
Summary:        SQLAlchemy support for Flask-Multipass
Requires:       python3-sqlalchemy
Requires:       python3-flask-wtf

%description -n python3-%{srcnamenu}+sqlalchemy
Optional SQLAlchemy integration for Flask-Multipass.


%prep
%autosetup -n %{srcname}-%{version}
sed -i 's/hatchling==/hatchling>=/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{modname}

%files -n python3-%{srcnamenu} -f %{pyproject_files}
%doc README.rst
%license LICENSE

# -------------------------
# Files for extras
# -------------------------

%files -n python3-%{srcnamenu}+authlib
# No files — this subpackage only adds Requires:

%files -n python3-%{srcnamenu}+ldap
# No files — this subpackage only adds Requires:

%files -n python3-%{srcnamenu}+saml
# No files — this subpackage only adds Requires:

%files -n python3-%{srcnamenu}+sqlalchemy
# No files — this subpackage only adds Requires:

%check
%pyproject_check_import

%changelog
* Thu Apr 23 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.11.2-1
- Initial version for Fedora
