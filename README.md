# buildroot_fmcomms_gnuradio

Currently set to use Analog Devices and Xilinx builds : 2017_R1. 

Buildroot version 2018.02.2

Designed for ZedBoard Rev C with FMCOMMS2/3 SDR device. 

Includes proper drivers for SDR device and full gnuradio build.

--------------------------------------------------------------------------------------

# File Structure
```
.
├── BOOT
│   ├── BOOT.BIN
│   ├── devicetree.dtb
│   ├── uEnv.txt
│   ├── uImage
│   └── VERSION
├── config_files
│   ├── buildroot_config
│   ├── package_config
│   └── users.desc
├── cross_compile
│   └── Makefile
├── gnuradio_designs
│   └── qpsk_ber_fmcomms
│       ├── ber_simulation.py
│       ├── peak_detector_random_number_gen.py
│       ├── peak_detector_random_number_gen_test.grc
│       ├── qpsk_modem_fmcomms.grc
│       ├── qpsk_modem_fmcomms.py
│       ├── qpsk_modem_loopback.grc
│       ├── qpsk_modem_pc.grc
│       └── qpsk_modem_pc.py
├── hdl
├── images
│   ├── sin_output.png
│   ├── spectral_sdr_csp.png
│   ├── waterfall_csp_sdr.png
│   └── zedboard_fmcomms3.jpg
├── import_submodules.sh
├── linux
├── packages
│   ├── gnuradio_patches
│   │   ├── Config.in
│   │   └── gnuradio.mk
│   ├── gr-iio
│   │   ├── Config.in
│   │   └── gr-iio.mk
│   ├── libad9361-iio
│   │   ├── Config.in
│   │   └── libad9361-iio.mk
│   └── libiio_patch
│       ├── libiio.hash
│       └── libiio.mk
├── pcstream
│   └── pc_stream.grc
├── populate_buildroot.sh
├── README.md
└── rootfs_overlay
    ├── etc
    │   ├── network
    │   │   └── interfaces
    │   ├── profile
    │   └── sudoers
    └── home
        └── fmcomms
            ├── c_example_code
            │   ├── ad9361-iiostream.c
            │   ├── hello
            │   ├── hello.c
            │   ├── iiostream
            │   └── Makefile
            └── gnuradio
                ├── loopback_tcp_wbfm_stream.grc
                ├── loopback_tcp_wbfm_stream.py
                ├── sdr-csp.wav
                ├── sin_f10e3_tcp_wbfm_stream.grc
                └── sin_f10e3_tcp_wbfm_stream.py

21 directories, 46 files
```

--------------------------------------------------------------------------------------

# Build Root Usage

## Packages Required for Build Root
g++
libssl-dev
libncurses5-dev

## Build Root Packages Added

* libad9361-iio (git commit `b98b1cd2280d73ced04cb4cf9482b2d2d91e31a2`)

* gr-iio (git commit `7079c1a60206fba4b37beb239bf25438ec8d9778`)

* libiio Updated to use v0.15

* gnuradio modified packages enabled

  * ZeroMQ

  * GRC

## Generate Build Root File System

**WARNING** : This requires about 10GB of space to generate everything

To create the buildroot design

`./populate_buildroot.sh`

This will create `./buildroot-2018.02.2` subdirectory. To generate the filesystem,

`cd buildroot-2018.02.2 && make`

A sample Makefile to generate executables for this target is in `./cross_compile`

## Build Root Output Products

Generated Filesystem,

`buildroot-2018.02.2/output/images/rootfs.tar` (200 M)

Generated uImage (Created from AD Linux Distribution)

`buildroot-2018.02.2/output/images/uImage`


## Setting up SD Card

Make sure compatible filesystem exists on SD card

|name  |filesystem|size|
|------|----------|----|
|BOOT  |  fat16   |36Mb|
|rootfs|  ext4    |max |

extract the output after building:

`cd /path/to/rootfs`

`sudo tar -xvf /path/to/buildroot-2016.08-rc1/output/images/rootfs.tar ./`

Files for the BOOT partition can be found in `./buildroot_fmcomms_gnuradio/BOOT`

## Build Root Environment

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

## rootfs overlay included files

**Physical Connections**

![zedboardconnections](https://github.com/gutelfuldead/buildroot_fmcomms_gnuradio/blob/master/images/zedboard_fmcomms3.jpg)

**IIO Stream Example**

An example compiled IIO Stream for the AD9361 is included in ~/c_example_code/iiostream

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

--------------------------------------------------------------------------------------

# Cross Compiling on the Target

An example cross compilation Makefile (`example_makefile_cross_compile`) provided which was used to generate the iiostream file.

--------------------------------------------------------------------------------------

# Useful Links

[Notes on Generating ZedBoard HW Files](https://wiki.analog.com/resources/tools-software/linux-software/build-the-zynq-boot-image)

[Downloading ZedBoard HW Files](https://wiki.analog.com/resources/tools-software/linux-software/zynq_images)

[Cross Compiling LIBIIO and general information for cmake cross compiling](https://wiki.analog.com/resources/tools-software/linux-software/libiio#cross-compilation)

[github Analog Devies Linux Kernel 2017_R1](https://github.com/analogdevicesinc/linux)

[github Analog Devices HDL](https://github.com/analogdevicesinc/hdl)

[github Analog Devices GR-IIO](https://github.com/analogdevicesinc/gr-iio)

[github Analog Devices libad9361-iio](https://github.com/analogdevicesinc/libad9361-iio)

--------------------------------------------------------------------------------------

# Analog Devices GITS

## Compiling Linux Kernel

```
export ARCH=arm 
export CROSS_COMPILE=arm-xilinx-linux-gnueabi-
make zynq_xcomm_adv7511_defconfig
make UIMAGE_LOADADDR=0x8000 uImage
```

## Creating Vivado Project

```
cd projects/fmcomms2/zed
make
```
