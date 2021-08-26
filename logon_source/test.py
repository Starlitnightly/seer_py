import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtGui import QIcon, QPixmap

import mainwindow


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=mainwindow.MainWindow()
    icon=QIcon()
    icon.addPixmap(QPixmap('favicon.ico'),QIcon.Normal, QIcon.Off)
    win.setWindowIcon(icon)
    win.show()
    app.exit(app.exec_())
