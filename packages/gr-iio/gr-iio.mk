################################################################################
#
# gr-iio 
#
# issue locating gnuradio-analog.pc in cmake
#
################################################################################

GR_IIO_VERSION = 9b58414b4db711823eb7e5d6e11aa39bfcaf2bac 
GR_IIO_SITE = $(call github,analogdevicesinc,gr-iio,$(GR_IIO_VERSION))
GR_IIO_LICENSE = GPLv3
GR_IIO_LICENSE_FILES = COPYING

# make sure gnuradio analog is installed...
# install gnuradio and blocks initially
# after image completely built add gnuradio analog support
# run $ make gnuradio-reconfigure
GR_IIO_DEPENDENCIES = gnuradio libiio libad9361-iio

GR_IIO_INSTALL_STAGING = YES

GR_IIO_CONF_OPTS = -DENABLE_DOXYGEN=OFF

$(eval $(cmake-package))

