Name:           python-sentry-sdk
Version:        1.5.7
Release:        1%{?dist}
Summary:        The new Python SDK for Sentry.io

License:        BSD
URL:            https://sentry.io/for/python/
Source0:        https://github.com/getsentry/sentry-python/archive/%{version}/sentry-python-%{version}.tar.gz
# Skip tests which cannot be run during Fedora build
#Patch1:         0001-python-sentry-1.5.7-sdk-skip-forbidden-tests.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Use Fedora versions of testing dependencies + pytest instead of pinned versions in upstream + tox
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(werkzeug)
BuildRequires:  python3dist(pytest-localserver)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pyrsistent)
BuildRequires:  python3dist(gevent)
BuildRequires:  python3dist(executing)
BuildRequires:  python3dist(asttokens)


%global _description %{expand:
Python Error and Performance Monitoring. Actionable insights to resolve Python
performance bottlenecks and errors. See the full picture of any Python exception
so you can diagnose, fix, and optimize performance in the Python debugging
process.}

%description %_description

%package -n python3-sentry-sdk
Summary:        %{summary}

%description -n python3-sentry-sdk %_description

# Dependencies for sanic, beam, pyspark, and chalice extras are not yet in Fedora
%pyproject_extras_subpkg -n flask bottle falcon django celery rq aiohttp tornado sqlalchemy pure_eval httpx


%prep
%autosetup -p1 -n sentry-python-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sentry_sdk


%check
#pytest


%files -n python3-sentry-sdk -f %{pyproject_files}
%doc README.md


%changelog
* Tue Mar 15 2022 Roman Inflianskas <rominf@aiven.io> - 1.5.7-1
- Initial package
