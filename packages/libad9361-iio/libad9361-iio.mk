################################################################################
#
# libad9361-iio
#
################################################################################

LIBAD9361_IIO_VERSION = b98b1cd2280d73ced04cb4cf9482b2d2d91e31a2 
LIBAD9361_IIO_SITE = $(call github,analogdevicesinc,libad9361-iio,$(LIBAD9361_IIO_VERSION))
LIBAD9361_IIO_LICENSE = LGPLv2.1
LIBAD9361_IIO_LICENSE_FILES = COPYING

LIBAD9361_IIO_DEPENDENCIES = libiio

LIBAD9361_IIO_INSTALL_STAGING = YES

$(eval $(cmake-package))
