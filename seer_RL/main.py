import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtGui import QIcon, QPixmap

import bat1


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=bat1.mainwindow()
    win.win.show()
    app.exit(app.exec_())
