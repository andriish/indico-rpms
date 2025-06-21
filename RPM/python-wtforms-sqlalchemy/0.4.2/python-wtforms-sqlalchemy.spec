%global pkg_name wtforms-sqlalchemy
%global module_name wtforms_sqlalchemy

Name:           python-%{pkg_name}
Version:        0.4.2
Release:        1%{?dist}
Summary:        WTForms integration for SQLAlchemy

License:        BSD-3-Clause
URL:            https://github.com/wtforms/%{pkg_name}
Source0:        %{url}/archive/%{version}/%{pkg_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel python3-hatchling python-flit-core python3-pip pyproject-rpm-macros

%global _description %{expand:
WTForms-SQLAlchemy is a fork of the wtforms.ext.sqlalchemy package
from WTForms. The package has been renamed to wtforms_sqlalchemy but
otherwise should function the same as wtforms.ext.sqlalchemy did.}

%description %_description

%package -n python3-%{pkg_name}
Summary:        %{summary}

%description -n python3-%{pkg_name} %_description


%prep
%autosetup -p1 -n %{pkg_name}-%{version}


#generate_buildrequires
#pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module_name}




%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst
%doc CHANGES.rst
%license LICENSE.txt


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Python Maint <python-maint@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 11 2022 Matěj Grabovský <mgrabovs@redhat.com> - 0.3.0-1
- Initial package
