from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QLibrary

from ctypes import *
import numpy as np


import ui_bat1
import damage
import random
import spirit

import threading



class mainwindow():
    def __init__(self):
        self.initui()
    def initui(self):
        self.win = QWidget()
        self.win.resize(250, 100)
        self.win.move(600, 400)
        self.win.setWindowTitle('对战信息')
        self.monster1=spirit.鲁斯王
        self.monster2=spirit.魔焰猩猩
        self.info=''

        self.layout=QGridLayout(self.win)
        self.label=QLabel('对战状态提示')
        self.layout.addWidget(self.label)
        self.button=QPushButton()
        self.layout.addWidget(self.button)
        self.button_2=QPushButton()
        self.layout.addWidget(self.button_2)
        self.win.setLayout(self.layout)

        self.com=damage.Seer_combat(self.monster1,self.monster2)

        self.bat1=Bat1(self.monster1,1,self.com)
        self.bat1.show()
        self.bat1.move(200,50)
        self.bat2=Bat1(self.monster2,2,self.com)
        self.bat2.show()
        self.bat2.move(800,50)

        self.button.clicked.connect(self.a)
        self.button_2.clicked.connect(self.off)


    def a(self):
        t = threading.Thread(target=self.on, name='t')
        t.start()

    def Isdie(self):
        if(self.monster1['基础']['life']<=0 or self.monster2['基础']['life']<=0):
            if(self.monster1['基础']['life']<=0):
                self.info=self.info+'游戏结束,'+self.monster1['基础']['name']+'已阵亡\n'
                self.label.setText(self.info)
                self.monster1['基础']['life']=0
                return True
            else:
                self.info=self.info+'游戏结束,'+self.monster2['基础']['name']+'已阵亡\n'
                self.label.setText(self.info)
                self.monster2['基础']['life']=0
                return True
        else:
            return False

    def Fresh_info(self,info1,info2):
        self.info=self.info+info1+info2
        self.label.setText(self.info)
        self.bat1.fresh(self.monster1)
        self.bat2.fresh(self.monster2)

    def round_effect(self,round_name,monster):#回合类效果：致命几率
        if(round_name=='致命几率' and monster['回合类标记'][round_name]['Isopen']==True):
            if(monster['回合类标记'][round_name]['round']!=0):
                monster['基础']['heart']+=(monster['回合类标记'][round_name]['content'])
                monster['回合类标记'][round_name]['round']-=1
            else:
                monster['基础']['heart']=monster['基础']['heart_normal']

        if(round_name=='叠加伤害' and monster['回合类标记'][round_name]['Isopen']==True):
            for i in monster['技能'].values():
                if(i['s_name']==monster['回合类标记'][round_name]['skill']):
                    if(monster['回合类标记'][round_name]['round']!=0):
                        i['s_damage']+=monster['回合类标记'][round_name]['content']
                        monster['回合类标记'][round_name]['round']-=1
                    else:
                        i['s_damage']=i['s_damage_raw']

    def on(self):
        self.flag = 1
        print("线程开启")
        self.info='round:1\n'
        self.label.setText(self.info)
        self.round=1
        self.nowround=1

        self.monster1['基础']['life'],self.monster2['基础']['life']=self.monster1['基础']['life_max'],self.monster2['基础']['life_max']
        for i in self.monster1['强化等级'].keys():
            self.monster1['强化等级'][i],self.monster2['强化等级'][i]=0,0
        self.bat1.skill_isuse,self.bat2.skill_isuse=False,False

        for i in self.monster1['技能'].keys():
            self.monster1['技能'][i]['s_damage']=self.monster1['技能'][i]['s_damage_raw']
            self.monster1['技能'][i]['s_pp']=self.monster1['技能'][i]['s_pp_max']
        self.bat1.fresh(self.monster1)
        self.bat2.fresh(self.monster2)


        while True:
            if self.flag == 1:
                #self.bat1.fresh(self.monster1)
                #self.bat2.fresh(self.monster2)

                if(self.round!=self.nowround):
                    #回合开始
                    self.info=self.info+'round:{0}\n'.format(self.nowround)
                    self.label.setText(self.info)
                    #依次结算回合类效果，速度快的优先
                    if(self.monster1['基础']['speed']>self.monster2['基础']['speed']):
                        for i in self.monster1['回合类标记'].keys():
                            if(i=='致命几率'):
                                self.round_effect('致命几率',self.monster1)
                            elif(i=='叠加伤害'):
                                self.round_effect('叠加伤害',self.monster1)
                        for i in self.monster2['回合类标记'].keys():
                            if(i=='致命几率'):
                                self.round_effect('致命几率',self.monster2)
                            elif(i=='叠加伤害'):
                                self.round_effect('叠加伤害',self.monster2)
                    elif(self.monster1['基础']['speed']<self.monster2['基础']['speed']):
                        for i in self.monster2['回合类标记'].keys():
                            if(i=='致命几率'):
                                self.round_effect('致命几率',self.monster2)
                            elif(i=='叠加伤害'):
                                self.round_effect('叠加伤害',self.monster2)
                        for i in self.monster1['回合类标记'].keys():
                            if(i=='致命几率'):
                                self.round_effect('致命几率',self.monster1)
                            elif(i=='叠加伤害'):
                                self.round_effect('叠加伤害',self.monster1)
                    else:
                        ra=random.ranint(0,1)
                        if(ra==0):
                            for i in self.monster1['回合类标记'].keys():
                                if(i=='致命几率'):
                                    self.round_effect('致命几率',self.monster1)
                                elif(i=='叠加伤害'):
                                    self.round_effect('叠加伤害',self.monster1)
                            for i in self.monster2['回合类标记'].keys():
                                if(i=='致命几率'):
                                    self.round_effect('致命几率',self.monster2)
                                elif(i=='叠加伤害'):
                                    self.round_effect('叠加伤害',self.monster2)
                        else:
                            for i in self.monster2['回合类标记'].keys():
                                if(i=='致命几率'):
                                    self.round_effect('致命几率',self.monster2)
                                elif(i=='叠加伤害'):
                                    self.round_effect('叠加伤害',self.monster2)
                            for i in self.monster1['回合类标记'].keys():
                                if(i=='致命几率'):
                                    self.round_effect('致命几率',self.monster1)
                                elif(i=='叠加伤害'):
                                    self.round_effect('叠加伤害',self.monster1)
                    self.bat1.fresh(self.monster1)
                    self.bat2.fresh(self.monster2)

                    self.round+=1                
                

                if(self.bat1.skill_isuse==True and self.bat2.skill_isuse==True):
                    print('双方都释放技能了')
                    info1,info2='',''
                    skill1,skill2='skill_{}'.format(self.bat1.skill_num),'skill_{}'.format(self.bat2.skill_num)
                    #判断出手顺序
                    if(self.monster1['技能'][skill1]['s_early']>self.monster2['技能'][skill2]['s_early']):
                        #精灵1技能先制大于精灵2
                        info1=self.com.monster_skill(skill1,1)
                        if(self.Isdie()):
                            self.Fresh_info(info1,info2)
                            break
                        info2=self.com.monster_skill(skill2,2)
                        if(self.Isdie()):
                            self.Fresh_info(info1,info2)
                            break
                    elif(self.monster1['技能'][skill1]['s_early']<self.monster2['技能'][skill2]['s_early']):
                        #精灵2技能先制大于精灵1
                        info1=self.com.monster_skill(skill2,2)
                        if(self.Isdie()):
                            self.Fresh_info(info1,info2)
                            break
                        info2=self.com.monster_skill(skill1,1)
                        if(self.Isdie()):
                            self.Fresh_info(info1,info2)
                            break
                    else:
                        #速度判断谁先出手
                        if(self.monster1['基础']['speed']>self.monster2['基础']['speed']):
                            info1=self.com.monster_skill(skill1,1)
                            if(self.Isdie()):
                                self.Fresh_info(info1,info2)
                                break
                            info2=self.com.monster_skill(skill2,2)
                            if(self.Isdie()):
                                self.Fresh_info(info1,info2)
                                break
                        elif(self.monster1['基础']['speed']<self.monster2['基础']['speed']):
                            info1=self.com.monster_skill(skill2,2)
                            if(self.Isdie()):
                                self.Fresh_info(info1,info2)
                                break
                            info2=self.com.monster_skill(skill1,1)
                            if(self.Isdie()):
                                self.Fresh_info(info1,info2)
                                break
                        else:
                            #如果速度相同
                            ra=random.ranint(0,1)
                            if(ra==0):
                                info1=self.com.monster_skill(skill1,1)
                                if(self.Isdie()):
                                    self.info=self.info+info1+info2
                                    self.label.setText(self.info)
                                    break
                                info2=self.com.monster_skill(skill2,2)
                                if(self.Isdie()):
                                    self.info=self.info+info1+info2
                                    self.label.setText(self.info)
                                    break
                            else:
                                info1=self.com.monster_skill(skill2,2)
                                if(self.Isdie()):
                                    self.info=self.info+info1+info2
                                    self.label.setText(self.info)
                                    break
                                info2=self.com.monster_skill(skill1,1)
                                if(self.Isdie()):
                                    self.info=self.info+info1+info2
                                    self.label.setText(self.info)
                                    break
                    
                    self.info=self.info+info1+info2
                    self.label.setText(self.info)
                    self.bat1.fresh(self.monster1)
                    self.bat2.fresh(self.monster2)
                    #回合结束
                    self.nowround+=1
                    self.bat1.skill_isuse,self.bat2.skill_isuse=False,False

            else:
                break
        print("暂停成功！")


    def off(self):
        self.flag = 0
        print('22222')    

            



class Bat1(QMainWindow, ui_bat1.Ui_MainWindow):
    def __init__(self,monster,num,com):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_QuitOnClose,False)
        #print(monster)
        self.com=com
        self.num=num
        self.info=''
        self.monster=monster

        self.pushButton.clicked.connect(self.skill1_use)
        self.pushButton_2.clicked.connect(self.skill2_use)
        self.pushButton_3.clicked.connect(self.skill3_use)
        self.pushButton_4.clicked.connect(self.skill4_use)

        self.pushButton_5.clicked.connect(self.hp)
        self.pushButton_6.clicked.connect(self.pp)
        self.skill_isuse=False
        self.axWidget.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        self.axWidget.dynamicCall("Navigate(QString)","http://seer.61.com/resource/pet/head/3889.swf")
        self.fresh(monster)
        

    def fresh(self,monster):

        skill=self.monster['技能']
        self.pushButton.setText(skill['skill_1']['s_name']+'\n{0}/{1}'.format(skill['skill_1']['s_pp'],skill['skill_1']['s_pp_max']))
        self.pushButton_2.setText(skill['skill_2']['s_name']+'\n{0}/{1}'.format(skill['skill_2']['s_pp'],skill['skill_2']['s_pp_max']))
        self.pushButton_3.setText(skill['skill_3']['s_name']+'\n{0}/{1}'.format(skill['skill_3']['s_pp'],skill['skill_3']['s_pp_max']))
        self.pushButton_4.setText(skill['skill_4']['s_name']+'\n{0}/{1}'.format(skill['skill_4']['s_pp'],skill['skill_4']['s_pp_max']))

        level=self.monster['强化等级']
        self.label_2.setText('命中:{0} 攻击:{1} 防御:{2} 特攻:{3} 特防:{4} 速度:{5}'.format(level['r_hit'],level['r_ap'],level['r_dp'],level['r_as'],level['r_ds'],level['r_s']))

        if(self.monster['基础']['life']>self.monster['基础']['life_max']):
            self.monster['基础']['life']=self.monster['基础']['life_max']
        life='体力:{0}/{1}'.format(self.monster['基础']['life'],self.monster['基础']['life_max'])
        self.monster['基础']['now_life']=self.monster['基础']['life']

        self.label_3.setText(life)
        

    def skill1_use(self):
        #if(self.oppo_skill_isuse!=False):
            self.skill_num=1
            #self.info=self.com.monster_skill('skill_1',self.num)
            self.skill_isuse=True

    def skill2_use(self):
        #if(self.oppo_skill_isuse==False):
            self.skill_num=2
            #self.info=self.com.monster_skill('skill_2',self.num)
            self.skill_isuse=True

    def skill3_use(self):
        #if(self.oppo_skill_isuse==False):
            self.skill_num=3
            #self.info=self.com.monster_skill('skill_3',self.num)
            self.skill_isuse=True

    def skill4_use(self):
        #if(self.oppo_skill_isuse==False):
            self.skill_num=4
            #self.info=self.com.monster_skill('skill_4',self.num)
            self.skill_isuse=True

    def hp(self):
        
        #self.monster['基础']['life']=self.monster['基础']['life_max']
        #self.info=self.monster['基础']['name']+'使用了回复药水\n'
        self.skill_num='hp'
        self.skill_isuse=True
    def pp(self):
        
        #self.monster['技能']['skill_1']['s_pp']=self.monster['技能']['skill_1']['s_pp_max']
        #self.monster['技能']['skill_2']['s_pp']=self.monster['技能']['skill_2']['s_pp_max']
        #self.monster['技能']['skill_3']['s_pp']=self.monster['技能']['skill_3']['s_pp_max']
        #self.monster['技能']['skill_4']['s_pp']=self.monster['技能']['skill_4']['s_pp_max']
        #self.info=self.monster['基础']['name']+'使用了pp药水\n'
        self.skill_num='pp'
        self.skill_isuse=True

