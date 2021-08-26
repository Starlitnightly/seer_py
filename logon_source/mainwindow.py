# coding:utf-8

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QMouseEvent, QScreen, QGuiApplication, QDesktopServices
from PyQt5.QtCore import Qt, QProcess, QMetaType, QVariant, pyqtSignal, QJsonDocument, QUrl, QSettings
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

#必要依赖
from pycaw.pycaw import AudioUtilities
import os

#主窗口ui
import ui_mainwindow

#子窗口
import speed
import form
import cdkform
import nono
import atoken
import changesp
#全局变量
import gl
#win32函数
import win32gui
import win32api

#大漠插件注册
def AutoRegDm():
    path=os.getcwd()
    
    u="Regsvr32 "+path+"\\dm.dll"
    print(u)
    os.system(u)

    import win32com.client
    gl.dm = win32com.client.Dispatch('dm.dmsoft')  #调用大漠插件
    print(gl.dm.ver())#输出版本号




class MainWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):
    
    #信号
    sendtip=pyqtSignal(str)
    sendcap=pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        
        gl.bind_status=False
        gl.currentpath=os.getcwd()
        gl.current_version='6.0.2'




        #变速窗口
        self.s=speed.Speed()#变速窗口
        #脚本窗口
        self.f=form.Form()
        self.cd=0
        self.ato=0
        self.csp=0

        configIniWrite=QSettings(gl.currentpath+"\\set.ini",QSettings.IniFormat)
        print('agree',str(configIniWrite.value('agree')))
        if(str(configIniWrite.value('agree'))!='true'):
            if(isinstance(self.ato, atoken.Atoken)==False):
                self.ato=atoken.Atoken()
            self.ato.show()


        self.setupUi(self)
        
        #载入赛尔号游戏
        self.axWidget.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        self.axWidget.setProperty("DisplayAlerts",False)
        self.axWidget.setProperty("DisplayScrollBars",True)
        self.axWidget.dynamicCall("Navigate(const QString&)", "http://seer.61.com/play.shtml")#此处替换你的网页地址就可以，必须是服务器地址，本地服务也可以。
        
        #信号连接
        self.action.triggered.connect(self.FreshSeer)
        self.action_2.triggered.connect(self.Mute)
        self.action_3.triggered.connect(self.unMute)
        self.action_5.triggered.connect(self.speedopen)
        self.action_ie.triggered.connect(self.ClearCache)

        #脚本
        self.action_8.triggered.connect(self.script_open)
        self.action_9.triggered.connect(self.Openscript)

        #工具信号
        self.action_ce.triggered.connect(self.Opence)
        self.action_fd.triggered.connect(self.Openfd)
        self.action_cdk.triggered.connect(self.Inputcdk)
        #self.action_4.triggered.connect(self.PeakMode)
        self.action_21.triggered.connect(self.seer_cal)
        self.action_7.triggered.connect(self.slot_shiyongshuoming)
        self.action_12.triggered.connect(self.slot_xiangmuyuanma)
        self.action_20.triggered.connect(self.slot_mianzexieyi)
        self.action_22.triggered.connect(self.slot_author)

        #一键换装备信号
        '''
        self.bag_sk.triggered.connect(self.Changebag_sk)
        self.bag_fs.triggered.connect(self.Changebag_fs)
        self.bag_ld.triggered.connect(self.Changebag_ld)
        self.bag_hd.triggered.connect(self.Changebag_hd)
        self.bag_dy.triggered.connect(self.Changebag_dy)
        self.bag_xa.triggered.connect(self.Changebag_xa)
        self.bag_wl.triggered.connect(self.Changebag_wl)
        self.bag_ys.triggered.connect(self.Changebag_ys)
        self.bag_tz.triggered.connect(self.Changebag_tz)
        self.bag_yy.triggered.connect(self.Changebag_yy)
        self.bag_tq.triggered.connect(self.Changebag_tq)
        self.bag_yh.triggered.connect(self.Changebag_yh)
        '''

        #一键换精灵
        self.actionyijian.triggered.connect(self.show_csp)
        
        #nono
        self.n=nono.Nono()        
        #nono信号绑定        
        self.sendtip.connect(self.n.slot_tip)#提示信号
        self.action_13.triggered.connect(self.n.slot_startedTimer_clicked)#计时器信号        
        self.sendcap.connect(self.n.slot_capture)#截图信号
        self.action_14.triggered.connect(self.dianfeng)#巅峰阵容截图信号
        self.n.signal_fresh.connect(self.FreshSeer)#刷新游戏信号
        self.n.signal_sb.connect(self.slot_sb)#绑定dm插件信号（测试用）
        #self.signal_openskill.connect(n.showskill)
        self.n.show()#显示nono窗口

        #nono移动到左下角
        screen=QGuiApplication.primaryScreen()
        mm=screen.availableGeometry()
        screen_width = mm.width()
        screen_height = mm.height()
        self.n.move(50,screen_height-self.n.height()-50)
        self.setAttribute(Qt.WA_QuitOnClose,True)

        #检查更新
        self.nam=QNetworkAccessManager(self)
        self.nam.finished.connect(self.slot_new)
        request=QNetworkRequest()
        request.setUrl(QUrl('http://jlhsmuseum.cn/news/test.json'))
        request.setHeader(QNetworkRequest.ContentTypeHeader,"application/x-www-form-urlencoded")
        reply=self.nam.get(request)

    #检测更新
    def slot_new(self,reply):
        err=reply.error()
        if(err!=QNetworkReply.NoError):
            print('accFailed:',reply.errorString())
        else:
            str1=reply.readAll()
            parse_doucment=QJsonDocument.fromJson(str1)
            obj=parse_doucment.object()
            #print(obj)
            self.new_version=obj["newversion"].toString()
            self.new_content=obj["content"].toString()
            self.new_error=obj["error"].toString()
            self.new_time=obj["time"].toString()
            self.new_upurl=obj["upurl"].toString()
            self.new_news=obj["news"].toString()
            self.new_guanggao=obj["guanggao"].toString()
            self.new_help=obj["help"].toString()
        if(self.new_error!="667"):
            print("tip","抱歉，星小夜登录器停止使用，如果非公告停止那么请检查网络连接")
            exit()
    
        if(self.new_time!="假"):
            print("tip",self.new_news)
        if(self.new_guanggao!=" "):
            QDesktopServices.openUrl(QUrl(self.new_guanggao))
    
        if(self.new_version!=gl.current_version):
            self.sendtip.emit("发现新版本！版本号："+self.new_version)
            QDesktopServices.openUrl(QUrl(self.new_upurl))
               



    #刷新游戏
    def FreshSeer(self):
        self.axWidget.dynamicCall("Refresh(void)")
        self.sendtip.emit('刷新成功')

    #静音
    def Mute(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == "python.exe":
                volume.SetMute(1, None)
        self.sendtip.emit("小赛尔，游戏静音成功啦，如果没有成功再按一次")

    #解除静音
    def unMute(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == "python.exe":
                volume.SetMute(0, None)
        self.sendtip.emit("小赛尔，游戏成功解除静音了")


    #变速
    def speedopen(self):
        self.s.show()
        self.s.move(self.x(),self.y()+self.height())
        self.sendtip.emit("变速功能已开启，请正确合理地使用该功能哦")

    #清理ie缓存
    def ClearCache(self):   
        #self.Binddm()
        os.system(r"RunDll32.exe InetCpl.cpl ClearMyTracksByProcess 8")
        self.sendtip.emit("ie缓存清理成功，如果还是卡顿建议刷新")

    #绑定大漠
    def Binddm(self):
        #获取游戏句柄
        hq=self.winId().__int__() 
        print(hq)
        test=win32gui.GetWindow(hq,5)
        test=win32gui.GetWindow(test,2)
        test=win32gui.GetWindow(test,5)
        test=win32gui.GetWindow(test,5)
        test=win32gui.GetWindow(test,5)
        test=win32gui.GetWindow(test,5)
        test=win32gui.GetWindow(test,5)
        test=win32gui.GetWindow(test,5)
        self.pid=test
        gl.pid=test
        print(test)

        #初始化大漠
        AutoRegDm()
        
        #绑定窗口
        if(gl.dm.BindWindow(self.pid,"dx2", "windows","windows",1)==0):
            if(gl.dm.GetLastError()==-18):
                print('关于绑定失败，请在群公告内查找解决方法')
            elif(gl.dm.GetLastError()==0):
                print('错误代码：0，本错误请关闭所有杀毒软件，并用管理员模式启动')
            else:
                print('错误代码：{0}，可发送错误代码给星夜咨询错误问题'.format(gl.dm.GetLastError()))
        else:
            gl.bind_status=True

        #设置识图目录
        path=os.getcwd()+'\\pic'
        gl.dm.SetPath(path)

        #测试识图效果
        #x,y=QVariant(),QVariant()
        pos={}
        #pos['x'],pos['y']=100,0
        ss=gl.FindPic(0,0,1000,600,"test.bmp","000000",0.8,0,pos)
        print(ss,pos['x'],pos['y'])

        #设置字库
        gl.dm.SetDict(0,path+"\\ziku.txt");

        print('绑定状态',gl.bind_status)

    #打开脚本窗口
    def script_open(self):
        if(gl.bind_status==False):
            self.Binddm()
        self.f.show()

    #打开自定义脚本
    def Openscript(self):
        path=gl.currentpath+'\\工具\\自定义脚本工具.exe'
        win32api.ShellExecute(0, 'open', path, '', '', 1)
        self.sendtip.emit("自定义脚本工具加载中，发挥你的创意吧")

    #打开ce
    def Opence(self):
        path=gl.currentpath+'\\工具\\ce6.8.exe'
        win32api.ShellExecute(0, 'open', path, '', '', 1)        

    #打开fd
    def Openfd(self):
        path=gl.currentpath+'\\工具\\Fiddler\\Fiddlerh.exe'
        win32api.ShellExecute(0, 'open', path, '', '', 1)

    #打开鼠标录制工具
    def OpenKeyandMouse(self):
        path=gl.currentpath+'\\工具\\录制\\星小夜的键鼠录制工具.exe'
        win32api.ShellExecute(0, 'open', path, '', '', 1)

    #打开鼠标连点器
    def OpenMousepoint(self):
        path=gl.currentpath+'\\工具\\录制\\星小夜的键鼠录制工具.exe'
        win32api.ShellExecute(0, 'open', path, '', '', 1)

    #一键输入cdk
    def Inputcdk(self):
        if(isinstance(self.cd, cdkform.CdkForm)==False):
            self.cd=cdkform.CdkForm()
        if(gl.bind_status==False):
            self.Binddm()
        self.cd.show()

    def show_csp(self):
        if(isinstance(self.csp, changesp.Changesp)==False):
            self.csp=changesp.Changesp()
        if(gl.bind_status==False):
            self.Binddm()
        self.csp.show()

    #橙汁赛尔数值计算器
    def seer_cal(self):
        path=gl.currentpath+'\\工具\\赛尔数据计算器\\赛尔数据计算器.exe'
        win32api.ShellExecute(0, 'open', path, '', '', 1)
        self.sendtip('赛尔数值计算器正在加载中（by橙汁）')

    #使用说明
    def slot_shiyongshuoming(self):
        QDesktopServices.openUrl(QUrl(self.new_help))

    #项目源码
    def slot_xiangmuyuanma(self):
        QDesktopServices.openUrl(QUrl("https://github.com/Starlitnightly/seer_logon"))

    #免责协议
    def slot_mianzexieyi(self):
        if(isinstance(self.ato, atoken.Atoken)==False):
            self.ato=atoken.Atoken()
        self.ato.show()

    #查看作者与鸣谢信息
    def slot_author(self):
        msg='''
                作者：星夜
                联系QQ：2681686121
                -
                用户鸣谢：
                小鸽子
                潜水人员
                於城
                对本登录器的开发提出的建议与帮助
                -
        '''
        QMessageBox.about(self,'help',msg)


    #截取对面阵容函数-巅峰
    def dianfeng(self):
        if(gl.bind_status==False):
            self.Binddm()
        self.sendcap(True)
        self.sendtip('精灵阵容已截图完毕')

    #绑定大漠插件函数
    def slot_sb(self):
        if(gl.bind_status==False):
            self.Binddm()


