%global srcname flask-url-map-serializer
%global srcnamenu flask_url_map_serializer

Name:           python-%{srcname}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Dumps the URL map of a flask app to a JSON file

License:        MIT
URL:            https://github.com/indico/babel-plugin-flask-urls
Source:         https://github.com/indico/js-flask-urls/archive/refs/tags/babel-plugin-flask-urls@0.1.0.tar.gz
BuildArch:      noarch

%global _description %{expand:
This package adds a urls_to_json command to the flask CLI that dumps the
 URL map of the flask app to a JSON file.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n js-flask-urls-babel-plugin-flask-urls-%{version}/flask-cli
cp ../LICENSE ./

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{srcnamenu}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE

%check
%pyproject_check_import

%changelog
* Wed Apr 22 2026 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de> - 0.1.0-1
- First version of 0.1.0 for Fedora
