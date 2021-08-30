from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QLibrary

from ctypes import *
import numpy as np


import ui_speed



class Speed(QMainWindow, ui_speed.Ui_Speed):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #载入变速dll
        self.lib=CDLL(r"SpeedControl.dll")
        self.setAttribute(Qt.WA_QuitOnClose,False)
        #让变速按钮跟变速条具有变速的能力
        self.pushButton.clicked.connect(self.Changespeed)
        self.speedslider.valueChanged.connect(self.sliderspeed)
        
    def Changespeed(self):
        #获取变速值
        text=self.speedtext.toPlainText()
        #设置变速值
        self.lib.SetRange(c_float(float(text)))

    def sliderspeed(self):
        #获取变速条的位置
        a=self.speedslider.sliderPosition()
        sp=pow(2,a)
        #设置变速值
        self.lib.SetRange(c_float(float(sp)))