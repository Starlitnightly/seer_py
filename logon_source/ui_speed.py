# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speed.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Speed(object):
    def setupUi(self, Speed):
        Speed.setObjectName("Speed")
        Speed.resize(679, 50)
        self.speedslider = QtWidgets.QSlider(Speed)
        self.speedslider.setGeometry(QtCore.QRect(0, 0, 501, 31))
        self.speedslider.setMinimumSize(QtCore.QSize(461, 0))
        self.speedslider.setMinimum(-7)
        self.speedslider.setMaximum(7)
        self.speedslider.setPageStep(1)
        self.speedslider.setOrientation(QtCore.Qt.Horizontal)
        self.speedslider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.speedslider.setTickInterval(1)
        self.speedslider.setObjectName("speedslider")
        self.speedtext = QtWidgets.QTextEdit(Speed)
        self.speedtext.setGeometry(QtCore.QRect(510, 10, 61, 31))
        self.speedtext.setUndoRedoEnabled(True)
        self.speedtext.setLineWrapMode(QtWidgets.QTextEdit.FixedColumnWidth)
        self.speedtext.setObjectName("speedtext")
        self.pushButton = QtWidgets.QPushButton(Speed)
        self.pushButton.setGeometry(QtCore.QRect(580, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Speed)
        self.label.setGeometry(QtCore.QRect(0, 30, 521, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Speed)
        QtCore.QMetaObject.connectSlotsByName(Speed)

    def retranslateUi(self, Speed):
        _translate = QtCore.QCoreApplication.translate
        Speed.setWindowTitle(_translate("Speed", "游戏变速"))
        self.pushButton.setText(_translate("Speed", "自定义变速"))
        self.label.setText(_translate("Speed", "-128  -64  -32  -16    -8   -4    -2     1     2     4    8     16    32    64   128"))