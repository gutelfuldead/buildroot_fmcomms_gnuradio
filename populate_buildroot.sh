#!/bin/bash

if [ "$1" = '' ]; then
	BROOTPATH="../buildroot-2016.08-rc1"
	echo "k"
else
	BROOTPATH=$1
	echo "n"
fi

cp buildroot_config $BROOTPATH/.config
cp packages/gr-iio packages/libad9361-iio Config.in $BROOTPATH/packages
cp packages/gnuradio_patches/* $BROOTPATH/gnuradio/