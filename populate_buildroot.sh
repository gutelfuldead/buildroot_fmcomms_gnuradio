#!/bin/bash

if [ "$1" = '' ]; then
	BROOTPATH=../buildroot-2016.08-rc1
else
	BROOTPATH=$1
fi

echo ">>> Copying all files into $BROOTPATH ..."
cp ./config_files/buildroot_config $BROOTPATH/.config
cp ./config_files/package_config $BROOTPATH/package/Config.in

cp -r ./packages/gr-iio packages/libad9361-iio $BROOTPATH/package
cp -r ./packages/gnuradio_patches/* $BROOTPATH/package/gnuradio/

