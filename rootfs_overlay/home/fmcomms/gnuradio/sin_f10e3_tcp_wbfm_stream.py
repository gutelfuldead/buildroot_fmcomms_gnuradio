#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Sin F10E3 Tcp Wbfm Stream
# Generated: Thu Jan  1 00:28:31 1970
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sys


class sin_f10e3_tcp_wbfm_stream(gr.top_block, Qt.QWidget):

    def __init__(self, pc_host_ip="192.168.0.10"):
        gr.top_block.__init__(self, "Sin F10E3 Tcp Wbfm Stream")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Sin F10E3 Tcp Wbfm Stream")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "sin_f10e3_tcp_wbfm_stream")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.pc_host_ip = pc_host_ip

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2536000
        self.rx_port = rx_port = 12346
        self.rf_freq = rf_freq = int(2.6*10**9)
        self.fmcomms_interp = fmcomms_interp = 1
        self.audio_rate = audio_rate = 48000
        self.audio_interp = audio_interp = 4
        self.DAC_scale = DAC_scale = 4096

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=audio_rate*audio_interp,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=audio_rate * audio_interp,
                taps=None,
                fractional_bw=None,
        )
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source("127.0.0.1", rf_freq, samp_rate, fmcomms_interp - 1, 20000000, False, False, True, True, 0x8000, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED")
        self.iio_fmcomms2_sink_0 = iio.fmcomms2_sink("127.0.0.1", rf_freq, samp_rate, fmcomms_interp - 1, 20000000, True, True, False, False, 0x8000, False, "A", 0, 0)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, DAC_scale)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, DAC_scale)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blks2_tcp_sink_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_float*1,
        	addr=pc_host_ip,
        	port=rx_port,
        	server=False,
        )
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate*audio_interp,
        	tau=75e-6,
        	max_dev=5e3,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=audio_rate*audio_interp,
        	audio_decimation=audio_interp,
        )
        self.analog_sig_source_x_0 = analog.sig_source_f(audio_rate, analog.GR_SIN_WAVE, 10000, 5, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.analog_wfm_tx_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.blks2_tcp_sink_0, 0))    
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.iio_fmcomms2_sink_0, 1))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.iio_fmcomms2_sink_0, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.iio_fmcomms2_source_0, 0), (self.blocks_short_to_float_0, 0))    
        self.connect((self.iio_fmcomms2_source_0, 1), (self.blocks_short_to_float_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.analog_wfm_rcv_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sin_f10e3_tcp_wbfm_stream")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_pc_host_ip(self):
        return self.pc_host_ip

    def set_pc_host_ip(self, pc_host_ip):
        self.pc_host_ip = pc_host_ip

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.iio_fmcomms2_sink_0.set_params(self.rf_freq, self.samp_rate, 20000000, "A", 0, 0)
        self.iio_fmcomms2_source_0.set_params(self.rf_freq, self.samp_rate, 20000000, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED")

    def get_rx_port(self):
        return self.rx_port

    def set_rx_port(self, rx_port):
        self.rx_port = rx_port

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        self.iio_fmcomms2_sink_0.set_params(self.rf_freq, self.samp_rate, 20000000, "A", 0, 0)
        self.iio_fmcomms2_source_0.set_params(self.rf_freq, self.samp_rate, 20000000, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED")

    def get_fmcomms_interp(self):
        return self.fmcomms_interp

    def set_fmcomms_interp(self, fmcomms_interp):
        self.fmcomms_interp = fmcomms_interp

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.audio_rate)

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp

    def get_DAC_scale(self):
        return self.DAC_scale

    def set_DAC_scale(self, DAC_scale):
        self.DAC_scale = DAC_scale
        self.blocks_float_to_short_0.set_scale(self.DAC_scale)
        self.blocks_float_to_short_0_0.set_scale(self.DAC_scale)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--pc-host-ip", dest="pc_host_ip", type="string", default="192.168.0.10",
        help="Set pc_host_ip [default=%default]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = sin_f10e3_tcp_wbfm_stream(pc_host_ip=options.pc_host_ip)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
