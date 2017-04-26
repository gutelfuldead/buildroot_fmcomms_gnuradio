#!/bin/bash
export LD_LIBRARY_PATH=/usr/lib

#start IIOD
sudo /usr/sbin/iiod &
#run the transmission
~/gnuradio/fm_txrx_net_sink.py
