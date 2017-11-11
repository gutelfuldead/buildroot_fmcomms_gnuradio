#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BER Simulation
# Author: Example
# Description: Adjust the noise and constellation... see what happens!
# Generated: Fri Nov 10 15:14:00 2017
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
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import numpy
import sip
import sys
from gnuradio import qtgui


class ber_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BER Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BER Simulation")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.system_samp_rate = system_samp_rate = 131072
        self.const_type = const_type = 1
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = {0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[const_type] + " - Change const_type for different constellation types!"
        self.sample_size = sample_size = int(10e6)
        self.data_rate = data_rate = system_samp_rate/16
        self.const = const = (digital.constellation_bpsk(), digital.constellation_qpsk(), digital.constellation_8psk())
        self.EbN0 = EbN0 = 10

        ##################################################
        # Blocks
        ##################################################
        self._EbN0_range = Range(-10, 200, 1, 10, 200)
        self._EbN0_win = RangeWidget(self._EbN0_range, self.set_EbN0, 'Eb / N0 (dB)', "counter_slider", float)
        self.top_layout.addWidget(self._EbN0_win)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Constellation Type'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)

        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['x10^-6', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1e6, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 1,0,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"foo", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ["Constellation: "+str(const[const_type].arity()) + "-PSK", '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.6, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 2,0,1,1)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(const[const_type].base())
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const[1].points()), 1)
        self.blocks_sample_and_hold_xx_0 = blocks.sample_and_hold_bb()
        self.blocks_peak_detector2_fb_0 = blocks.peak_detector2_fb(7, 1000, 0.001)
        self.blocks_add_xx = blocks.add_vcc(1)
        self.blks2_error_rate = grc_blks2.error_rate(
        	type='BER',
        	win_size=sample_size,
        	bits_per_symbol=const[const_type].bits_per_symbol(),
        )
        self.analog_sig_source_x_0 = analog.sig_source_f(system_samp_rate, analog.GR_COS_WAVE, data_rate, 1, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 4, sample_size)), True)
        self.analog_noise_source_x = analog.noise_source_c(analog.GR_GAUSSIAN, 1.0 / math.sqrt(2.0 * const[const_type].bits_per_symbol() * 10**(EbN0/10)), 42)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x, 0), (self.blocks_add_xx, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_sample_and_hold_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_peak_detector2_fb_0, 0))
        self.connect((self.blks2_error_rate, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_add_xx, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_add_xx, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_peak_detector2_fb_0, 0), (self.blocks_sample_and_hold_xx_0, 1))
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.blks2_error_rate, 0))
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.blocks_add_xx, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_error_rate, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_system_samp_rate(self):
        return self.system_samp_rate

    def set_system_samp_rate(self, system_samp_rate):
        self.system_samp_rate = system_samp_rate
        self.set_data_rate(self.system_samp_rate/16)
        self.analog_sig_source_x_0.set_sampling_freq(self.system_samp_rate)

    def get_const_type(self):
        return self.const_type

    def set_const_type(self, const_type):
        self.const_type = const_type
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter({0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[self.const_type] + " - Change const_type for different constellation types!"))
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(2.0 * self.const[self.const_type].bits_per_symbol() * 10**(self.EbN0/10)))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_sample_size(self):
        return self.sample_size

    def set_sample_size(self, sample_size):
        self.sample_size = sample_size

    def get_data_rate(self):
        return self.data_rate

    def set_data_rate(self, data_rate):
        self.data_rate = data_rate
        self.analog_sig_source_x_0.set_frequency(self.data_rate)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const[1].points()))
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(2.0 * self.const[self.const_type].bits_per_symbol() * 10**(self.EbN0/10)))

    def get_EbN0(self):
        return self.EbN0

    def set_EbN0(self, EbN0):
        self.EbN0 = EbN0
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(2.0 * self.const[self.const_type].bits_per_symbol() * 10**(self.EbN0/10)))


def main(top_block_cls=ber_simulation, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
