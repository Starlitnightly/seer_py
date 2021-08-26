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
        self.lib=CDLL(r"SpeedControl.dll")
        self.setAttribute(Qt.WA_QuitOnClose,False)
        self.pushButton.clicked.connect(self.Changespeed)
        self.speedslider.valueChanged.connect(self.sliderspeed)
        '''
        lib=QLibrary(r"SpeedControl.dll")
        void = typedef(MyPrototype)(float a)
        u = (MyPrototype) lib.resolve("SetRange")
        if(lib.load()):
            if(u==0):
                print('failed')
            else:
                u(256.0)

        else:
            print('failed')
        '''


    def Changespeed(self):
        text=self.speedtext.toPlainText()
        self.lib.SetRange(c_float(float(text)))

    def sliderspeed(self):
        a=self.speedslider.sliderPosition()
        sp=pow(2,a)
        self.lib.SetRange(c_float(float(sp)))