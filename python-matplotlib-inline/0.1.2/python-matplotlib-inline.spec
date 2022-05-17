Name:           python-matplotlib-inline
Version:        0.1.2
Release:        3%{?dist}
Summary:        Inline Matplotlib backend for Jupyter

License:        BSD
URL:            https://github.com/ipython/matplotlib-inline
Source0:        %{pypi_source matplotlib-inline}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Inline Matplotlib backend for Jupyter

%package -n     python3-matplotlib-inline
Summary:        %{summary}

%description -n python3-matplotlib-inline
Inline Matplotlib backend for Jupyter


%prep
%autosetup -n matplotlib-inline-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files matplotlib_inline

%files -n python3-matplotlib-inline -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-2
- Rebuilt for Python 3.10

* Tue May 04 2021 Lumír Balhar <lbalhar@redhat.com> - 0.1.2-1
- Initial package.
