%global srcname Flask-Limiter
%global srcnamenu flask_limiter

Name:           python-%{srcname}
Version:        3.12
Release:        1%{?dist}
Summary:        Provides rate limiting features to Flask applications.

License:        MIT
URL:            https://flask-limiter.readthedocs.io/en/stable/
Source:         https://files.pythonhosted.org/packages/70/75/92b237dd4f6e19196bc73007fff288ab1d4c64242603f3c401ff8fc58a42/flask_limiter-3.12.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel 

%global _description %{expand:
Flask-Limiter provides rate limiting features to Flask applications.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcnamenu}-%{version}

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
