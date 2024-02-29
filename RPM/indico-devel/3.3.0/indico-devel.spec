%define debug_package %{nil}
%global srcname indico-devel
%global srcnamenu indico-devel

Name:           indico-devel
Version:        3.3.0
Release:        6%{?dist}
Summary:        Dependencies and build environment for Indico

License:        MIT
URL:            https://github.com/andriish/indico-rpms
Source:         indico-devel-%{version}.tar.gz


BuildRequires: python3-devel
BuildRequires: python3-setuptools 
BuildRequires: python-srpm-macros 
BuildRequires: python3-rpm-macros
BuildRequires: pyproject-rpm-macros
Requires: python3-rpm-macros 
Requires: python-srpm-macros 
Requires: python3-devel
Requires: pyproject-rpm-macros






#Those are fake to satisfy the Indico requirements.
Provides: python%{python3_version}dist(redis[hiredis])
Provides: python%{python3_version}dist(celery[redis])
Provides: python%{python3_version}dist(lxml[html5])
Provides: python%{python3_version}dist(marshmallow-dataclass[enum])
Provides: python%{python3_version}dist(wtforms[email])
Provides: python%{python3_version}dist(bleach[css])
Provides: python%{python3_version}dist(pypdf)
Provides: python%{python3_version}dist(tzdata)
Provides: python%{python3_version}dist(importlib-resources)


%global _description %{expand:
Dependencies and build environment for Indico and some scripts to start Indico.}

%description %_description

Summary:        %{summary}

%prep
%setup -q  -c

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755  indico-devel-remove-indico.sh %{buildroot}/%{_bindir}
install -m 755  indico-devel-start-indico.sh %{buildroot}/%{_bindir}

%files -n %{srcname}
%{_bindir}/indico-devel-remove-indico.sh
%{_bindir}/indico-devel-start-indico.sh


%changelog
* Thu Feb 22 2024 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2.9
- Version 3.2.9 
* Wed Sep 28 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2
- Version 3.2. 


