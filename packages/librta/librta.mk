################################################################################
#
# librta
#
################################################################################

LIBRTA_VERSION = 93ea6760ec6f07c4530cabcba17ea6a6e17b98b3 
LIBRTA_SITE = $(call github,librta,librta,$(LIBAD9361_IIO_VERSION))
LIBRTA_LICENSE = MIT
LIBRTA_LICENSE_FILES = COPYING

LIBRTA_INSTALL_STAGING = YES

$(eval $(cmake-package))
