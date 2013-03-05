##################################################################
# ControlEee is a little application that let you turn on/off
# bluetooth, webcam and wifi on your Asus EeePC. This application
# is partially based on poweeersave written by Georg Holzmann.
#
# Version: 0.1
# Author: Andrea Grandi <a _DOT_ grandi _AT_ gmail _DOT_ com>
# License: GPL2
# Website: www.andreagrandi.it
##################################################################

import sys
from ui_controleee import Ui_ControlEeeDialog
from controleeecommands import ControlEeeCommands

try:
	from PyQt4 import QtCore, QtGui
except:
	print "You must install python-qt4 !"
	print 'Do it with "sudo apt-get install python-qt4".'
	sys.exit(1)

class ControlEee(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ControlEeeDialog()
        self.ui.setupUi(self)
        
        self.commands = ControlEeeCommands()
        self.init_status()
        
        #setup SIGNALS and SLOTS
        self.connect(self.ui.bt_checkbox, QtCore.SIGNAL("stateChanged(int)"), self.bt_checkbox_changed)
        self.connect(self.ui.cam_checkbox, QtCore.SIGNAL("stateChanged(int)"), self.cam_checkbox_changed)
        self.connect(self.ui.wifi_checkbox, QtCore.SIGNAL("stateChanged(int)"), self.wifi_checkbox_changed)
        
    def init_status(self):
        #setup initial bluetooth status
        bt_status = self.commands.bluetooth_status()
        
        if bt_status == 1:
            self.ui.bt_checkbox.setChecked(True)
        if bt_status == 0:
            self.ui.bt_checkbox.setChecked(False)
        if bt_status == -1:
            self.ui.bt_checkbox.setChecked(False)
            self.ui.bt_checkbox.setEnabled(False)
            
        #setup initial webcam status
        webcam_status = self.commands.webcam_status()
        
        if webcam_status == 1:
            self.ui.cam_checkbox.setChecked(True)
        if webcam_status == 0:
            self.ui.cam_checkbox.setChecked(False)
        if webcam_status == -1:
            self.ui.cam_checkbox.setChecked(False)
            self.ui.cam_checkbox.setEnabled(False)
            
        #setup initial wifi status
        wifi_status = self.commands.wifi_status()
        
        if wifi_status == 1:
            self.ui.wifi_checkbox.setChecked(True)
        if wifi_status == 0:
            self.ui.wifi_checkbox.setChecked(False)
        if wifi_status == -1:
            self.ui.wifi_checkbox.setChecked(False)
            self.ui.wifi_checkbox.setEnabled(False)
            
        #FIXME: workaround to avoid kernel panic. I have to disable this function at the moment.
        self.ui.wifi_checkbox.setEnabled(False)
            
    def bt_checkbox_changed(self, value):
        if value == 2:
            self.commands.bluetooth_on()
        else:
            self.commands.bluetooth_off()
    
    def cam_checkbox_changed(self, value):
        if value == 2:
            self.commands.webcam_on()
        else:
            self.commands.webcam_off()
    
    def wifi_checkbox_changed(self, value):
        if value == 2:
            self.commands.wifi_on()
        else:
            self.commands.wifi_off()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = ControlEee()
	myapp.show()
	sys.exit(app.exec_())
