from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QLibrary, QSettings, QTime, QTimer

from ctypes import *
import numpy as np


import ui_atoken
import gl



class Atoken(QMainWindow, ui_atoken.Ui_Atoken):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_QuitOnClose,False)
        configIniWrite=QSettings(gl.currentpath+"\\set.ini",QSettings.IniFormat)
        #向ini文件中写入内容,setValue函数的两个参数是键值对
        self.uu=str(configIniWrite.value("agree"))
        if(str(configIniWrite.value("agree"))!="true"):
            self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(True)

        self.time=QTime()
        self.timer=QTimer()
        self.timer.timeout.connect(self.slot_timer_timeout)
        self.pushButton.clicked.connect(self.slot_agree)
        self.time.start()
        self.timer.start(1000)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.show()
    def closeEvent(self,event):
        super().closeEvent(event)
        self.show()
        print('???')
    def slot_timer_timeout(self):
        firetime=30-(self.time.elapsed()//1000)
        if(firetime<3):
            self.pushButton.setEnabled(True)
            self.setAttribute(Qt.WA_DeleteOnClose)
        elif(firetime>=3 and self.uu!="true"):
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
        self.label.setText('等待'+str(firetime)+'s后才能确认')
    def slot_agree(self):
        self.hide()
        configIniWrite=QSettings(gl.currentpath+"\\set.ini",QSettings.IniFormat)
        configIniWrite.setValue('agree','true')


