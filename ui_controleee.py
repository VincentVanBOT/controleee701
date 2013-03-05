# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_controleee.ui'
#
# Created: Wed Oct  1 14:17:12 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ControlEeeDialog(object):
    def setupUi(self, ControlEeeDialog):
        ControlEeeDialog.setObjectName("ControlEeeDialog")
        ControlEeeDialog.setWindowModality(QtCore.Qt.NonModal)
        ControlEeeDialog.resize(QtCore.QSize(QtCore.QRect(0,0,287,104).size()).expandedTo(ControlEeeDialog.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ControlEeeDialog.sizePolicy().hasHeightForWidth())
        ControlEeeDialog.setSizePolicy(sizePolicy)
        ControlEeeDialog.setMinimumSize(QtCore.QSize(287,104))
        ControlEeeDialog.setMaximumSize(QtCore.QSize(287,104))
        #ControlEeeDialog.setModal(False)

        self.bt_label = QtGui.QLabel(ControlEeeDialog)
        self.bt_label.setGeometry(QtCore.QRect(20,10,51,51))
        self.bt_label.setPixmap(QtGui.QPixmap("icons/bluetooth.svg"))
        self.bt_label.setObjectName("bt_label")

        self.bt_checkbox = QtGui.QCheckBox(ControlEeeDialog)
        self.bt_checkbox.setGeometry(QtCore.QRect(10,70,79,24))
        self.bt_checkbox.setObjectName("bt_checkbox")

        self.cam_label = QtGui.QLabel(ControlEeeDialog)
        self.cam_label.setGeometry(QtCore.QRect(120,10,54,48))
        self.cam_label.setPixmap(QtGui.QPixmap("icons/camera-web.svg"))
        self.cam_label.setObjectName("cam_label")

        self.cam_checkbox = QtGui.QCheckBox(ControlEeeDialog)
        self.cam_checkbox.setGeometry(QtCore.QRect(100,70,79,24))
        self.cam_checkbox.setObjectName("cam_checkbox")

        self.wifi_label = QtGui.QLabel(ControlEeeDialog)
        self.wifi_label.setGeometry(QtCore.QRect(220,10,54,48))
        self.wifi_label.setPixmap(QtGui.QPixmap("icons/network-wireless.svg"))
        self.wifi_label.setObjectName("wifi_label")

        self.wifi_checkbox = QtGui.QCheckBox(ControlEeeDialog)
        self.wifi_checkbox.setGeometry(QtCore.QRect(210,70,61,24))
        self.wifi_checkbox.setObjectName("wifi_checkbox")

        self.retranslateUi(ControlEeeDialog)
        QtCore.QMetaObject.connectSlotsByName(ControlEeeDialog)

    def retranslateUi(self, ControlEeeDialog):
        ControlEeeDialog.setWindowTitle(QtGui.QApplication.translate("ControlEeeDialog", "ControlEee", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_checkbox.setText(QtGui.QApplication.translate("ControlEeeDialog", "Bluetooth", None, QtGui.QApplication.UnicodeUTF8))
        self.cam_checkbox.setText(QtGui.QApplication.translate("ControlEeeDialog", "Webcam", None, QtGui.QApplication.UnicodeUTF8))
        self.wifi_checkbox.setText(QtGui.QApplication.translate("ControlEeeDialog", "Wifi", None, QtGui.QApplication.UnicodeUTF8))

