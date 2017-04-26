buildroot_fmcomms_gnuradio
==================

Requires [buildroot-2016.08-rc1](https://buildroot.org/downloads/buildroot-2016.08-rc1.tar.gz)

Configuration files and packages for buildroot. 

Designed for ZedBoard Rev C with FMCOMMS2/3 SDR device. Includes proper drivers for SDR device and full gnuradio build. Supports SSH.

To auto-update buildroot run

`./populate_buildroot.sh ./path/to/buildroot-2016.08-rc1`

If no argument provided scripts assumes the relative path from this repository is `../buildroot-2016.08-rc1`

Usage with SD Card
------------------

Make sure compatible filesystem exists

|name|filesystem|size|
|----|----------|----|
|BOOT|fat16|36Mb|
|rootfs|ext4|max|

extract the output after building:

`cd /path/to/rootfs`

`sudo tar -xvf /path/to/buildroot-2016.08-rc1/output/images/rootfs.tar ./`

Login Info
----------

User fmcomms is in the sudoers file and has access to dialout,sshd groups.

|user|password|
|----|--------|
|root|      |
|fmcomms|fmcomms|
