#
# spec file for package python-charset-normalizer
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-charset-normalizer
Version:        1.3.9
Release:        1.1
Summary:        Python Universal Charset detector
License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source:         https://files.pythonhosted.org/packages/source/c/charset_normalizer/charset_normalizer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable
Requires:       python-cached-property >= 1.5
Requires:       python-dragonmapper >= 0.2
Requires:       python-loguru >= 0.5
Requires:       python-zhon
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       python-requests
Suggests:       python-requests-html
Suggests:       python-unicodedata2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PrettyTable}
BuildRequires:  %{python_module cached-property >= 1.5}
BuildRequires:  %{python_module dragonmapper >= 0.2}
BuildRequires:  %{python_module loguru >= 0.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zhon}
# /SECTION
%python_subpackages

%description
Python Universal Charset detector.

%prep
%setup -q -n charset_normalizer-%{version}
dos2unix README.md
chmod a-x charset_normalizer/assets/frequencies.json

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/normalizer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative normalizer

%postun
%python_uninstall_alternative normalizer

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/normalizer
%{python_sitelib}/*

%changelog
* Thu May 20 2021 pgajdos@suse.com
- version update to 1.3.9
  * Bugfix: bug In some very rare cases, you may end up getting encode/decode errors due to a bad bytes payload #40
  * Bugfix: bug Empty given payload for detection may cause an exception if trying to access the alphabets property. #39
  * Bugfix: bug The legacy detect function should return UTF-8-SIG if sig is present in the payload. #38
* Tue Feb  9 2021 John Vandenberg <jayvdb@gmail.com>
- Switch to PyPI source
- Add Suggests: python-unicodedata2
- Remove executable bit from charset_normalizer/assets/frequencies.json
- Update to v1.3.6
  * Allow prettytable 2.0
- from v1.3.5
  * Dependencies refactor and add support for py 3.9 and 3.10
  * Fix version parsing
* Mon May 25 2020 Petr Gajdos <pgajdos@suse.com>
- %%python3_only -> %%python_alternative
* Mon Jan 27 2020 Marketa Calabkova <mcalabkova@suse.com>
- Update to 1.3.4
  * Improvement/Bugfix : False positive when searching for successive upper, lower char. (ProbeChaos)
  * Improvement : Noticeable better detection for jp
  * Bugfix : Passing zero-length bytes to from_bytes
  * Improvement : Expose version in package
  * Bugfix : Division by zero
  * Improvement : Prefers unicode (utf-8) when detected
  * Apparently dropped Python2 silently
* Fri Oct  4 2019 Marketa Calabkova <mcalabkova@suse.com>
- Update to 1.3.0
  * Backport unicodedata for v12 impl into python if available
  * Add aliases to CharsetNormalizerMatches class
  * Add feature preemptive behaviour, looking for encoding declaration
  * Add method to determine if specific encoding is multi byte
  * Add has_submatch property on a match
  * Add percent_chaos and percent_coherence
  * Coherence ratio based on mean instead of sum of best results
  * Using loguru for trace/debug <3
  * from_byte method improved
* Thu Sep 26 2019 Tomáš Chvátal <tchvatal@suse.com>
- Update to 1.1.1:
  * from_bytes parameters steps and chunk_size were not adapted to sequence len if provided values were not fitted to content
  * Sequence having lenght bellow 10 chars was not checked
  * Legacy detect method inspired by chardet was not returning
  * Various more test updates
* Fri Sep 13 2019 Tomáš Chvátal <tchvatal@suse.com>
- Update to 0.3:
  * Improvement on detection
  * Performance loss to expect
  * Added --threshold option to CLI
  * Bugfix on UTF 7 support
  * Legacy detect(byte_str) method
  * BOM support (Unicode mostly)
  * Chaos prober improved on small text
  * Language detection has been reviewed to give better result
  * Bugfix on jp detection, every jp text was considered chaotic
* Fri Aug 30 2019 Tomáš Chvátal <tchvatal@suse.com>
- Fix the tarball to really be the one published by upstream
* Wed Aug 28 2019 John Vandenberg <jayvdb@gmail.com>
- Initial spec for v0.1.8
