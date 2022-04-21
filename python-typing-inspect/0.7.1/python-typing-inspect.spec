%global pypi_name typing-inspect
%global pypi_srcname typing_inspect

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        1%{?dist}
Summary:        Runtime inspection utilities for typing module

License:        MIT
URL:            https://github.com/ilevkivskyi/%{pypi_srcname}
Source0:        %{pypi_source %pypi_srcname}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(mypy-extensions) >= 0.3.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions) >= 3.7.4

#Patch000: typing-3_9.patch

%description
Typing Inspect The "%{pypi_srcname}" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(mypy-extensions) >= 0.3.0
Requires:       python3dist(typing-extensions) >= 3.7.4
%description -n python3-%{pypi_name}
The "%{pypi_srcname}" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.


%prep
%autosetup -n %{pypi_srcname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/%{pypi_srcname}.*.pyc
%{python3_sitelib}/%{pypi_srcname}.py
%{python3_sitelib}/%{pypi_srcname}-%{version}-py*.egg-info

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Anna Khaitovich <akhaitov@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Anna Khaitovich <akhaitov@redhat.com> - 0.5.0-1
- Initial package.
