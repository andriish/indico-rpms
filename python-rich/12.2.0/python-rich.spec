%global pypi_name rich

Name:           python-%{pypi_name}
Version:        12.2.0
Release:        %autorelease
Summary:        Render rich text and beautiful formatting in the terminal

License:        MIT
URL:            https://github.com/Textualize/rich
Source0:        %{url}/archive/v%{version}/rich-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# for checks
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(toml)

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
# This was previously misnamed, remove the obsolete in Fedora 38, EPEL 10
Obsoletes:      python-%{pypi_name} < 10.16.1-2

%description -n python3-%{pypi_name}
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rich

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
