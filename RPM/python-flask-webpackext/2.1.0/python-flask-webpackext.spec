%global srcname flask_webpackext
%global srcnamenu flask_webpackext

Name:           python-%{srcname}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Webpack integration for Flask

License:        BSD-3-Clause
URL:            https://flask-webpackext.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/f6/b4/43fcb72a19ee53ee04b6c922633152e38eedc433745a537439ed520ec548/flask_webpackext-2.1.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-werkzeug gcc make
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Flask-WebpackExt makes it easy to interface with your existing Webpack 
project from Flask and does not try to manage Webpack for you. }

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{srcnamenu}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%doc CHANGES.rst
%license LICENSE

%check
%pytest

%changelog
* Wed Apr 22 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 2.1.0-1
- First version of 2.1.0 for Fedora
