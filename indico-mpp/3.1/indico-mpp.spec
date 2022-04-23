#URL:            https://github.com/ua-parser/uap-python
#Source:         https://files.pythonhosted.org/packages/source/u/{_pkgname}/{_pkgname}-{version}.tar.gz

%global srcname indico
%global srcnamenu indico

Name:           mpp-indico
Version:        3.1
Release:        2%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser

Source:         indico.cil
BuildArch:      noarch
BuildRequires:  npm
BuildRequires:  redis
BuildRequires:  python3-pip python3-wheel
#Requires: python3-indico

%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

%description %_description

%package -n %{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n %{srcname} %_description

%prep

%build

%install


%files -n %{srcname}
#license COPYING
#doc README.rst
%{python3_sitelib}/%{srcnamenu}-*.egg-info/
%{python3_sitelib}/%{srcnamenu}/
%{_bindir}/indico
