#!/bin/bash

BROOTPATH=./buildroot-2018.02.2

if [ ! -d $BROOTPATH ]; then
	echo ">>> Buildroot path not found... Fetching buildroot..."
	wget https://buildroot.org/downloads/buildroot-2018.02.2.tar.gz 
	tar -xvzf buildroot-2018.02.2.tar.gz
else
	echo ">>> Buildroot path found..."
fi

echo ">>> Copying all files into $BROOTPATH"
cp ./config_files/buildroot_config $BROOTPATH/.config
cp ./config_files/package_config $BROOTPATH/package/Config.in

# copy new packages
cp -r ./packages/gr-iio packages/libad9361-iio $BROOTPATH/package
cp -r ./packages/librta $BROOTPATH/package/librta

# add patches
cp -r ./packages/gnuradio_patches/* $BROOTPATH/package/gnuradio
cp -r ./packages/libiio_patch/* $BROOTPATH/package/libiio

