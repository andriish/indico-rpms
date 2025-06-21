%global srcname indico-mpp-configuration
%global srcnamenu indico-mpp-configuration

Name:           python-%{srcname}
Version:        3.3
Release:        16%{?dist}
Summary:        MPP Indico configuration
License:        MIT
URL:            https://mpp.mpg.de
Source:         indico-mpp-configuration-%{version}.tar.gz

BuildArch:     noarch


 

BuildRequires: npm
BuildRequires: firewalld
BuildRequires: python3-pip python3-wheel
BuildRequires: openssl-devel openssl-libs openssl
BuildRequires: policycoreutils



BuildRequires: python3-nbconvert 
BuildRequires: python3-rpm-macros 
BuildRequires: python-srpm-macros 
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: pyproject-rpm-macros


%description 
Configuration of Indico for MPP.
 

%package -n python3-indico-mpp-configuration
Summary:  Configuration of Indico for MPP.
Conflicts: python3-indico-default-configuration
Conflicts: python-indico-default-configuration
Requires: python3-indico
Requires: openssl-devel openssl-libs openssl
Requires: httpd mod_proxy_uwsgi mod_ssl mod_xsendfile
Requires: postgresql postgresql-server postgresql-libs postgresql-devel postgresql-contrib
Requires: redis httpd mod_proxy_uwsgi mod_ssl mod_xsendfile

Requires: policycoreutils
Requires: firewalld
Requires: /usr/bin/xelatex
Requires: postfix
Requires: python-certbot-apache

Requires: python3-nbconvert 
Requires: python3-rpm-macros 
Requires: python-srpm-macros 
Requires: python3-devel
Requires: pyproject-rpm-macros

Requires: python3-indico-vc_zoom-plugin
Requires: python3-indico-vc_dummy-plugin
Requires: python3-indico-ursh-plugin
Requires: python3-indico-themes_legacy-plugin
Requires: python3-indico-storage_s3-plugin
Requires: python3-indico-prometheus-plugin
Requires: python3-indico-previewer_jupyter-plugin
Requires: python3-indico-previewer_code-plugin
Requires: python3-indico-piwik-plugin
Requires: python3-indico-payment_sixpay-plugin
Requires: python3-indico-payment_paypal-plugin
Requires: python3-indico-payment_manual-plugin
Requires: python3-indico-owncloud-plugin
Requires: python3-indico-livesync-plugin
Requires: python3-indico-cloud_captchas-plugin
Requires: python3-indico-citadel-plugin



%description -n python3-indico-mpp-configuration 
Configuration of Indico for MPP.

%pre
mkdir -p /opt/indico
adduser  -rm -g apache -m -d /opt/indico -s /bin/bash indico
chown -R indico /opt/indico
systemctl stop postgresql.service


%prep
%setup -q  -c

%build

%install
THISHOSTNAME=indico01.mpp.mpg.de
sed -i 's/YOURHOSTNAME/'"$THISHOSTNAME"'/g' *.*
sed -i 's,PYTHONSITELIB,'%{python3_sitelib}',g'   indico.conf 

mkdir -p %{buildroot}/etc
install -m 0755 uwsgi-indico.ini %{buildroot}/etc/uwsgi-indico.ini
mkdir -p %{buildroot}/etc/systemd/system/
install -m 0755 indico-uwsgi.service %{buildroot}/etc/systemd/system/indico-uwsgi.service
mkdir -p %{buildroot}/etc/httpd/conf.d/
install -m 0755 indico.conf %{buildroot}/etc/httpd/conf.d/indico.conf
mkdir -p %{buildroot}/etc/systemd/system/
install -m 0755 indico-celery.service %{buildroot}/etc/systemd/system/indico-celery.service
mkdir -p %{buildroot}/etc/httpd/conf.d/
install -m 0755 indico-sslredir.conf %{buildroot}/etc/httpd/conf.d/indico-sslredir.conf
mkdir  -p %{buildroot}/etc/ssl/indico
#chown root:root %{buildroot}/etc/ssl/indico/
#chmod 700 %{buildroot}/etc/ssl/indico
install -m 0700 ffdhe2048 %{buildroot}//etc/ssl/indico/ffdhe2048

install -m 0700 indico.cil %{buildroot}//etc/ssl/indico/indico.cil

mkdir -p %{buildroot}/opt/indico/etc/

install -m 755  etcindico.conf %{buildroot}//opt/indico/etc/indico.conf

mkdir -p %{buildroot}/%{python3_sitelib}/indico/web/static/images/
mkdir -p %{buildroot}/%{python3_sitelib}/indico-mpp-configuration/web/static/images/
#install -m 755 scaledglobe.png #{buildroot}/#{python3_sitelib}/indico/web/static/images/globe.png
#install -m 755 logo_indico_bw.svg #{buildroot}/#{python3_sitelib}/indico/web/static/images/logo_indico_bw.svg
install -m 755 robots.txt %{buildroot}/%{python3_sitelib}/indico/web/static/robots.txt



mkdir -p %{buildroot}/%{python3_sitelib}/indico/modules/auth/templates/
install -m 755 register.html   %{buildroot}/%{python3_sitelib}/indico/modules/auth/templates/register.html

mkdir -p %{buildroot}/etc/systemd/system/postgresql.service.d/
install -m 755  indicopostgresql.conf %{buildroot}/etc/systemd/system/postgresql.service.d/indicopostgresql.conf

%post -n python3-indico-mpp-configuration

sudo /usr/sbin/useradd -rm -g apache -d /opt/indico -s /bin/bash indico
mkdir -p /opt/indico
chown -R indico /opt/indico

echo 'LoadModule proxy_uwsgi_module modules/mod_proxy_uwsgi.so' > /etc/httpd/conf.modules.d/proxy_uwsgi.conf


systemctl daemon-reload
sudo mkdir -p /opt/pgsql/data
sudo chown -R postgres:postgres /opt/pgsql

postgresql-setup initdb
systemctl start postgresql.service redis.service
systemctl enable postgresql.service redis.service
su - postgres -c 'createuser indico'
su - postgres -c 'createdb -O indico indico'
su - postgres -c 'psql indico -c "CREATE EXTENSION unaccent; CREATE EXTENSION pg_trgm;"'
##systemctl start postgresql.service redis.service
systemctl enable postfix.service
systemctl start postfix.service

systemctl enable httpd.service postgresql.service redis.service indico-celery.service indico-uwsgi.service

firewall-cmd --permanent --add-port 443/tcp --add-port 80/tcp
firewall-cmd --reload

semodule -i /etc/ssl/indico/indico.cil


openssl req -x509 -nodes -newkey rsa:4096 -subj /CN=$THISHOSTNAME -keyout /etc/ssl/indico/indico.key -out /etc/ssl/indico/indico.crt


cat >> /opt/indico/.bashrc <<'EOF'
export PATH="/opt/indico/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
EOF

sudo -u indico ln -s  /opt/indico/etc/indico.conf /opt/indico/.indico.conf

sudo -u indico mkdir -p /opt/indico/tmp
sudo -u indico mkdir -p  /opt/indico/log
sudo -u indico mkdir -p /opt/indico/cache
sudo -u indico mkdir -p /opt/indico/archive
sudo -u indico mkdir -p /opt/indico/web
sudo -u indico mkdir -p /opt/indico/etc/

#NEW
sudo -u indico mkdir -p /opt/indico/assets

sudo -u indico mkdir -p /opt/indico/tmp/

sudo -u indico cp /usr/lib/python%{python3_version}/site-packages/indico/logging.yaml.sample  /opt/indico/etc/logging.yaml
##
sudo -u indico mkdir -p /opt/indico/web/static
sudo -u indico mkdir -p /opt/indico/web/static/plugins
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico/web/static/css /opt/indico/web/static/css
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico/web/static/dist /opt/indico/web/static/dist
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico/web/static/fonts /opt/indico/web/static/images
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico/web/static/export-reversed.xsl /opt/indico/web/static/export-reversed.xsl
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico/web/static/export.xsl /opt/indico/web/static/export.xsl
sudo -u indico ln -s    /usr/lib/python{python3_version}/site-packages/indico/web/static/robots.txt /opt/indico/web/static/robots.txt

sudo -u indico mkdir -p /opt/indico/web/static/plugins/cloud_captchas
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_cloud_captchas/static/dist  /opt/indico/web/static/plugins/cloud_captchas/dist

sudo -u indico mkdir -p /opt/indico/web/static/plugins/indico_owncloud
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_indico_owncloud/static/dist  /opt/indico/web/static/plugins/indico_owncloud/dist

sudo -u indico mkdir -p /opt/indico/web/static/plugins/payment_manual
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_payment_manual/static/images  /opt/indico/web/static/plugins/payment_manual/images

sudo -u indico mkdir -p /opt/indico/web/static/plugins/payment_paypal
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_payment_paypal/static/images  /opt/indico/web/static/plugins/payment_paypal/images

sudo -u indico mkdir -p /opt/indico/web/static/plugins/piwik
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_piwik/static/images  /opt/indico/web/static/plugins/piwik/images
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_piwik/static/dist  /opt/indico/web/static/plugins/piwik/dist

sudo -u indico mkdir -p /opt/indico/web/static/plugins/previewer_jupyter
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_previewer_jupyter/static/dist  /opt/indico/web/static/plugins/previewer_jupyter/dist

sudo -u indico mkdir -p /opt/indico/web/static/plugins/themes_legacy
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_themes_legacy/static/dist  /opt/indico/web/static/plugins/themes_legacy/dist

sudo -u indico mkdir -p /opt/indico/web/static/plugins/ursh
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_ursh/static/dist  /opt/indico/web/static/plugins/ursh/dist

sudo -u indico mkdir -p /opt/indico/web/static/plugins/vc_dummy
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_vc_dummy/static/images  /opt/indico/web/static/plugins/vc_dummy/images


sudo -u indico mkdir -p /opt/indico/web/static/plugins/vc_zoom
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_vc_zoom/static/images  /opt/indico/web/static/plugins/vc_zoom/images
sudo -u indico ln -s    /usr/lib/python%{python3_version}/site-packages/indico_vc_zoom/static/dist  /opt/indico/web/static/plugins/vc_zoom/dist

#
sudo -u indico ln -s /opt/indico/etc/indico.conf /opt/indico/.indico.conf 

python3 -m venv --system-site-packages --prompt indico /opt/indico/.venv
sudo -u indico mkdir -p /opt/indico/log/apache
sudo -u indico chmod go-rwx /opt/indico/* /opt/indico/.[^.]*
sudo -u indico chmod 710 /opt/indico/ /opt/indico//archive /opt/indico/cache /opt/indico//log /opt/indico//tmp
sudo -u indico chmod 750 /opt/indico/web /opt/indico//.venv
sudo -u indico chmod g+w /opt/indico/log/apache

sudo -u indico mkdir -p /opt/indico/etc/
restorecon -R /opt/indico/

####  WARNING! Commenting the line below will reduce performance, but might be useful for debug.
echo -e "\nSTATIC_FILE_METHOD = 'xsendfile'" >> /opt/indico/etc/indico.conf

chown -R indico /opt/indico/
chown -R indico /opt/indico/.bashrc
chgrp -R apache /opt/indico
chgrp -R apache /opt/indico/cache
chgrp  apache /opt/indico/.bashrc

#NEW
chgrp -R apache /opt/indico/assets
sudo -u indico indico db prepare

sudo /usr/sbin/setsebool -P httpd_can_network_connect 1
sudo -u indico cp /usr/lib/python%{python3_version}/site-packages/indico/web/indico.wsgi  /opt/indico/web/indico.wsgi




%files -n python3-indico-mpp-configuration
/etc/uwsgi-indico.ini
/etc/systemd/system/indico-uwsgi.service
/etc/httpd/conf.d/indico.conf
/etc/systemd/system/indico-celery.service
/etc/ssl/indico/ffdhe2048
/etc/httpd/conf.d/indico-sslredir.conf
/etc/ssl/indico/indico.cil
%config(noreplace) /opt/indico/etc/indico.conf
#{python3_sitelib}/indico/web/static/images/logo_indico_bw.svg
#{python3_sitelib}/indico/web/static/images/globe.png
%{python3_sitelib}/indico/web/static/robots.txt
%{python3_sitelib}/indico/modules/auth/templates/register.html
/etc/systemd/system/postgresql.service.d/indicopostgresql.conf

%changelog
* Wed Feb 28 2024 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.3
- Version 3.3. Bump version.
* Wed Sep 28 2022 Andrii Verbytskyi andrii.verbytskyi@mpp.mpg.de> - 3.2
- Version 3.2. Removed duplicated packages in dependencies.

