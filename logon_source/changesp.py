from PyQt5.QtWidgets import QMainWindow, QDirModel, QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QLibrary, QTextStream,QIODevice, QFile, QThread

from ctypes import *
import numpy as np


import ui_changesp
import win32api
import gl

def change_init(tmp):
    tmp.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")

def deletesp(tmp):
    tmp.setControl("{d27cdb6e-ae6d-11cf-96b8-444553540000}")

def change_sp(tmp,url):
    deletesp(tmp)
    tmp.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
    tmp.dynamicCall("Navigate(QString)",url)

class ffAutoC(QThread):
    status=False
    def __init__(self):
        super().__init__()
        self.status=False
    def run(self):
        pos={}
        while(self.status==True):
            if(gl.FindPic(406, 322, 562, 402,"放入背包确认.bmp","000000",0.8,0,pos)!=-1):
                gl.dm.MoveTo(pos['x'],pos['y'])
                gl.dm.LeftClick()
            if(gl.FindPic(400, 200, 600, 300, "数据非法.bmp","000000",0.8,0,pos)!=-1):
                gl.dm.MoveTo(pos['x'],pos['y'])
                gl.dm.LeftClick()
            if(gl.FindPic(0,0,1000,600,"消息盒子x.bmp","000000",0.8,0,pos)!=-1):
                gl.dm.MoveTo(pos['x'],pos['y'])
                gl.dm.LeftClick()    
            gl.Delay(1000)
            


class Changesp(QMainWindow, ui_changesp.Ui_Changesp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_QuitOnClose,False)
        self.bag=[]

        self.sp=[]
        self.sp.append(self.axWidget)
        self.sp.append(self.axWidget_2)
        self.sp.append(self.axWidget_3)
        self.sp.append(self.axWidget_4)
        self.sp.append(self.axWidget_5)
        self.sp.append(self.axWidget_6)
        self.sp.append(self.axWidget_7)
        self.sp.append(self.axWidget_8)
        self.sp.append(self.axWidget_9)
        self.sp.append(self.axWidget_10)
        self.sp.append(self.axWidget_11)
        self.sp.append(self.axWidget_12)
        for i in range(12):
            change_init(self.sp[i])

        self.model=QDirModel()
        self.treeView.setModel(self.model)
        self.path=gl.currentpath+"\\seer背包"
        self.treeView.setRootIndex(self.model.index(self.path))

        self.treeView.pressed.connect(self.slot_treeView_pressed)
        self.pushButton_3.clicked.connect(self.slot_pre_bag)
        self.pushButton.clicked.connect(self.slot_savebag)
        self.pushButton_2.clicked.connect(self.slot_auto_bag)


    def slot_pre_bag(self):
        tmp=self.textEdit.toPlainText()
        sections=tmp.split('|')
        for i in range(12):
            deletesp(self.sp[i])
        for i in range(len(sections)):
            print(sections[i])
            webstr="http://seer.61.com/resource/pet/head/"+sections[i]+".swf"
            self.bag.append(sections[i])
            change_sp(self.sp[i],webstr)
            self.bag.append(sections[i])

    def slot_savebag(self):
        saveDialog=QFileDialog()
        saveDialog.setAcceptMode(QFileDialog.AcceptSave)
        saveDialog.setWindowTitle("0.0")
        saveDialog.setDirectory(self.path)
        saveDialog.selectFile("1")
        saveDialog.setNameFilter("*.txt")
        saveDialog.selectNameFilter("*.txt")

        if(saveDialog.exec() == QFileDialog.AcceptSave):
            saveFile = saveDialog.selectedFiles()[0]
            savePath = saveDialog.directory().path()
            filter = saveDialog.selectedNameFilter()
            file=QFile(saveFile)
            if(file.open(QIODevice.WriteOnly | QIODevice.Text | QIODevice.Append)==0):
                QMessageBox.warning(self,"sdf","can't open",QMessageBox.Yes)
            stream=QTextStream(file)
            stream<<self.textEdit.toPlainText()
            file.close()
        self.model=QDirModel()
        self.treeView.setModel(self.model)
        self.path=gl.currentpath+"\\seer背包"
        self.treeView.setRootIndex(self.model.index(self.path))

    def slot_treeView_pressed(self,modeIndex):
        self.treeView.resizeColumnToContents(modeIndex.row())
        selectedRowTxt = self.treeView.model().itemData(modeIndex)
        print(selectedRowTxt)
        file=QFile(self.path+"\\"+selectedRowTxt[0])
        file.open(QIODevice.ReadOnly | QIODevice.Text)
        value=str(file.readAll(),encoding='utf-8')
        self.textEdit.setText(value)

    def Putsp_home(self):
        pos={}
        while(gl.FindPic(0,0,1000,600,"黑色入库.bmp","000000",0.8,0,pos)==-1):
            gl.dm.MoveTo(633,268)
            gl.dm.LeftClick()
            if(gl.FindPic(0,0,1000,600,"识别仓库.bmp|识别仓库2.bmp","000000",0.8,0,pos)!=-1):
                break
            QApplication.processEvents()
            gl.Delay(500)

    def Opensp_home(self):
        pos={}
        while(gl.FindPic(0,0,1000,600,"识别仓库.bmp|识别仓库2.bmp","000000",0.8,0,pos)==-1):
            gl.dm.MoveTo(849,470)
            gl.dm.LeftClick()
            QApplication.processEvents()
            gl.Delay(500)


    def Searchsp(self,pid,name):
        pos={}
        gl.dm.MoveTo(901,103)
        gl.dm.LeftDown()
        gl.dm.MoveTo(839,103)
        for i in [ord(c) for c in name]:
            win32api.PostMessage(pid, 258, i, 0)
        gl.dm.LeftUp()
        while(gl.FindPic(620, 115, 794, 186, "搜索结果.bmp","000000",0.8,0,pos)==-1):
            gl.dm.MoveTo(925,108)
            gl.dm.LeftClick()
            gl.Delay(100)
            QApplication.processEvents()

    def Putsp_bag(self):
        for i in range(5):
            gl.dm.MoveTo(216,489)
            gl.dm.LeftClick()
            gl.Delay(100)
            
        for i in range(5):
            gl.dm.MoveTo(925,137)
            gl.dm.LeftClick()
            gl.Delay(100)

    def slot_auto_bag(self):
        gl.Delay(100)
        tmp=ffAutoC()
        tmp.status=True
        tmp.start()
        self.Putsp_home()
        self.Opensp_home()
        tmpl=self.textEdit.toPlainText()
        sections=tmpl.split('|')
        self.bag=[]
        for i in range(len(sections)):
            self.bag.append(sections[i])
            QApplication.processEvents()
        for i in range(len(self.bag)):
            self.Searchsp(gl.pid,self.bag[i])
            QApplication.processEvents()
            self.Putsp_bag()
            QApplication.processEvents()
            gl.Delay(200)
        tmp.status=False
        QApplication.processEvents()
        tmp=0
        print('success bag')
        #gl.dm.MoveTo(515,150)
        #gl.dm.LeftDown()
        #gl.dm.MoveTo(520,150)
        #for i in [ord(c) for c in 'name']:
        #    win32api.PostMessage(gl.pid, 258, i, 0)