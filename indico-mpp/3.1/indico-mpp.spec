#URL:            https://github.com/ua-parser/uap-python
#Source:         https://files.pythonhosted.org/packages/source/u/{_pkgname}/{_pkgname}-{version}.tar.gz

%global srcname indico-mpp
%global srcnamenu indico-mpp

Name:           indico-mpp
Version:        3.1
Release:        3%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://pypi.python.org/pypi/ua-parser

Source:         indico-mpp-3.1.tar.gz


BuildArch:      noarch
BuildRequires:  npm
BuildRequires:  redis
BuildRequires:  firewalld
BuildRequires:  python3-pip python3-wheel
#Requires: python3-indico
Requires: postgresql postgresql-server postgresql-contrib
Requires: redis firewalld

%global _description %{expand:
A python module which provides a convenient example. This is the
rest of the description that provides more details.}

%description %_description

#package -n {srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n %{srcname} %_description

%prep
%setup -q  -c

%build

%install


mkdir -p %{buildroot}/etc
install -m 0755 uwsgi-indico.ini %{buildroot}/etc/uwsgi-indico.ini
mkdir -p %{buildroot}/etc/systemd/system/
install -m 0755 indico-uwsgi.service %{buildroot}/etc/systemd/system/indico-uwsgi.service
mkdir -p %{buildroot}/etc/nginx/conf.d/
install -m 0755 indico.conf %{buildroot}/etc/nginx/conf.d/indico.conf
mkdir -p %{buildroot}/etc/systemd/system/
install -m 0755 indico-celery.service %{buildroot}/etc/systemd/system/indico-celery.service
mkdir -p %{buildroot}/etc/httpd/conf.d/
install -m 0755 indico-sslredir.conf %{buildroot}/etc/httpd/conf.d/indico-sslredir.conf
mkdir  -p %{buildroot}/etc/ssl/indico
#chown root:root %{buildroot}/etc/ssl/indico/
#chmod 700 %{buildroot}/etc/ssl/indico
install -m 0700 ffdhe2048 %{buildroot}//etc/ssl/indico/ffdhe2048

install -m 0700 indico.cil %{buildroot}//etc/ssl/indico/indico.cil

#install -m 0755 bello /usr/bin/bello

#
%post
postgresql-setup initdb
postgres -c 'createuser indico'
postgres -c 'createdb -O indico indico'
postgres -c 'psql indico -c "CREATE EXTENSION unaccent; CREATE EXTENSION pg_trgm;"'

useradd -rm -g apache -d /opt/indico -s /bin/bash indico

echo 'LoadModule proxy_uwsgi_module modules/mod_proxy_uwsgi.so' > /etc/httpd/conf.modules.d/proxy_uwsgi.conf

systemctl enable httpd.service postgresql.service redis.service indico-celery.service indico-uwsgi.service

firewall-cmd --permanent --add-port 443/tcp --add-port 80/tcp
firewall-cmd --reload

semodule -i /etc/ssl/indico/indico.cil

%files -n %{srcname}
#license COPYING
#doc README.rst
/etc/uwsgi-indico.ini
/etc/systemd/system/indico-uwsgi.service
/etc/nginx/conf.d/indico.conf
/etc/systemd/system/indico-celery.service
/etc/ssl/indico/ffdhe2048
/etc/httpd/conf.d/indico-sslredir.conf
/etc/ssl/indico/indico.cil
