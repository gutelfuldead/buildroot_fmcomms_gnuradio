#!/bin/bash

BROOTPATH=./buildroot

git submodule update --init buildroot &&
cd buildroot
git checkout 2016.08.x
cd ..

echo ">>> Copying all files into $BROOTPATH"
cp ./config_files/buildroot_config $BROOTPATH/.config
cp ./config_files/package_config $BROOTPATH/package/Config.in

cp -r ./packages/gr-iio packages/libad9361-iio $BROOTPATH/package
cp -r ./packages/gnuradio_patches/* $BROOTPATH/package/gnuradio/

