%global pypi_name Flask-PluginEngine
%global modname flask_pluginengine

Name:           python-%{pypi_name}
Version:        0.5
Release:        1%{?dist}
Summary:        A simple plugin system for Flask applications.

License:        BSD-3-Clause
URL:            https://flask-pluginengine.readthedocs.io/
Source:        https://github.com/indico/flask-pluginengine/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

%description
Flask-PluginEngine is an extension that provides interfaces to create plugins
and handle them within a Flask application.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Flask-PluginEngine is an extension that provides interfaces to create plugins
and handle them within a Flask application.

%prep
%autosetup -n flask-pluginengine-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%check
%pyproject_check_import

%changelog
* Mon Apr 20 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> 0.5-1
- First version of 0.5 for Fedora
