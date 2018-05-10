# This Example Makefile is for cross compiling onto the Buildroot Zynq Target
# https://wiki.analog.com/resources/tools-software/linux-software/libiio#cross-compilation
# $ file hello 
# hello: ELF 32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked (uses shared libs), not stripped

BROOT_PATH=../buildroot-2018.02.2
CC=$(BROOT_PATH)/output/host/usr/bin/arm-buildroot-linux-uclibcgnueabi-gcc
LDFLAGS=-Wall -g -lc -ldl -lm -lz -lusb-1.0 -lserialport -lxml2 -llzma -liio
LDPATH=-L$(BROOT_PATH)/output/target/lib32 -L$(BROOT_PATH)/output/target/usr/lib
# location of iio.h
INCPATH=-I/home/jgutel/gits/libiio_zynq

iiostream:
	$(CC) -o iiostream ad9361-iiostream.c $(LDFLAGS) $(LDPATH) $(INCPATH)

hello_world:
	$(CC) -o hello hello.c -g

all:iiostream hello_world

.PHONY: clean

clean:
	rm -f *~ *.o hello iiostream