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

|name  |filesystem|size|
|------|----------|----|
|BOOT  |  fat16   |36Mb|
|rootfs|  ext4    |max |

extract the output after building:

`cd /path/to/rootfs`

`sudo tar -xvf /path/to/buildroot-2016.08-rc1/output/images/rootfs.tar ./`

Environment Setup
-----------------

**Login info:**

|user   |password|
|-------|--------|
|root   |        |
|fmcomms| fmcomms|

User fmcomms is in the sudoers file and has access to dialout,sshd groups and has a configured bashrc

**Default eth0 static ipv4 info:**

|   ip       | subnet      |gateway    |
|------------|-------------|-----------|
|192.168.0.20|255.255.255.0|192.168.0.1|

**gnuradio**

Platform has already been profiled by volk and is available in `/home/fmcomms/.volk/volk_config`

Scripts are pre-populated to test a loopback wbfm signal and stream the data to a host computer. The GNU Radio flowchart to be used on the host PC can be found in `buildroot_fmcomms_gnuradio/pcstream`.

Ensure ZedBoard is connected via hub with the PC and the PC is on the appropriate network settings to communicate with the aforementioned zedboard network settings.

Gnuradio example files in: `/home/fmcomms/gnuradio/`

Expected output as seen from PC. This image is obviously distorted and can be cleaned by a better modulation scheme; the concern here is simply hardware verification which this shows.

![csp-sdr.wav waterfall output](https://github.com/gutelfuldead/buildroot_fmcomms_gnuradio/blob/master/pcstream/waterfall_csp_sdr.png)
