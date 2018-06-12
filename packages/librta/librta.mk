################################################################################
#
# librta
#
################################################################################

LIBRTA_VERSION = 93ea6760ec6f07c4530cabcba17ea6a6e17b98b3 
LIBRTA_SITE = $(call github,librta,librta,$(LIBRTA_VERSION))
LIBRTA_LICENSE = MIT
LIBRTA_LICENSE_FILES = COPYING
LIBRTA_INSTALL_STAGING = YES
LIBRTA_MAKEFILE_PATH = output/build/librta-$(LIBRTA_VERSION)/src

define LIBRTA_BUILD_CMDS
	$(MAKE) -C $(LIBRTA_MAKEFILE_PATH) $(TARGET_CONFIGURE_OPTS) default
endef

define LIBRTA_INSTALL_TARGET_CMDS
	$(INSTALL) -D -m 0755 $(@D)/src/librta.so* $(TARGET_DIR)/usr/lib
endef

$(eval $(generic-package))
