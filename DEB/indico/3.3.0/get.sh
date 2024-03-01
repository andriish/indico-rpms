p=indico
v=3.3.0
set -x
rm -rf XXX
mkdir XXX
cd XXX
wget -q https://github.com/indico/indico/archive/11daf353758a3b32e5ef37ca3e932f97c37ce8ca.tar.gz -O $p"_"$v.orig-main.tar.gz     
wget -q https://github.com/indico/indico-plugins/archive/refs/tags/v3.2.2.tar.gz -O  $p"_"$v.orig-plugins-base.tar.gz
rm -rf $p-$v
mkdir -p $p-$v
tar zxf  $p"_"$v.orig-main.tar.gz -C $p-$v 
mv $p-$v/$p-11daf353758a3b32e5ef37ca3e932f97c37ce8ca $p-$v/$p-$v
mkdir -p $p-$v/$p-$v/plugins
tar zxf   $p"_"$v.orig-plugins-base.tar.gz -C $p-$v/$p-$v/plugins/
mv $p-$v/$p-$v/plugins/indico-plugins-3.2.2 $p-$v/$p-$v/plugins/base
rm -rf $p"_"$v.orig-plugins-base.tar.gz $p"_"$v.orig-main.tar.gz     
cd $p-$v/$p-$v
tar -zcf ../../../$p"_"$v.orig.tar.gz  .
cd ../../../
rm -rf XXX