# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cdkform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CdkForm(object):
    def setupUi(self, CdkForm):
        CdkForm.setObjectName("CdkForm")
        CdkForm.resize(562, 52)
        self.label = QtWidgets.QLabel(CdkForm)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.label.setStyleSheet("color:rgb(85, 0, 127)")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(CdkForm)
        self.textEdit.setGeometry(QtCore.QRect(140, 10, 231, 31))
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(CdkForm)
        self.pushButton.setGeometry(QtCore.QRect(380, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(CdkForm)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 10, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(CdkForm)
        QtCore.QMetaObject.connectSlotsByName(CdkForm)

    def retranslateUi(self, CdkForm):
        _translate = QtCore.QCoreApplication.translate
        CdkForm.setWindowTitle(_translate("CdkForm", "一键输入cdk"))
        self.label.setText(_translate("CdkForm", "cdk(神奇密码)"))
        self.pushButton.setText(_translate("CdkForm", "一键输入cdk"))
        self.pushButton_2.setText(_translate("CdkForm", "清空"))
