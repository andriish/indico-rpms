%global srcname hiredis
%global srcnamenu hiredis

Name:           python-%{srcname}
Version:        2.0.0
Release:        2%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
Source:         %{pypi_source}
#BuildArch:      noarch
BuildRequires: python3-pip python3-wheel
BuildRequires: python3-werkzeug 
BuildRequires: gcc 
BuildRequires: make
%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
#{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitearch}/%{srcnamenu}-*.egg-info/
%{python3_sitearch}/%{srcnamenu}/

