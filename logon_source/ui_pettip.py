# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pettip.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pettip(object):
    def setupUi(self, Pettip):
        Pettip.setObjectName("Pettip")
        Pettip.resize(590, 489)
        self.tableWidget = QtWidgets.QTableWidget(Pettip)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 591, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.textEdit = QtWidgets.QTextEdit(Pettip)
        self.textEdit.setGeometry(QtCore.QRect(90, 450, 81, 31))
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Pettip)
        self.pushButton.setGeometry(QtCore.QRect(180, 450, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Pettip)
        self.label.setGeometry(QtCore.QRect(30, 450, 51, 31))
        self.label.setStyleSheet("color:rgb(85, 0, 127)")
        self.label.setObjectName("label")

        self.retranslateUi(Pettip)
        QtCore.QMetaObject.connectSlotsByName(Pettip)

    def retranslateUi(self, Pettip):
        _translate = QtCore.QCoreApplication.translate
        Pettip.setWindowTitle(_translate("Pettip", "精灵技能快查"))
        self.pushButton.setText(_translate("Pettip", "查询"))
        self.label.setText(_translate("Pettip", "精灵名称"))