%global srcname flask-url-map-serializer
%global srcnamenu flask_url_map_serializer

Name:           python-%{srcname}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Dumps the URL map of a flask app to a JSON file

License:        MIT
URL:            https://github.com/indico/babel-plugin-flask-urls
Source:         https://github.com/indico/js-flask-urls/archive/refs/tags/babel-plugin-flask-urls@0.1.0.tar.gz
#{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel
BuildRequires: python3-werkzeug gcc make

%global _description %{expand:
This package adds a urls_to_json command to the flask CLI that dumps the
 URL map of the flask app to a JSON file.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n js-flask-urls-babel-plugin-flask-urls-%{version}/flask-cli

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}


%{python3_sitelib}/*

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
