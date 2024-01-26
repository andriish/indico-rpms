
p=$1
v=$2
P=$3
u=https://pypi.io/packages/source/$(echo $p | head -c 1)/$p/$P-$v.tar.gz
cd $p/$v
TOP=$(pwd)
rm -rf mydbtop
mkdir -p mydbtop/BUILD
cd mydbtop/BUILD
cp -r $TOP/debian ./
wget $u -O ../$p"_"$v.orig.tar.gz
tar zxfv ../$p"_"$v.orig.tar.gz 
mv $P-$v/* ./
dpkg-buildpackage -us -uc
