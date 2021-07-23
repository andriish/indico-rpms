%define srcname dnspython

Name:          python-dnspython
Summary:       DNS toolkit for Python
Version:       1.16.0
Release:       %mkrel 4
License:       MIT
Group:         Development/Python
URL:           http://www.dnspython.org/
Source0:       http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
Source1:       http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz.asc
BuildArch:     noarch

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic updates.
It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high level
classes perform queries for data of a given name, type, and class, and
return an answer set. The low level classes allow direct manipulation
of DNS zones, messages, names, and records.

%package -n python3-dnspython
Summary:       DNS toolkit for Python 3
BuildRequires: pkgconfig(python3)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(pycryptodome)
%{?python_provide:%python_provide python3-dnspython}
Provides:      dnspython = %{version}-%{release}
Requires:      python3dist(idna)
Requires:      python3dist(pycryptodome)
Requires:      python3dist(ecdsa)

%description -n python3-dnspython
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic updates.
It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high level
classes perform queries for data of a given name, type, and class, and
return an answer set. The low level classes allow direct manipulation
of DNS zones, messages, names, and records.

%prep
%setup -q -n dnspython-%version

# drop bundled egg-info
rm -rf %{srcname}.egg-info

# strip executable permissions so that we don't pick up dependencies
# from documentation
find examples -type f | xargs chmod a-x

# fix tests
sed -i -e 's,tests.ttxt_module,ttxt_module,g' tests/test_rdata.py

%build
%py3_build

%install
%py3_install

%check
# skip one test because it queries the network
for py in tests/*.py
do
  if [ $py != tests/test_resolver.py ]
  then
    PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} $py
  fi
done

%files -n python3-dnspython
%license LICENSE
%doc README* examples
%{python3_sitelib}/*egg-info
%{python3_sitelib}/dns


%changelog
* Sun Feb 16 2020 umeabot <umeabot> 1.16.0-4.mga8
+ Revision: 1531353
- Mageia 8 Mass Rebuild

* Wed Sep 11 2019 tv <tv> 1.16.0-3.mga8
+ Revision: 1439568
- rebuild for python-3.8

* Thu Sep 05 2019 wally <wally> 1.16.0-2.mga8
+ Revision: 1437683
- rebuild for python3.8
- update requires
- drop python2 support

* Sat Jan 12 2019 wally <wally> 1.16.0-1.mga7
+ Revision: 1355679
- new version 1.16.0
- last version with python2 support
- provide dnspython with python3 pkg

* Mon Jan 07 2019 kekepower <kekepower> 1.15.0-3.mga7
+ Revision: 1350274
- Rebuild for Python 3.7

* Thu Sep 20 2018 umeabot <umeabot> 1.15.0-2.mga7
+ Revision: 1288777
- Mageia 7 Mass Rebuild

* Mon Mar 26 2018 kekepower <kekepower> 1.15.0-1.mga7
+ Revision: 1212579
- BR python-setuptools
- Update to version 1.15.0
- Renamed python-dnspython to python2-dnspython
- Added python3-dnspython
- Using python_provide

* Fri Feb 19 2016 umeabot <umeabot> 1.11.1-10.mga6
+ Revision: 970497
- Mageia 6 Mass Rebuild

* Wed Oct 07 2015 ovitters <ovitters> 1.11.1-9.mga6
+ Revision: 887053
- rebuild for new python3 (again)

* Wed Oct 07 2015 ovitters <ovitters> 1.11.1-8.mga6
+ Revision: 887018
- rebuild for new python3
+ tv <tv>
- use new python2 macros
- split python3 in its own SRPM

* Wed Oct 15 2014 umeabot <umeabot> 1.11.1-7.mga5
+ Revision: 749737
- Second Mageia 5 Mass Rebuild

* Sat Sep 27 2014 tv <tv> 1.11.1-6.mga5
+ Revision: 728371
- rebuild for missing pythoneggs deps

* Tue Sep 16 2014 umeabot <umeabot> 1.11.1-5.mga5
+ Revision: 688003
- Mageia 5 Mass Rebuild

* Sat May 31 2014 pterjan <pterjan> 1.11.1-4.mga5
+ Revision: 628614
- Rebuild for new Python

* Tue Oct 22 2013 umeabot <umeabot> 1.11.1-3.mga4
+ Revision: 543321
- Mageia 4 Mass Rebuild

* Tue Oct 15 2013 pterjan <pterjan> 1.11.1-2.mga4
+ Revision: 498431
- Rebuild to add different pythonegg provides for python 2 and 3

* Sat Oct 05 2013 philippem <philippem> 1.11.1-1.mga4
+ Revision: 491663
- Update to 1.11.1

* Sun Sep 01 2013 philippem <philippem> 1.11.0-1.mga4
+ Revision: 474138
- update to 1.11.0, add Python 3

* Sun Jan 13 2013 umeabot <umeabot> 1.9.4-2.mga3
+ Revision: 378755
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Wed Jun 22 2011 dmorgan <dmorgan> 1.9.4-1.mga2
+ Revision: 111984
- imported package python-dnspython


* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.4-1mdv2011.0
+ Revision: 662530
- update to new version 1.9.4

* Thu Nov 25 2010 Funda Wang <fwang@mandriva.org> 1.9.2-1mdv2011.0
+ Revision: 600934
- update to new version 1.9.2

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.8.0-2mdv2011.0
+ Revision: 598984
- rebuild for py2.7

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.0-1mdv2011.0
+ Revision: 569667
- update to new version 1.8.0

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.1-1mdv2010.0
+ Revision: 397063
- update to new version 1.7.1

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.0-1mdv2010.0
+ Revision: 384248
- update to new version 1.6.0

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.5.0-6mdv2009.1
+ Revision: 323622
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-5mdv2009.0
+ Revision: 259578
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-4mdv2009.0
+ Revision: 247405
- rebuild
- fix no-buildroot-tag

* Mon Nov 05 2007 Nicolas Vigier <nvigier@mandriva.com> 1.5.0-2mdv2008.1
+ Revision: 106164
- add provides on dnspython
- import python-dnspython


