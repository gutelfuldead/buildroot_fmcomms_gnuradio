# This Example Makefile is for cross compiling onto the Buildroot Zynq Target
# https://wiki.analog.com/resources/tools-software/linux-software/libiio#cross-compilation
# $ file foo 
# foo: ELF 32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked (uses shared libs), not stripped

BROOT_PATH=../buildroot-2018.02.2
CC=$(BROOT_PATH)/output/host/usr/bin/arm-buildroot-linux-uclibcgnueabi-gcc
LDFLAGS=-Wall -g3 -lc -ldl -lm -lz -lusb-1.0 -lserialport -lxml2 -llzma -liio
LDPATH=-L$(BROOT_PATH)/output/target/lib32 -L$(BROOT_PATH)/output/target/usr/lib
ROOTFS_FILE_PATH=../rootfs_overlay/home/fmcomms/c_example_code

all: sampTxRx sampCw iiostream

# all builds copy the executable and source code to the target to support
# gdb -tui debugging

sampTxRx:
	@echo ""; echo ">>> Generating sampTxRx and updating rootfs"
	$(CC) -o sampTxRx ./src/fileStreamSample.c $(LDFLAGS) $(LDPATH) 
	cp sampTxRx $(ROOTFS_FILE_PATH)
	cp ./src/fileStreamSample.c $(ROOTFS_FILE_PATH)

sampCw:
	@echo ""; echo ">>> Generating sampCw and updating rootfs"
	$(CC) -o sampCw ./src/cwStreamSample.c $(LDFLAGS) $(LDPATH) 
	cp sampCw $(ROOTFS_FILE_PATH)
	cp ./src/cwStreamSample.c $(ROOTFS_FILE_PATH)

iiostream:
	@echo ""; echo ">>> Generating iio-stream and updating rootfs"
	$(CC) -o iiostream ./src/ad9361-iiostream.c $(LDFLAGS) $(LDPATH)
	cp iiostream $(ROOTFS_FILE_PATH)
	cp ./src/ad9361-iiostream.c $(ROOTFS_FILE_PATH)

.PHONY: clean

clean:
	rm -f *~ *.o hello iiostream sampTxRx sampCw
