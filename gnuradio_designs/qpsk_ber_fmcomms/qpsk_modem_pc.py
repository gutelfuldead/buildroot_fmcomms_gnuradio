#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: qpsk_modem_pc
# Generated: Fri Nov 10 14:06:17 2017
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import sip
import sys
from gnuradio import qtgui


class qpsk_modem_pc(gr.top_block, Qt.QWidget):

    def __init__(self, pc_host_ip='10.0.1.245'):
        gr.top_block.__init__(self, "qpsk_modem_pc")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("qpsk_modem_pc")
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

        self.settings = Qt.QSettings("GNU Radio", "qpsk_modem_pc")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.pc_host_ip = pc_host_ip

        ##################################################
        # Variables
        ##################################################
        self.const_type = const_type = 1
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = {0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[const_type] + " - Change const_type for different constellation types!"
        self.samp_rate = samp_rate = 100e3
        self.output_bits_port = output_bits_port = 12347
        self.modulated_data_tx_port = modulated_data_tx_port = 12348
        self.modulated_data_rx_port = modulated_data_rx_port = 12349
        self.input_bits_port = input_bits_port = 12346

        ##################################################
        # Blocks
        ##################################################
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
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"TX Modulated Data", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['"Constellation: "+str(const[const_type].arity()) + "-PSK"', '', '', '', '',
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
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 2,0,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"RX Modulated Data", #name
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

        labels = ['"Constellation: "+str(const[const_type].arity()) + "-PSK"', '', '', '', '',
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
        self.blks2_tcp_source_0_1_1 = grc_blks2.tcp_source(
        	itemsize=gr.sizeof_char*1,
        	addr=pc_host_ip,
        	port=input_bits_port,
        	server=True,
        )
        self.blks2_tcp_source_0_1 = grc_blks2.tcp_source(
        	itemsize=gr.sizeof_char*1,
        	addr=pc_host_ip,
        	port=output_bits_port,
        	server=True,
        )
        self.blks2_tcp_source_0_0 = grc_blks2.tcp_source(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr=pc_host_ip,
        	port=modulated_data_rx_port,
        	server=True,
        )
        self.blks2_tcp_source_0 = grc_blks2.tcp_source(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr=pc_host_ip,
        	port=modulated_data_rx_port,
        	server=True,
        )
        self.blks2_error_rate = grc_blks2.error_rate(
        	type='BER',
        	win_size=int(1e7),
        	bits_per_symbol=2,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_error_rate, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blks2_tcp_source_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blks2_tcp_source_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.blks2_tcp_source_0_1, 0), (self.blks2_error_rate, 1))
        self.connect((self.blks2_tcp_source_0_1_1, 0), (self.blks2_error_rate, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "qpsk_modem_pc")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_pc_host_ip(self):
        return self.pc_host_ip

    def set_pc_host_ip(self, pc_host_ip):
        self.pc_host_ip = pc_host_ip

    def get_const_type(self):
        return self.const_type

    def set_const_type(self, const_type):
        self.const_type = const_type
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter({0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[self.const_type] + " - Change const_type for different constellation types!"))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

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


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--pc-host-ip", dest="pc_host_ip", type="string", default='10.0.1.245',
        help="Set pc_host_ip [default=%default]")
    return parser


def main(top_block_cls=qpsk_modem_pc, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(pc_host_ip=options.pc_host_ip)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
