buildroot_fmcomms_gnuradio
==================

Requires [buildroot-2016.08-rc1](https://buildroot.org/downloads/buildroot-2016.08-rc1.tar.gz)

Configuration files and packages for buildroot. 

Designed for ZedBoard Rev C with FMCOMMS2/3 SDR device. Includes proper drivers for SDR device and full gnuradio build. Supports SSH.

To auto-update buildroot run

`./populate_buildroot.sh`

Script assumes/requires folder hierarchy of:

```
|	./PWD
|_______|	buildroot-2016.08-rc1
|_______|	buildroot_fmcomms_gnuradio
```

Since the path to the users description and rootfs overlay are hardcoded in the config files this structure must be preserved.

Package Support Added
---------------------

* libad9361-iio

* gr-iio

* gnuradio modified packages enabled

  * ZeroMQ

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

Environment Setup
-----------------

**Login info:**

|user|password|
|----|--------|
|root|      |
|fmcomms|fmcomms|

User fmcomms is in the sudoers file and has access to dialout,sshd groups and has a configured bashrc

**Default eth0 static ipv4 info:**

|ip|subnet|gateway|
|--|------|-------|
|192.168.0.20|255.255.255.0|192.168.0.1|

**gnuradio**

Platform has already been profiled by volk and is available in `/home/fmcomms/.volk/volk_profile`

Scripts are pre-populated to test a loopback nbfm signal and stream the data to a host computer. 

Gnuradio example files in: `/home/fmcomms/gnuradio/`
