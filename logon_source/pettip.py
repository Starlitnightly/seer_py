from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QLibrary

from ctypes import *
import numpy as np


import ui_pettip



class Pettip(QMainWindow, ui_pettip.Ui_Pettip):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_QuitOnClose,False)
        #self.m_manager=

   # def slot_