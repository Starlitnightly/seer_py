from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QMouseEvent, QPixmap, QFont, QFontDatabase, QMovie
from PyQt5.QtCore import Qt, QLibrary, QPoint, QTime, QTimer, pyqtSignal

from ctypes import *
import numpy as np


import ui_nono
import gl
import os
import win32api
import pettip
import random


class ClickedLabel(QLabel):
    Clicked=pyqtSignal()
    #m_str=
    

    def __init__(self,m_str):
        super().__init__(m_str)
        #self.m_str=self.setText(m_str)
        


    def mouseReleaseEvent(self,event):        
        super().mouseReleaseEvent(event)
        #print('信号传递尝试')
        self.Clicked.emit()



class Nono(QMainWindow, ui_nono.Ui_Nono):
    #nono信号
    signal_fresh=pyqtSignal()
    signal_sb=pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_QuitOnClose,False)
        


        #窗体不透明
        self.setWindowOpacity(1)
        #窗体无边框，允许任务栏按钮右键菜单
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        #设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        #当前路径
        gl.currentpath=os.getcwd()
        self.tmp1=win32api.GetCurrentProcessId()
        #vipfire
        pixmap=QPixmap(gl.currentpath+"\\gif\\buff_VIP_5.png")
        self.label_2.setPixmap(pixmap)
        self.label_2.show()
        #字体
        font=QFont("Microsoft YaHei", 10, 75)
        self.label_3.setFont(font)
        fontId=QFontDatabase.addApplicationFont(gl.currentpath+"\\font\\RuiZiZhenYanTiMianFeiShangYong-2.ttf")
        print('fontId',fontId)
        nonot=QFontDatabase.applicationFontFamilies(fontId)[0]
        font1=QFont(nonot,12)
        #控件可视化
        self.label_6.setFont(font1)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label_8.setVisible(False)
        self.label_9.setVisible(False)
        self.label_10.setVisible(False)
        self.label_11.setVisible(False)
        self.label_12.setVisible(False)
        self.label_13.setVisible(False)
        self.label_14.setVisible(False)
        self.hidecap=True

        #初始化时间
        self.time=QTime()
        self.timer=QTimer()

        self.time1=QTime()
        self.timer1=QTimer()

        self.timer.timeout.connect(self.slot_timer_timeout)
        self.timer1.timeout.connect(self.slot_nono_change)

        #刷新按钮
        self.freshlabel=ClickedLabel(self)
        self.freshlabel.setGeometry(120,420,50,50)
        self.freshlabel.Clicked.connect(self.slot_Fresh)

        #识别按钮
        self.shibielabel=ClickedLabel(self)
        self.shibielabel.setGeometry(70,490,50,50)
        self.shibielabel.Clicked.connect(self.slot_shibie)



        
        #nonogif
        self.mouseMovePos=QPoint(0,0)
        self.movie=QMovie(gl.currentpath+"\\gif\\nono3.gif")
        self.movie1 =QMovie(gl.currentpath+"\\gif\\nono_1_1.gif")
        self.movie2 =QMovie(gl.currentpath+"\\gif\\nono_2_1.gif")
        self.movie3 =QMovie(gl.currentpath+"\\gif\\nono_3_1.gif")
        self.movie4 =QMovie(gl.currentpath+"\\gif\\nono_4_1.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.show()

        #cap
        self.clabel=ClickedLabel(self)
        self.clabel.setGeometry(50,0,396,345)
        self.clabel.Clicked.connect(self.slot_hidecap)

        #定时更换nono
        self.time1.restart()
        self.timer1.start(1000)

        #识别
        #self.pt=pettip.Pettip()
        #self.pt.sendmes.connect(slot_tip)
        #self.signal_pet.connect(self.pt.slot_getname)
        

    #绿火计时器每秒动作
    def slot_timer_timeout(self):
        self.firetime=1800-(self.time.elapsed()//1000)
        self.firetime_min=self.firetime//60
        self.firetime_sec=self.firetime-self.firetime_min*60
        tmp=str(self.firetime_min)+':'+str(self.firetime_sec)
        if(self.firetime<10):
            self.timer.stop()
        self.label_3.setText(tmp)

    #nono状态改变
    def slot_nono_change(self):
        t=self.time1.elapsed()//1000
        random.seed()
        k=random.randint(0,3)
        if(t%15==0):
            t2=gl.xy_memory(self.tmp1)
            if(t2>600):
                self.slot_tip("当前内存使用:"+str(t2)+"MB(内存占用较大及时刷新避免卡顿)")
            else:
                self.slot_tip("当前内存使用:"+str(t2)+"MB")
        if(t%30==0):
            if(k==0):
                self.label.setMovie(self.movie1)
                self.movie1.start()
                gl.Delay(4000)
                self.label.setMovie(self.movie)
                self.movie.start()
            elif(k==1):
                self.label.setMovie(self.movie2)
                self.movie2.start()
                gl.Delay(3000)
                self.label.setMovie(self.movie)
                self.movie.start()
            elif(k==2):
                self.label.setMovie(self.movie3)
                self.movie3.start()
                gl.Delay(3500)
                self.label.setMovie(self.movie)
                self.movie.start()
            elif(k==3):
                self.label.setMovie(self.movie4)
                self.movie4.start()
                gl.Delay(3000)
                self.label.setMovie(self.movie)
                self.movie.start() 

        if(self.underMouse()):
            self.label_7.setVisible(True)
            self.label_8.setVisible(True)
            self.label_9.setVisible(True)
            self.label_10.setVisible(True)
            self.label_11.setVisible(True)
            self.label_12.setVisible(True)
            self.label_13.setVisible(True)
            self.label_14.setVisible(True) 
        else:
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_9.setVisible(False)
            self.label_10.setVisible(False)
            self.label_11.setVisible(False)
            self.label_12.setVisible(False)
            self.label_13.setVisible(False)
            self.label_14.setVisible(False)                                      

    #nono窗口提示信息            
    def slot_tip(self,content):

        self.label_5.setVisible(True)
        self.label_6.setVisible(True)
        self.label_6.setText(content)
        print(content)
        gl.Delay(4000)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)

    #绿火计时器
    def slot_startedTimer_clicked(self):
        print('开启计时器')
        self.time.restart()
        self.timer.start(1000)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)

    #刷新按钮按下
    def slot_Fresh(self):
        #self.slot_tip('刷新成功？')
        self.signal_fresh.emit() 

    #显示对面巅峰阵容
    def slot_capture(self,tmp):
        gl.dm.Capture(564, 223, 960, 568,gl.currentpath+"\\screen.bmp")
        pixmap=QPixmap(gl.currentpath+"\\screen.bmp")
        self.label_4.setPixmap(pixmap)
        self.label_4.show()
        self.label_4.setVisible(True)
        self.hidecap=False

    #巅峰阵容截图隐藏
    def slot_hidecap(self):
        if(self.hidecap==True):
            self.hidecap=False
            self.label_4.setVisible(True)
        else:
            self.hidecap=True
            self.label_4.setVisible(False)

    #识别对战精灵
    def slot_shibie():
        return


    def mouseMoveEvent(self,event):
        if(self.mouseMovePos!=QPoint(0,0)):
            self.move(self.geometry().x()+event.globalPos().x() - self.mouseMovePos.x(), \
                self.geometry().y() + event.globalPos().y() - self.mouseMovePos.y()) 
            self.mouseMovePos=event.globalPos()

    def mousePressEvent(self,event):
        self.mouseMovePos=event.globalPos()

    def mouseReleaseEvent(self,event):
        self.mouseMovePos=QPoint(0,0)

