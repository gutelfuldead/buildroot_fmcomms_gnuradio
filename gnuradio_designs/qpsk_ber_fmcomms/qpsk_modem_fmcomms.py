#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: qpsk_modem_fmcomms
# Generated: Fri Nov 10 15:13:34 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import numpy


class qpsk_modem_fmcomms(gr.top_block):

    def __init__(self, pc_host_ip='192.168.0.10'):
        gr.top_block.__init__(self, "qpsk_modem_fmcomms")

        ##################################################
        # Parameters
        ##################################################
        self.pc_host_ip = pc_host_ip

        ##################################################
        # Variables
        ##################################################
        self.system_samp_rate = system_samp_rate = 131072
        self.sample_size = sample_size = int(10e6)
        self.rf_freq = rf_freq = int(2.6*10**9)
        self.output_bits_port = output_bits_port = 12347
        self.modulated_data_tx_port = modulated_data_tx_port = 12348
        self.modulated_data_rx_port = modulated_data_rx_port = 12349
        self.input_bits_port = input_bits_port = 12346
        self.fmcomms_samp_rate = fmcomms_samp_rate = 2536000
        self.data_rate = data_rate = system_samp_rate/16
        self.const_type = const_type = 1
        self.const = const = (digital.constellation_bpsk(), digital.constellation_qpsk(), digital.constellation_8psk())
        self.DAC_scale = DAC_scale = 4096

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=fmcomms_samp_rate,
                decimation=data_rate,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=fmcomms_samp_rate,
                decimation=data_rate,
                taps=None,
                fractional_bw=None,
        )
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source('local:', rf_freq, fmcomms_samp_rate, 1 - 1, 20000000, True, False, False, False, 0x8000, True, True, True, "fast_attack", 64.0, "fast_attack", 64.0, "A_BALANCED", '')
        self.iio_fmcomms2_sink_0 = iio.fmcomms2_sink('local:', rf_freq, fmcomms_samp_rate, 1 - 1, 20000000, True, False, False, False, 0x8000, False, "A", 10.0, 10.0, '')
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(const[const_type].base())
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const[const_type].points()), 1)
        self.blocks_sample_and_hold_xx_0 = blocks.sample_and_hold_bb()
        self.blocks_peak_detector2_fb_0 = blocks.peak_detector2_fb(7, 1000, 0.001)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((DAC_scale, ))
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(False, False)
        self.blocks_complex_to_interleaved_short_0 = blocks.complex_to_interleaved_short(False)
        self.blks2_tcp_sink_1_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr=pc_host_ip,
        	port=modulated_data_rx_port,
        	server=False,
        )
        self.blks2_tcp_sink_1 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr=pc_host_ip,
        	port=modulated_data_tx_port,
        	server=False,
        )
        self.blks2_tcp_sink_0_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_char*1,
        	addr=pc_host_ip,
        	port=output_bits_port,
        	server=False,
        )
        self.blks2_tcp_sink_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_char*1,
        	addr=pc_host_ip,
        	port=input_bits_port,
        	server=False,
        )
        self.analog_sig_source_x_0 = analog.sig_source_f(system_samp_rate, analog.GR_COS_WAVE, data_rate, 1, 0)
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, 4, sample_size)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x, 0), (self.blocks_sample_and_hold_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_peak_detector2_fb_0, 0))
        self.connect((self.blocks_complex_to_interleaved_short_0, 0), (self.iio_fmcomms2_sink_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_peak_detector2_fb_0, 0), (self.blocks_sample_and_hold_xx_0, 1))
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.blks2_tcp_sink_0, 0))
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.blks2_tcp_sink_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_tcp_sink_0_0, 0))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_interleaved_short_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blks2_tcp_sink_1_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.digital_constellation_decoder_cb_0, 0))

    def get_pc_host_ip(self):
        return self.pc_host_ip

    def set_pc_host_ip(self, pc_host_ip):
        self.pc_host_ip = pc_host_ip

    def get_system_samp_rate(self):
        return self.system_samp_rate

    def set_system_samp_rate(self, system_samp_rate):
        self.system_samp_rate = system_samp_rate
        self.set_data_rate(self.system_samp_rate/16)
        self.analog_sig_source_x_0.set_sampling_freq(self.system_samp_rate)

    def get_sample_size(self):
        return self.sample_size

    def set_sample_size(self, sample_size):
        self.sample_size = sample_size

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        self.iio_fmcomms2_source_0.set_params(self.rf_freq, self.fmcomms_samp_rate, 20000000, True, True, True, "fast_attack", 64.0, "fast_attack", 64.0, "A_BALANCED")
        self.iio_fmcomms2_sink_0.set_params(self.rf_freq, self.fmcomms_samp_rate, 20000000, "A", 10.0, 10.0)

    def get_output_bits_port(self):
        return self.output_bits_port

    def set_output_bits_port(self, output_bits_port):
        self.output_bits_port = output_bits_port

    def get_modulated_data_tx_port(self):
        return self.modulated_data_tx_port

    def set_modulated_data_tx_port(self, modulated_data_tx_port):
        self.modulated_data_tx_port = modulated_data_tx_port

    def get_modulated_data_rx_port(self):
        return self.modulated_data_rx_port

    def set_modulated_data_rx_port(self, modulated_data_rx_port):
        self.modulated_data_rx_port = modulated_data_rx_port

    def get_input_bits_port(self):
        return self.input_bits_port

    def set_input_bits_port(self, input_bits_port):
        self.input_bits_port = input_bits_port

    def get_fmcomms_samp_rate(self):
        return self.fmcomms_samp_rate

    def set_fmcomms_samp_rate(self, fmcomms_samp_rate):
        self.fmcomms_samp_rate = fmcomms_samp_rate
        self.iio_fmcomms2_source_0.set_params(self.rf_freq, self.fmcomms_samp_rate, 20000000, True, True, True, "fast_attack", 64.0, "fast_attack", 64.0, "A_BALANCED")
        self.iio_fmcomms2_sink_0.set_params(self.rf_freq, self.fmcomms_samp_rate, 20000000, "A", 10.0, 10.0)

    def get_data_rate(self):
        return self.data_rate

    def set_data_rate(self, data_rate):
        self.data_rate = data_rate
        self.analog_sig_source_x_0.set_frequency(self.data_rate)

    def get_const_type(self):
        return self.const_type

    def set_const_type(self, const_type):
        self.const_type = const_type
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const[self.const_type].points()))

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const[self.const_type].points()))

    def get_DAC_scale(self):
        return self.DAC_scale

    def set_DAC_scale(self, DAC_scale):
        self.DAC_scale = DAC_scale
        self.blocks_multiply_const_vxx_0.set_k((self.DAC_scale, ))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--pc-host-ip", dest="pc_host_ip", type="string", default='192.168.0.10',
        help="Set pc_host_ip [default=%default]")
    return parser


def main(top_block_cls=qpsk_modem_fmcomms, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(pc_host_ip=options.pc_host_ip)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
