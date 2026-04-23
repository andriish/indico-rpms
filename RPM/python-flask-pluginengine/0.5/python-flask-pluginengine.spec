%global srcname Flask-PluginEngine
%global srcnamenu flask-pluginengine
%global modname flask_pluginengine

Name:           python-%{srcnamenu}
Version:        0.5
Release:        1%{?dist}
Summary:        A simple plugin system for Flask applications.

License:        BSD-3-Clause
URL:            https://flask-pluginengine.readthedocs.io/
Source:         %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Flask-PluginEngine is an extension that provides interfaces to create plugins
and handle them within a Flask application.}

%description %_description

%package -n python3-%{srcnamenu}
Summary:        %{summary}

%description -n python3-%{srcnamenu} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%files -n python3-%{srcnamenu} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%check
%pyproject_check_import

%changelog
* Mon Apr 20 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.5-1
- Initial version of 0.5 for Fedora
