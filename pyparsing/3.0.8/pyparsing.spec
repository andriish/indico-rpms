%global srcname pyparsing
%global _summary Python package with an object-oriented approach to text processing

# when bootstrapping Python 3, pyparsing needs to be rebuilt before depndency generator is available
%bcond_with bootstrap
%if %{without bootstrap}
%global build_wheel 1
%global python_wheelname %{srcname}-%{version}-py2.py3-none-any.whl
%endif


Summary:        %{_summary}
Name:           pyparsing
Version:        3.0.8
Release:        1%{?dist}

License:        MIT
URL:            https://github.com/pyparsing/pyparsing
Source0:        https://github.com/%{name}/%{name}/archive/%{name}_%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  dos2unix
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{without bootstrap}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%if 0%{?build_wheel}
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
%endif

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


%if %{without bootstrap}
%package        doc
Summary:        Documentation for pyparsing python package

# Most examples are under the project's license, MIT
# pymicko.py is under GPLv3+
# snmp_api.h is under CMU-UC (MIT)
# sparser.py is under GPLv2+
# searchparser.py is under BSD (3-clause, with advertising)
# btpyparse.py is under "Simplified BSD license"
License:        MIT and GPLv2+ and GPLv3+ and BSD

%description    doc
The package contains documentation for pyparsing.
%endif


%package -n python%{python3_pkgversion}-pyparsing
Summary:        %{_summary}
%if %{with bootstrap}
Provides:       python%{python3_pkgversion}dist(pyparsing) = %{version}
Provides:       python%{python3_version}dist(pyparsing) = %{version}
Requires:       python(abi) = %{python3_version}
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-pyparsing
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.

This is the Python 3 version.


%prep
%setup -q -n %{name}-%{name}_%{version}
dos2unix -k CHANGES LICENSE


%build
%if 0%{?build_wheel}
%py3_build_wheel
%else
%py3_build
%endif

%if %{without bootstrap}
# build docs
pushd docs
# Theme is not available
sed -i '/alabaster/d' conf.py
sphinx-build -b html . html
popd
%endif

%install
%if 0%{?build_wheel}
%py3_install_wheel %{python_wheelname}
%else
%py3_install
%endif


%check
%{__python3} unitTests.py
%{__python3} simple_unit_tests.py


%files -n python%{python3_pkgversion}-pyparsing
%license LICENSE
%doc CHANGES README.rst
%{python3_sitelib}/pyparsing.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pyparsing-*-info/

%if %{without bootstrap}
%files doc
%license LICENSE
%doc CHANGES README.rst docs/html examples
%endif


%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 2.4.7-8
- Rebuilt for Python 3.10

* Tue Jun 01 2021 Python Maint <python-maint@redhat.com> - 2.4.7-7
- Bootstrap for Python 3.10

* Thu May 27 2021 Petr Viktorin <pviktori@redhat.com> - 2.4.7-6
- Fix licence for examples shipped in pyparsing-doc

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.7-3
- Rebuilt for Python 3.9

* Thu May 21 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.7-2
- Bootstrap for Python 3.9

* Mon Apr 06 2020 Dan Horák <dan[at]danny.cz> - 2.4.7-1
- Update to 2.4.7 (#1821085)

* Mon Mar 30 2020 David King <amigadave@amigadave.com> - 2.4.6-3
- Fix the summary for the Python 3 subpackage

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Dan Horák <dan[at]danny.cz> - 2.4.6-1
- Update to 2.4.6 (#1786815)

* Fri Nov 15 2019 Dan Horák <dan[at]danny.cz> - 2.4.5-1
- Update to 2.4.5 (#1768725)
- Drop Python2 subpackage (#1770564)

* Tue Oct  8 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.2-1
- Update to latest version (#1742167)

* Mon Sep 02 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-6
- Reduce Python 2 build time dependencies

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-5
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-4
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 José Matos <jamatos@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Tue Feb 26 2019 Yatin Karel <ykarel@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Dan Horák <dan[at]danny.cz> - 2.3.0-1
- Update to 2.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.7

* Wed Mar 14 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.10-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-5
- Remove the empty pyparsing package, provide and obsolete it from python2-pyparsing

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.1.10-3
- Rebuild as wheel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 José Matos <jamatos@fedoraproject.org> - 2.1.10-1
- update to 2.1.10
- do not own __pycache__

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.1.5-3
- Rebuild for Python 3.6
- Add missing BuildRequires for python-setuptools

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 José Abílio Matos <jamatos@fc.up.pt> - 2.1.5-1
- update to 2.1.5

* Thu May 12 2016 José Matos <jamatos@fedoraproject.org> - 2.1.3-1
- update to 2.1.3

* Sun May  8 2016 José Matos <jamatos@fedoraproject.org> - 2.1.1-1
- update to 2.1.1

* Tue Feb 16 2016 José Matos <jamatos@fedoraproject.org> - 2.1.0-2
- fix typo in provides for the python3 subpackage

* Mon Feb 15 2016 José Matos <jamatos@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- add a python2 subpackage preserving the upgrade path

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.0.7-1
- 2.0.7

* Tue Nov 17 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.0.6-1
- 2.0.6
- Some clean up

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 2.0.3-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 28 2014 José Matos <jamatos@fedoraproject.org> - 2.0.3-1
- update to 2.0.3
- include the whole documentation set

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Oct 27 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.0.1-1
- 2.0.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr  3 2013 Thomas Spura <tomspur@fedoraproject.org> - 1.5.6-8
- add patch to correct typo in exception handling

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 David Malcolm <dmalcolm@redhat.com> - 1.5.6-6
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1.5.6-5
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec  6 2011 David Malcolm <dmalcolm@redhat.com> - 1.5.6-2
- fix __pycache__ conditional on RHEL

* Fri Jul  1 2011 José Matos <jamatos@fedoraproject.org> - 1.5.6-1
- New upstream version.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 21 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.5.5-1
- 1.5.5
- use buildroot macro
- fix wrong file end of line encoding
- convert files to utf-8
- doc subpackage
- python3 subpackage
- rpmlint clean

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 16 2010 Dan Horák <dan[at]danny.cz> - 1.5.0-6
- include egginfo on EL >= 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.5.0-3
- Rebuild for Python 2.6

* Mon Aug  4 2008 José Matos <jamatos[AT]fc.up.pt> - 1.5.0-2
- respun (now with the right sources)

* Mon Aug  4 2008 José Matos <jamatos[AT]fc.up.pt> - 1.5.0-1
- new upstream release.

* Tue Apr  1 2008 José Matos <jamatos[AT]fc.up.pt> - 1.4.11-1
- New upstream version, add egg-info for F9+.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 1.4.7-1
- New upstream version.

* Sat Apr 21 2007 José Matos <jamatos[AT]fc.up.pt> - 1.4.6-1
- New upstream version.

* Mon Dec 11 2006 José Matos <jamatos[AT]fc.up.pt> - 1.4.4-1
- New upstream version.

* Mon Sep 11 2006 José Matos <jamatos[AT]fc.up.pt> - 1.4.3-1
- New version.

* Wed Aug  3 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.3-1
- Initial RPM release
