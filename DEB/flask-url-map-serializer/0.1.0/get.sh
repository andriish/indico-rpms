p=flask-url-map-serializer
v=0.1.0
mkdir XXX
cd XXX
wget https://github.com/indico/js-flask-urls/archive/refs/tags/babel-plugin-flask-urls@$v.tar.gz -O $p"_"$v.orig1.tar.gz
mkdir -p $p-$v 
tar zxf  $p"_"$v.orig1.tar.gz -C $p-$v 
mv $p-$v/js-flask-urls-babel-plugin-flask-urls-$v $p-$v/$p-$v
cd $p-$v/$p-$v
tar -zcf ../../../$p"_"$v.orig.tar.gz  .
cd ../../../
rm -rf XXX