buildroot_fmcomms_gnuradio
==========================

Currently set to use 2017_R1

Designed for ZedBoard Rev C with FMCOMMS2/3 SDR device. Includes proper drivers for SDR device and full gnuradio build. Supports SSH.

To create the buildroot design

`./populate_buildroot.sh`

[Notes on Generating HW Files](https://wiki.analog.com/resources/tools-software/linux-software/build-the-zynq-boot-image)

[Downloading HW Files](https://wiki.analog.com/resources/tools-software/linux-software/zynq_images)

Compiling Linux Kernel
---------------------
The Linux Kernel is stored in the `linux` folder submodule (Using Branch 2017_R1)


```
export ARCH=arm 
export CROSS_COMPILE=arm-xilinx-linux-gnueabi-
make zynq_xcomm_adv7511_defconfig
make UIMAGE_LOADADDR=0x8000 uImage
```

Creating Vivado Project
-----------------------
The project is stored in the `hdl` folder submodule (Using Branch 2017_R1; requires Vivado 2016.4+)
```
cd projects/fmcomms2/zed
make
```

Package Support Added
---------------------

* libad9361-iio (git commit `b98b1cd2280d73ced04cb4cf9482b2d2d91e31a2`)

* gr-iio (git commit `7079c1a60206fba4b37beb239bf25438ec8d9778`)

* libiio Updated to use v0.15

* gnuradio modified packages enabled

  * ZeroMQ

  * GRC

Usage with SD Card
------------------

Make sure compatible filesystem exists on SD card

|name  |filesystem|size|
|------|----------|----|
|BOOT  |  fat16   |36Mb|
|rootfs|  ext4    |max |

extract the output after building:

`cd /path/to/rootfs`

`sudo tar -xvf /path/to/buildroot-2016.08-rc1/output/images/rootfs.tar ./`

Files for the BOOT partition can be found in `./buildroot_fmcomms_gnuradio/BOOT`

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

**Physical Connections**

![zedboardconnections](https://github.com/gutelfuldead/buildroot_fmcomms_gnuradio/blob/master/images/zedboard_fmcomms3.jpg)

**gnuradio**

Platform has already been profiled by volk and is available in `/home/fmcomms/.volk/volk_config`

Scripts are pre-populated to test a loopback wbfm signal and stream the data to a host computer. The GNU Radio flowchart to be used on the host PC can be found in `buildroot_fmcomms_gnuradio/pcstream`.

Ensure ZedBoard is connected via hub with the PC and the PC is on the appropriate network settings to communicate with the aforementioned zedboard network settings.

Gnuradio example files in: `/home/fmcomms/gnuradio/` to run simply execute the `.py` file

`sin_f10e3_tcp_wbfm_stream.grc` expected output:

![sin test](https://github.com/gutelfuldead/buildroot_fmcomms_gnuradio/blob/master/images/sin_output.png)

`loopback_tcp_wbfm_stream.py` expected output:
![csp-sdr.wav waterfall output](https://github.com/gutelfuldead/buildroot_fmcomms_gnuradio/blob/master/images/waterfall_csp_sdr.png)

Actual Spectral Image:
![csp-sdr.wav spectral](https://github.com/gutelfuldead/buildroot_fmcomms_gnuradio/blob/master/images/spectral_sdr_csp.png)
