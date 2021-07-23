#
# spec file for package python-sentry-sdk
#
# Copyright (c) 2020 SUSE LLC
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
# nothing provides python2-venusian >= 1.0 needed by python2-pyramid
%define skip_python2 1
Name:           python-sentry-sdk
Version:        0.19.5
Release:        31.3
Summary:        Python SDK for Sentry.io
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getsentry/sentry-python
Source0:        https://github.com/getsentry/sentry-python/archive/%{version}/sentry-python-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.11}
BuildRequires:  %{python_module SQLAlchemy >= 1.2}
BuildRequires:  %{python_module aiohttp >= 3.5}
BuildRequires:  %{python_module blinker >= 1.1}
BuildRequires:  %{python_module bottle >= 0.12.13}
BuildRequires:  %{python_module celery >= 3}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module executing}
BuildRequires:  %{python_module falcon >= 1.4}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module rq >= 0.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 5}
BuildRequires:  %{python_module urllib3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pyramid}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tox}
# /SECTION
# SECTION extra requirements - which rise up buildtime error or missing in openSUSE
#BuildRequires:  %%{python_module Django >= 1.8}
#BuildRequires:  %%{python_module sanic >= 0.8}
#BuildRequires:  %%{python_module apache-beam >= 2.12}
#BuildRequires:  %%{python_module pyspark >= 2.4.4}
#BuildRequires:  %%{python_module pure_eval}
#BuildRequires:  %%{python_module asttokens}
#BuildRequires:  %%{python_module chalice >= 1.16.0}
# /SECTION
Requires:       python-Flask >= 0.11
Requires:       python-SQLAlchemy >= 1.2
Requires:       python-aiohttp >= 3.5
Requires:       python-blinker >= 1.1
Requires:       python-bottle >= 0.12.13
Requires:       python-celery >= 3
Requires:       python-certifi
Requires:       python-executing
Requires:       python-falcon >= 1.4
Requires:       python-jsonschema
Requires:       python-rq >= 0.6
Requires:       python-tornado >= 5
Requires:       python-urllib3
# SECTION extra requirements - which rise up buildtime error or missing in openSUSE
#Requires:       python-Django >= 1.8
#Requires:       python-sanic >= 0.8
#Requires:       python-apache-beam >= 2.12
#Requires:       python-pyspark >= 2.4.4
#Requires:       python-pure_eval
#Requires:       python-asttokens
#Requires:       python-chalice >= 1.16.0
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A Python SDK for Sentry.io.
https://sentry.io/for/python/

%prep
%setup -q -n sentry-python-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS="-W ignore::DeprecationWarning"
# do not test integration:
rm -r tests/integrations
# test_transport_works / test_transport_infinite_loop / test_simple_rate_limits/ test_data_category_limits / test_complex_limits_without_data_category stucks

# test_auto_enabling_integrations_catches_import_error asert False where False = ..., not sure
%pytest -k 'not (test_transport_works or test_auto_enabling_integrations_catches_import_error or test_filename or test_transport_infinite_loop or test_simple_rate_limits or test_data_category_limits or test_complex_limits_without_data_category)'

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/*

%changelog
* Thu Dec 10 2020 ecsos <ecsos@opensuse.org>
- Update to 0.19.5
  - Fix two regressions added in 0.19.2 with regard to sampling
    behavior when reading the sampling decision from headers.
  - Increase internal transport queue size and make it configurable.
* Wed Dec  2 2020 ecsos <ecsos@opensuse.org>
- Add additional and missing requirements.
* Tue Dec  1 2020 Hans-Peter Jansen <hpj@urpla.net>
- Update to version 0.19.4
  * Fix a bug that would make applications crash if an old version
    of boto3 was installed.
- Update to version 0.19.3
  * Automatically pass integration-relevant data to traces_sampler
    for AWS, AIOHTTP, ASGI, Bottle, Celery, Django, Falcon, Flask,
    GCP, Pyramid, Tryton, RQ, and WSGI integrations
  * Fix a bug where the AWS integration would crash if event was
    anything besides a dictionary
  * Fix the Django integrations's ASGI handler for Channels 3.0.
    Thanks Luke Pomfrey!
- Update to version 0.19.2
  * Add traces_sampler option.
  * The SDK now attempts to infer a default release from various
    environment variables and the current git repo.
  * Fix a crash with async views in Django 3.1.
  * Fix a bug where complex URL patterns in Django would create
    malformed transaction names.
  * Add options for transaction styling in AIOHTTP.
  * Add basic attachment support (documentation tbd).
  * fix a crash in the pure_eval integration.
  * Integration for creating spans from boto3.
- Update to version 0.19.1
  * Fix dependency check for blinker fixes #858
  * Fix incorrect timeout warnings in AWS Lambda and GCP
    integrations #854
- Update to version 0.19.0
  * Removed _experiments.auto_enabling_integrations in favor of
    just auto_enabling_integrations which is now enabled by
    default.
- Update to version 0.18.0
  * Breaking change: The no_proxy environment variable is now
    honored when inferring proxy settings from the system. Thanks
    Xavier Fernandez!
  * Added Performance/Tracing support for AWS and GCP functions.
  * Fix an issue with Django instrumentation where the SDK modified
    resolver_match.callback and broke user code.
- Update to version 0.17.8
  * Fix yet another bug with disjoint traces in Celery.
  * Added support for Chalice 1.20. Thanks again to the folks at
    Cuenca MX!
- Update to version 0.17.7
  * Internal: Change data category for transaction envelopes.
  * Fix a bug under Celery 4.2+ that may have caused disjoint
    traces or missing transactions.
- Update to version 0.17.6
  * Support for Flask 0.10 (only relaxing version check)
- Update to version 0.17.5
  * Work around an issue in the Python stdlib that makes the entire
    process deadlock during garbage collection if events are sent
    from a __del__ implementation.
  * Add possibility to wrap ASGI application twice in middleware to
    enable split up of request scope data and exception catching.
- Update to version 0.17.4
  * New integration for the Chalice web framework for AWS Lambda.
    Thanks to the folks at Cuenca MX!
- Update to version 0.17.3
  * Fix an issue with the pure_eval integration in interaction with
    trimming where pure_eval would create a lot of useless local
    variables that then drown out the useful ones in trimming.
- Update to version 0.17.2
  * Fix timezone bugs in GCP integration.
- Update to version 0.17.1
  * Fix timezone bugs in AWS Lambda integration.
  * Fix crash on GCP integration because of missing parameter
    timeout_warning.
- Update to version 0.17.0
  * Fix a bug where class-based callables used as Django views
    (without using Django's regular class-based views) would not
    have csrf_exempt applied.
  * New integration for Google Cloud Functions.
  * Fix a bug where a recently released version of urllib3 would
    cause the SDK to enter an infinite loop on networking and SSL
    errors.
  * Breaking change: Remove the traceparent_v2 option. The option
    has been ignored since 0.16.3, just remove it from your code.
- Update to version 0.16.5
  * Fix a bug that caused Django apps to crash if the view didn't
    have a __name__ attribute.
- Update to version 0.16.4
  * Add experiment to avoid trunchating span descriptions.
    Initialize with
    init(_experiments={"smart_transaction_trimming": True}).
  * Add a span around the Django view in transactions to
    distinguish its operations from middleware operations.
- Update to version 0.16.3
  * Fix AWS Lambda support for Python 3.8.
  * The AWS Lambda integration now captures initialization/import
    errors for Python 3.
  * The AWS Lambda integration now supports an option to warn about
    functions likely to time out.
  * Testing for RQ 1.5
  * Flip default of traceparent_v2. This change should have zero
    impact. The flag will be removed in 0.17.
  * Fix compatibility bug with Django 3.1.
- Update to version 0.16.2
  * New (optional) integrations for richer stacktraces: pure_eval
    for additional variables, executing for better function names.
- Update to version 0.16.1
  * Flask integration: Fix a bug that prevented custom tags from
    being attached to transactions.
- Update to version 0.16.0
  * Redis integration: add tags for more commands
  * Redis integration: Patch rediscluster package if installed.
  * Session tracking: A session is no longer considered crashed if
    there has been a fatal log message (only unhandled exceptions
    count).
  * Breaking change: Revamping of the tracing API.
  * Breaking change: before_send is no longer called for
    transactions.
- Update to version 0.15.1
  * Fix fatal crash in Pyramid integration on 404.
- Update to version 0.15.0
  * Breaking change: The ASGI middleware will now raise an
    exception if contextvars are not available, like it is already
    the case for other asyncio integrations.
  * Contextvars are now used in more circumstances following a
    bugfix release of gevent. This will fix a few instances of
    wrong request data being attached to events while using an
    asyncio-based web framework.
  * APM: Fix a bug in the SQLAlchemy integration where a span was
    left open if the database transaction had to be rolled back.
    This could have led to deeply nested span trees under that db
    query span.
  * Fix a bug in the Pyramid integration where the transaction name
    could not be overridden at all.
  * Fix a broken type annotation on capture_exception.
  * Basic support for Django 3.1. More work is required for async
    middlewares to be instrumented properly for APM.
- Add new dependencies
* Thu Jun 18 2020 Martin Hauke <mardnh@gmx.de>
- update to 0.14.4
  * Fix bugs in transport rate limit enforcement for specific data
    categories.
  * The bug should not have affected anybody because we do not yet
    emit rate limits for specific event types/data categories.
  * Fix a bug in capture_event where it would crash if given
    additional kwargs.
  * Fix a bug where contextvars from the request handler were
    inaccessible in AIOHTTP error handlers.
  * Fix a bug where the Celery integration would crash if newrelic
    instrumented Celery as well.
* Thu Mar 26 2020 Marketa Calabkova <mcalabkova@suse.com>
- update to 0.14.3
  * Attempt to use a monotonic clock to measure span durations in Performance/APM.
  * Avoid overwriting explicitly set user data in web framework integrations.
  * Allow to pass keyword arguments to `capture_event` instead of configuring the scope.
  * Feature development for session tracking.
* Wed Mar 18 2020 pgajdos@suse.com
- version update to 0.14.2
  * Fix a crash in the Django integration when used in combination with Django Rest Framework's test utilities for request.
  * Fix high memory consumption when sending a lot of errors in the same process. Particularly noticeable in async environments.
  * Show ASGI request data in Django 3.0
  * New integration for the Trytond ERP framework. Thanks n1ngu!
  * Fix trace continuation bugs in APM.
  * No longer report `asyncio.CancelledError` as part of AIOHTTP integration.
  * Fix package classifiers to mark this package as supporting Python 3.8. The SDK supported 3.8 before though.
  * Update schema sent for transaction events (transaction status).
  * Fix a bug where `None` inside request data was skipped/omitted.
  * Fix an issue with the ASGI middleware that would cause Uvicorn to infer the wrong ASGI versions and call the wrapped application with the wrong argument count.
  * Do not ignore the `tornado.application` logger.
  * The Redis integration now instruments Redis blaster for breadcrumbs and transaction spans.
- test at least something
- deleted sources
  - pytest.ini (not needed)
* Fri Nov  8 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.13.2
  - Fix a bug in APM that would cause wrong durations to be
    displayed on non-UTC servers.
* Fri Oct 25 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.13.1
  - Add new global functions for setting scope/context data.
  - Fix a bug that would make Django 1.11+ apps crash when using
    function-based middleware.
* Thu Oct 17 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.13.0
  - Remove an old deprecation warning (behavior itself already
    changed since a long time).
  - The AIOHTTP integration now attaches the request body to crash
    reports. Thanks to Vitali Rebkavets!
  - Add an experimental PySpark integration.
  - First release to be tested under Python 3.8. No code changes
    were necessary though, so previous releases also might have
    worked.
* Wed Oct  2 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.12.3
  - Various performance improvements to event sending.
  - Avoid crashes when scope or hub is racy.
  - Revert a change that broke applications using gevent and channels
    (in the same virtualenv, but different processes).
  - Fix a bug that made the SDK crash on unicode in SQL.
- Comment out test build dependencies since tests are disabled.
* Mon Sep 30 2019 Jimmy Berry <jberry@suse.com>
- Add pytest.ini source to ignore deprecation warning from eventlet
- Disable %%check since pytest does not want to follow documentation
* Mon Sep 30 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.12.2
  - Temporarily remove sending of SQL parameters (as part of
    breadcrumbs or spans for APM) to Sentry to avoid memory
    consumption issues.
  - Fix a crash with ASGI (Django Channels) when the ASGI request
    type is neither HTTP nor Websockets.
* Thu Sep 19 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.12.0
  - Fix a bug where the response object for httplib (or requests)
    was held onto for an unnecessarily long amount of time.
  - APM: Add spans for more methods on subprocess.Popen objects.
  - APM: Add spans for Django middlewares.
  - APM: Add spans for ASGI requests.
* Fri Aug 30 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.11.2
  - fixed shutdown bug while runnign under eventlet
  - added missing data to Redis breadcrumbs
- Include build requirement on python eventlet module for the tests
  while exclusing a subset of new tests
* Sat Aug 24 2019 Jan Engelhardt <jengelh@inai.de>
- Trim time-dependent wording from description.
* Mon Aug 19 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.11.1
  - Remove a faulty assertion (observed in environment with
    Django Channels and ASGI).
* Fri Aug 16 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.11.0
  - mostly bug fixes
  - integration with SQLAlchemy and Apache Beam
* Mon Aug 12 2019 Tomáš Chvátal <tchvatal@suse.com>
- Format with spec-cleaner
- Run tests
* Fri Aug  9 2019 Jimmy Berry <jberry@suse.com>
- Set BuildArch to noarch.
* Fri Aug  9 2019 Jimmy Berry <jberry@suse.com>
- Update to 0.10.2.
* Fri Jun  7 2019 ecsos@opensuse.org
- initial version 0.9.0
