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

%global _description %{expand:
Flask-Limiter provides rate limiting features to Flask applications.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcnamenu}-%{version}
#rich>=12,<14
sed -i 's/ich>=12,<14/ich>=12/' requirements/main.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{srcnamenu}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
* Thu Apr 23 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 3.12-1
- First Fedora package release for python-Flask-Limiter 3.12
