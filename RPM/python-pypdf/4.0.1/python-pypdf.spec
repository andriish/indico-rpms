%global srcname pypdf
%global srcnamenu pypdf

Name:           python-%{srcname}
Version:        4.0.1
Release:        1%{?dist}
Summary:        A Pure-Python library built as a PDF toolkit

License:        BSD
URL:            https://pypdf.readthedocs.io/en/latest/
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-pip python3-wheel


%global _description %{expand:
pypdf is a free and open source pure-python PDF library capable of 
splitting, merging, cropping, and transforming the pages of PDF files. 
It can also add custom data, viewing options, and passwords to PDF files. 
pypdf can retrieve text and metadata from PDFs as well.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-flit-core

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n pypdf-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*info/
%{python3_sitelib}/%{srcnamenu}/

%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
