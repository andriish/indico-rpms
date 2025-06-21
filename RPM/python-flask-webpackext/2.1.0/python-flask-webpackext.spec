%global srcname flask-webpackext
%global srcnamenu flask_webpackext

Name:           python-%{srcname}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Webpack integration for Flask.

License:        BSD
URL:            https://flask-webpackext.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/f6/b4/43fcb72a19ee53ee04b6c922633152e38eedc433745a537439ed520ec548/flask_webpackext-2.1.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel python-pytest-runner
BuildRequires:  python3-werkzeug gcc make

%global _description %{expand:
Flask-WebpackExt makes it easy to interface with your existing Webpack 
project from Flask and does not try to manage Webpack for you. }

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools pyproject-rpm-macros

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcnamenu}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install


# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*.dist-info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
