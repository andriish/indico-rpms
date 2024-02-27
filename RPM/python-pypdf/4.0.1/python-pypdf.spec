%global srcname pypdf
%global srcnamenu pypdf

Name:           python-%{srcname}
Version:        4.0.1
Release:        1%{?dist}
Summary:        A Pure-Python library built as a PDF toolkit

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel


%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-flit-core

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n pypdf-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
