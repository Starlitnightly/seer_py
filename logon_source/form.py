from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QLibrary

from ctypes import *
import numpy as np


import ui_form



class Form(QMainWindow, ui_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)