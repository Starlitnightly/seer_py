#全局变量
import os
from PyQt5.QtCore import QEventLoop, QTimer
import win32api
import win32process

def __init__():
    #大漠插件
    global dm
    #绑定大漠状态
    global bind_status
    #当前路径
    global currentpath
    #pid
    global pid

def Delay(time=100):
    loop=QEventLoop()
    QTimer.singleShot(time,loop.quit)
    loop.exec()

def xy_memory(pid):
    hProcess=win32api.OpenProcess(2035711,False,pid)
    pmc=win32process.GetProcessMemoryInfo(hProcess)
    if(pmc!={}):
        win32api.CloseHandle(hProcess)
        a=1024*1024
        return(pmc['WorkingSetSize']//a)
    win32api.CloseHandle(hProcess)
    return(0)

def FindPic(x1,y1,x2,y2,bmp,color,sin,code,pos):
    flag,pos['x'],pos['y']=dm.FindPic(x1,y1,x2,y2,bmp,color,sin,code)
    return flag


