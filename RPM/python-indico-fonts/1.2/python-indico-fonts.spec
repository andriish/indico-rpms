%global srcname indico-fonts
%global srcnamenu indico_fonts

Name:           python-%{srcname}
Version:        1.2
Release:        1%{?dist}
Summary:        This package contains several fonts used by Indico for PDF generation.

License:        Other
URL:            https://github.com/indico/indico-fonts
Source:         %{pypi_source}
BuildArch:      noarch
BuildRequires: python3-pip python3-wheel

%global _description %{expand:
This package contains several fonts used by Indico for PDF generation..}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}

%{python3_sitelib}/%{srcnamenu}-*.egg-info/
%{python3_sitelib}/%{srcnamenu}/


%changelog
* Thu Sep 29 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de>
- Cleanup 
