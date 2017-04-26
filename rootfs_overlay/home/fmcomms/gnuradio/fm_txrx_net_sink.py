#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fm Txrx Net Sink
# Generated: Tue Apr 25 16:26:38 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class fm_txrx_net_sink(gr.top_block):

    def __init__(self, hostname="127.0.0.1", interpolation=2, wav_file="/home/analog/Music/Epoq.wav"):
        gr.top_block.__init__(self, "Fm Txrx Net Sink")

        ##################################################
        # Parameters
        ##################################################
        self.hostname = hostname
        self.interpolation = interpolation
        self.wav_file = wav_file

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3072000
        self.fm_station = fm_station = 4*10**9
        self.decimation = decimation = 2

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "192.168.0.10", 100, False, -1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=8 / interpolation,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(samp_rate / (384000 * decimation), firdes.low_pass(
        	1, samp_rate, 44100, 44100, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source(hostname, fm_station, samp_rate, decimation - 1, 20000000, False, False, True, True, 0x8000, True, True, True, "slow_attack", 64.0, "slow_attack", 64.0, "A_BALANCED", "")
        self.iio_fmcomms2_sink_0_0 = iio.fmcomms2_sink(hostname, fm_station, samp_rate, interpolation - 1, 20000000, True, True, False, False, 0x8000, False, "A", 10.0, 10.0, "")
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/fmcomms/gnuradio/sdr-csp.wav", True)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((32768, ))
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 1)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=48000,
        	quad_rate=samp_rate / 64,
        	tau=75e-6,
        	max_dev=75e3,
                )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.iio_fmcomms2_sink_0_0, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.iio_fmcomms2_sink_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 1), (self.blocks_add_xx_0, 1))    
        self.connect((self.iio_fmcomms2_source_0, 0), (self.blocks_short_to_float_0, 0))    
        self.connect((self.iio_fmcomms2_source_0, 1), (self.blocks_short_to_float_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.zeromq_push_sink_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_0, 0))    

    def get_hostname(self):
        return self.hostname

    def set_hostname(self, hostname):
        self.hostname = hostname

    def get_interpolation(self):
        return self.interpolation

    def set_interpolation(self, interpolation):
        self.interpolation = interpolation

    def get_wav_file(self):
        return self.wav_file

    def set_wav_file(self, wav_file):
        self.wav_file = wav_file

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.iio_fmcomms2_sink_0_0.set_params(self.fm_station, self.samp_rate, 20000000, "A", 10.0, 10.0)
        self.iio_fmcomms2_source_0.set_params(self.fm_station, self.samp_rate, 20000000, True, True, True, "slow_attack", 64.0, "slow_attack", 64.0, "A_BALANCED")
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 44100, 44100, firdes.WIN_HAMMING, 6.76))

    def get_fm_station(self):
        return self.fm_station

    def set_fm_station(self, fm_station):
        self.fm_station = fm_station
        self.iio_fmcomms2_sink_0_0.set_params(self.fm_station, self.samp_rate, 20000000, "A", 10.0, 10.0)
        self.iio_fmcomms2_source_0.set_params(self.fm_station, self.samp_rate, 20000000, True, True, True, "slow_attack", 64.0, "slow_attack", 64.0, "A_BALANCED")

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--hostname", dest="hostname", type="string", default="127.0.0.1",
        help="Set Hostname [default=%default]")
    parser.add_option(
        "", "--interpolation", dest="interpolation", type="intx", default=2,
        help="Set Interpolation [default=%default]")
    parser.add_option(
        "", "--wav-file", dest="wav_file", type="string", default="/home/analog/Music/Epoq.wav",
        help="Set WAV File [default=%default]")
    return parser


def main(top_block_cls=fm_txrx_net_sink, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(hostname=options.hostname, interpolation=options.interpolation, wav_file=options.wav_file)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
