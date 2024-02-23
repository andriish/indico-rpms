#!/bin/bash
           export TOP=$(pwd)           
           mkdir COMPILE
           cd COMPILE/
           wget https://github.com/indico/indico/archive/refs/tags/v3.2.9.zip
           unzip -q v3.2.9.zip 
           wget https://github.com/indico/indico-plugins/archive/refs/tags/v3.2.2.tar.gz
           tar xf  v3.2.2.tar.gz 
           cd indico-3.2.9/
           cp -r $TOP/python-indico/3.2.9/PATCHED/* ./
           mkdir -p plugins
           mv ../indico-plugins-3.2.2/ plugins/base
           rm -rf plugins/base/piwik
           rm -rf plugins/base/themes_legacy
           rm -rf plugins/base/ursh
           rm -rf plugins/base/vc_zoom
           rm -rf plugins/base/cloud_captchas
           rm -rf plugins/base/owncloud
           rm -rf plugins/base/previewer_jupyter
           sed -i 's/iso4217\=\=.*$/iso4217/g'     plugins/base/*/setup.cfg
           sed -i 's/nbconvert\=\=.*$/nbconvert/g' plugins/base/*/setup.cfg
           sed -i 's/indico-plugin-piwik.*$//g'    plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-ursh.*$//g'     plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-vc-zoom.*$//g'  plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-cloud-captchas.*$//g'  plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-owncloud.*$//g'  plugins/base/_meta/setup.cfg
           sed -i 's/indico-plugin-previewer-jupyter.*$//g'  plugins/base/_meta/setup.cfg
           sed -i 's/\=\=.*$//g' requirements.*
           sed -i 's/tzdata/#tzdata/g' requirements.*
           sed -i 's/pypdf/#pypdf/g' requirements.*
           sed -i 's/importlib/#importlib/g' requirements.*
           export NODE_OPTIONS="--max-old-space-size=5120"
           export PYTHONPATH=$(pwd):$PYTHONPATH
           mkdir -p indico/web/client
           cd indico/web/client
           npm install
           cd ../../../
           npm install
           ./bin/maintenance/build-wheel.py indico       --ignore-unclean 
           ./bin/maintenance/build-wheel.py all-plugins  --ignore-unclean  plugins/base

