################################################################################
#
# libad9361-iio
#
################################################################################

LIBAD9361_IIO_VERSION = af541b1b3f1e2462d18abdba2a108df2bfd55647 
LIBAD9361_IIO_SITE = $(call github,analogdevicesinc,libad9361-iio,$(LIBAD9361_IIO_VERSION))
LIBAD9361_IIO_LICENSE = LGPLv2.1
LIBAD9361_IIO_LICENSE_FILES = COPYING

LIBAD9361_IIO_DEPENDENCIES = libiio

LIBAD9361_IIO_INSTALL_STAGING = YES

$(eval $(cmake-package))
