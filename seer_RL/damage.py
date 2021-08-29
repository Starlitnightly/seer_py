import random
import numpy as np



def seer_damage(level,skill,attack,defend,attr,same=True):
    '''
    赛尔号精灵伤害计算,由infinite网上整理
    链接:https://tieba.baidu.com/p/6085129190/
    
    Parameters
    ----------
    level:
        等级
    skill:
        技能伤害
    attack:
        己方精灵攻击力（特攻
    defend:
        对方精灵防御力（特防
    attr:
        克制系数
    same:
        是否使用本系技能出招
    '''

    #等级系数
    factor_level=(level*0.4+2)/50
    #攻防系数
    if(defend==0):
        return 0
    else:
        factor_att=attack/defend
    #随即系数
    factor_random=(random.randint(217,255))/255
    #属性系数
    if(same!=True):
        factor_attr=attr
    else:
        factor_attr=1.5*attr
    #计算伤害
    da=(factor_level*skill*factor_att+2)*factor_random*factor_attr

    return da

def seer_counter_single(monster1_attr,monster2_attr):
    '''
    赛尔号单属性克制系数，由橙汁整理
    链接:https://www.bilibili.com/read/cv6206519/

    Parameters:
    monster1_attr:
        精灵1属性
    monster2_attr:
        精灵2属性
    '''
    invaild={'电':'地面',
    '地面':'飞行',
    '超能':'光',
    '光':'草',
    '次元':'暗影',
    '邪灵':'神灵',
    '混沌':'虚空'}
    if(monster1_attr in [key for key in invaild.keys()]):
        if(monster2_attr ==invaild[monster1_attr]):
            return 0

    counter,countered={},{}
    counter['草']=['水','地面','光']
    countered['草']=['草','火','飞行','机械','圣灵','远古','混沌','神灵']
    counter['水']=['火','地面']
    countered['水']=['草','水','圣灵','自然','混沌','神灵']
    counter['火']=['草','机械','冰']
    countered['火']=['水','火','圣灵','自然','混沌','神灵']
    counter['飞行']=['草','战斗','虫']
    countered['飞行']=['电','机械','次元','邪灵','自然','混沌']
    counter['电']=['水','飞行','暗影','次元','混沌','虚空']
    countered['电']=['草','电','神秘','圣灵','自然','神灵',]
    counter['机械']=['冰','战斗','远古','邪灵','神灵']
    countered['机械']=['水','火','电','机械','次元']
    counter['地面']=['火','电','机械','王','轮回']
    countered['地面']=['草','超能','暗影','龙','圣灵','自然','神灵','虫']
    counter['普通']=['']
    countered['普通']=['']
    counter['冰']=['草','飞行','地面','次元','远古','轮回','虫']
    countered['冰']=['水','火','机械','冰','圣灵','混沌','神灵']
    counter['超能']=['战斗','神秘','自然']
    countered['超能']=['机械','超能','虫']
    counter['战斗']=['机械','冰','龙','圣灵']
    countered['战斗']=['超能','战斗','暗影','邪灵','王']
    counter['光']=['超能','暗影','虫']
    countered['光']=['机械','冰','光','圣灵','邪灵','自然','神灵','轮回','虚空']
    counter['暗影']=['超能','暗影','次元']
    countered['暗影']=['机械','冰','光','圣灵','邪灵','神灵']
    counter['神秘']=['电','神秘','圣灵','自然','王','神灵','轮回']
    countered['神秘']=['地面','战斗','邪灵','混沌','虫']
    counter['龙']=['冰','龙','圣灵','邪灵']
    countered['龙']=['草','水','火','电','远古','虫']
    counter['圣灵']=['草','水','火','电','冰','远古','虚空']
    countered['圣灵']=['战斗','神秘','龙','轮回']
    counter['次元']=['飞行','机械','超能','邪灵','自然','虫','虚空']
    countered['次元']=['冰','王','混沌','神灵','轮回']
    counter['远古']=['草','飞行','神秘','龙','虚空']
    countered['远古']=['机械','冰','王','轮回']
    counter['邪灵']=['光','暗影','神秘','次元','自然']
    countered['邪灵']=['机械','冰','超能','圣灵','王','混沌','轮回']
    counter['自然']=['草','水','火','飞行','电','地面','光','王','轮回']
    countered['自然']=['机械','超能','战斗','暗影','神秘','次元','邪灵','混沌','虚空']
    counter['王']=['战斗','暗影','次元','邪灵']
    countered['王']=['超能','自然','虫']
    counter['混沌']=['飞行','冰','神秘','次元','邪灵','自然','神灵']
    countered['混沌']=['电','机械','战斗','轮回']
    counter['神灵']=['草','水','火','电','冰','远古','邪灵','混沌']
    countered['神灵']=['机械','战斗','龙']
    counter['轮回']=['光','暗影','圣灵','次元','邪灵','混沌']
    countered['轮回']=['冰','超能','自然','虚空']
    counter['虫']=['草','地面','战斗','混沌','虫']
    countered['虫']=['水','火','冰','光']
    counter['虚空']=['超能','战斗','光','神秘','自然','轮回']
    countered['虚空']=['飞行','暗影','圣灵','次元']

    if(monster2_attr in counter[monster1_attr]):
        return 2
    elif(monster2_attr in countered[monster1_attr]):
        return 0.5
    else:
        return 1

def seer_counter(monster1_attr,monster2_attr):
    '''
    赛尔号克制系数，由橙汁整理
    链接:https://www.bilibili.com/read/cv6206519/

    Parameters:
    monster1_attr:
        精灵1属性
    monster2_attr:
        精灵2属性
    '''
    monster1_attr_len=len(monster1_attr)
    monster2_attr_len=len(monster2_attr)
    if(monster1_attr_len==1 and monster2_attr_len==2):
        attr1=seer_counter_single(monster1_attr[0],monster2_attr[0])
        attr2=seer_counter_single(monster1_attr[0],monster2_attr[1])
        if(attr1==2 and attr2==2):
            return 4
        elif(attr1==0 or attr2==0):
            return (attr1+attr2)/4
        else:
            return (attr1+attr2)/2
    elif(monster1_attr_len==2 and monster2_attr_len==1):
        attr1=seer_counter_single(monster1_attr[0],monster2_attr[0])
        attr2=seer_counter_single(monster1_attr[1],monster2_attr[0])
        if(attr1==2 and attr2==2):
            return 4
        elif(attr1==0 or attr2==0):
            return (attr1+attr2)/4
        else:
            return (attr1+attr2)/2
    elif(monster1_attr_len==2 and monster2_attr_len==2):
        attr1=seer_counter_single(monster1_attr[0],monster2_attr[0])
        attr2=seer_counter_single(monster1_attr[1],monster2_attr[0])
        if(attr1==2 and attr2==2):
            factor1=4
        elif(attr1==0 or attr2==0):
            factor1=(attr1+attr2)/4
        else:
            factor1=(attr1+attr2)/2

        attr1=seer_counter_single(monster1_attr[0],monster2_attr[1])
        attr2=seer_counter_single(monster1_attr[1],monster2_attr[1])
        if(attr1==2 and attr2==2):
            factor2=4
        elif(attr1==0 or attr2==0):
            factor2=(attr1+attr2)/4
        else:
            factor2=(attr1+attr2)/2
        return (factor1+factor2)/2
    elif(monster1_attr_len==1 and monster2_attr_len==1):
        return seer_counter_single(monster1_attr[0],monster2_attr[0])
    else:
        return 1

    #print(seer_counter(['次元'],['暗影']))
    #print(seer_counter(['圣灵'],['电','火']))
    #print(seer_counter(['次元','电'],['地面']))
    #print(seer_counter(['圣灵','超能'],['电','火']))

def cal_skill_effect_pr(hit):
    hit_flag=False#技能命中标志
    pr=random.randint(0,100)
    if(pr in range(int(hit))):
        hit_flag=True
    else:
        hit_flag=False
    return hit_flag

class Seer_combat(object):
    """
    赛尔号对战类

    """
    def __init__(self, monster1, monster2, round=1):
        '''
        对战初始化

        Parameter
        ----------
        monster1:dict
            精灵1属性:

                基础:dict
                level:等级
                #skill:技能伤害
                life:体力
                attack_p:攻击
                defend_p:防御
                attack_s:特攻
                defend_s:特防
                speed:速度
                attr:精灵属性
                state:精灵状态，能动是1，不能动是0

                强化等级:dict
                r_hit:命中等级
                r_ap:攻击等级
                r_dp:防御等级
                r_as:特攻等级
                r_ds:特防等级
                r_s:速度等级

                

                技能:dict
                skill_1:技能1
                skill_2:技能2
                skill_3:技能3
                skill_4:技能4

                    技能详细:dict
                    s_hit:技能精准度
                    s_type:技能类别
                    s_damage:技能威力
                    s_effect:技能效果
                    s_pp_max:技能数量
                    s_pp:技能当前数量

                        技能效果:dict
                        e_round:持续生效回合数

                e.g. mon1={'level':100,'skill':160,'attack':500,'defend':300,'attr':['圣灵']}

        monster2:dict
            精灵2属性

        '''
        self.monster1=monster1
        self.monster2=monster2

    def print_state(self):
        #print(self.monster1)
        print('精灵1当前状态:\n','体力:{0}/{1}'.format(self.monster1['基础']['life'],self.monster1['基础']['life_max']),'\n强化等级:',self.monster1['强化等级'])
        print('skill_1:',self.monster1['技能']['skill_1']['s_pp'],'/',self.monster1['技能']['skill_1']['s_pp_max'])
        print('skill_2:',self.monster1['技能']['skill_2']['s_pp'],'/',self.monster1['技能']['skill_2']['s_pp_max'])
        print('skill_3:',self.monster1['技能']['skill_3']['s_pp'],'/',self.monster1['技能']['skill_3']['s_pp_max'])
        print('skill_4:',self.monster1['技能']['skill_4']['s_pp'],'/',self.monster1['技能']['skill_4']['s_pp_max'])
        
        print('精灵2当前状态:\n','体力:{0}/{1}'.format(self.monster2['基础']['life'],self.monster2['基础']['life_max']),'\n强化等级:',self.monster2['强化等级'])
        print('skill_1:',self.monster2['技能']['skill_1']['s_pp'],'/',self.monster2['技能']['skill_1']['s_pp_max'])
        print('skill_2:',self.monster2['技能']['skill_2']['s_pp'],'/',self.monster2['技能']['skill_2']['s_pp_max'])
        print('skill_3:',self.monster2['技能']['skill_3']['s_pp'],'/',self.monster2['技能']['skill_3']['s_pp_max'])
        print('skill_4:',self.monster2['技能']['skill_4']['s_pp'],'/',self.monster2['技能']['skill_4']['s_pp_max'])
        
    def monster_skill(self,skill_t='skill_2',mon_type=1):
        '''
        技能释放效果

        '''
        #计算真实伤害
        if(mon_type==1):
            monster1=self.monster1
            monster2=self.monster2
        elif(mon_type==2):
            monster1=self.monster2
            monster2=self.monster1



        level=monster1['基础']['level']
        skill=monster1['技能'][skill_t]

        if(skill_t=='skill_pp'):
            self.monster['技能']['skill_1']['s_pp']=self.monster['技能']['skill_1']['s_pp_max']
            self.monster['技能']['skill_2']['s_pp']=self.monster['技能']['skill_2']['s_pp_max']
            self.monster['技能']['skill_3']['s_pp']=self.monster['技能']['skill_3']['s_pp_max']
            self.monster['技能']['skill_4']['s_pp']=self.monster['技能']['skill_4']['s_pp_max']
            return('回复了pp\n')
        elif(skill_t=='skill_hp'):
            monster1['基础']['life']+=200
            return('回复了血量\n')



        reforce1=monster1['强化等级']
        reforce2=monster2['强化等级']
        #计算attack
        if(skill['s_type']=='物理'):
            if(reforce1['r_ap']>0):
                factor1=0.5
                attack=monster1['基础']['attack_p']*(1+factor1*reforce1['r_ap'])
            else:
                factor1=0.75
                attack=monster1['基础']['attack_p']*(np.power(factor1,0-reforce1['r_ap']))
        elif(skill['s_type']=='特殊'):
            if(reforce1['r_as']>0):
                factor1=0.5
                attack=monster1['基础']['attack_s']*(1+factor1*reforce1['r_as'])
            else:
                factor1=0.75
                attack=monster1['基础']['attack_s']*(np.power(factor1,0-reforce1['r_as']))
                #print(factor1,reforce1['r_as'],attack)
        else:
            attack=0
        #计算defend
        if(skill['s_type']=='物理'):
            if(reforce2['r_dp']>0):
                factor2=0.5
                defend=monster2['基础']['defend_p']*(1+factor2*reforce2['r_dp'])
            else:
                factor2=0.75
                defend=monster2['基础']['defend_p']*(np.power(factor2,reforce2['r_dp']))
        elif(skill['s_type']=='特殊'):
            if(reforce2['r_ds']>0):
                factor2=0.5
                defend=monster2['基础']['defend_s']*(1+factor2*reforce2['r_ds'])
            else:
                factor2=0.75
                defend=monster2['基础']['defend_s']*(np.power(factor2,reforce2['r_ds']))
        else:
            defend=0
        #计算属性系数
        print(skill['s_attr'],\
                                monster2['基础']['attr'])
        factor_attr=seer_counter(skill['s_attr'],\
                                monster2['基础']['attr'])

        #计算是否致命一击
        h=int(cal_skill_effect_pr(monster1['基础']['heart']*100))
        if(h):
            heart=2
        else:
            heart=1

        #判断是否是本系技能
        if(skill['s_attr']==monster1['基础']['attr']):
            same=True
        else:
            same=False

        #计算攻击次数
        tim=random.randint(skill['s_times'][0],skill['s_times'][1])
        s_d=skill['s_damage']*tim

        #计算造成伤害
        damage=(seer_damage(level,\
                    s_d,\
                    attack,\
                    defend,\
                    factor_attr,same))
        damage=int(damage)*heart

        #计算技能命中概率
        hit_flag=False#技能命中标志
        if(reforce1['r_hit']>0):
            factor3=0.5
        else:
            factor3=0.25
        hit_flag=cal_skill_effect_pr(int(skill['s_hit']*(1+factor3*reforce1['r_hit'])))


        #技能pp减少
        skill['s_pp']-=1

        #monster2体力下降
        monster2['基础']['life']-=damage
        print('{0}对{1}使用了{2}造成了{3}点伤害'.format(\
            monster1['基础']['name'],\
            monster2['基础']['name'],\
            skill['s_name'],\
            damage))

        

        #结算技能效果
        s_effect=skill['s_effect']
        n_effect=''
        for i in s_effect.keys():
            if(i=='回复'):
                if(int(cal_skill_effect_pr(s_effect[i]['Pr']*100))):
                    n_effect='生命值得到了回复'
                    now_life=monster1['基础']['life']
                    l=now_life+s_effect[i]['hp']*monster1['基础']['life_max']
                    if(l>monster1['基础']['life_max']):
                        monster1['基础']['life']=monster1['基础']['life_max']
                    else:
                        monster1['基础']['life']=l
            elif(i=='吸血'):
                if(int(cal_skill_effect_pr(s_effect[i]['Pr']*100))):
                    ex_life=damage*s_effect[i]['hp']
                    monster1['基础']['life']+=ex_life
                    if(monster1['基础']['life']>monster1['基础']['life_max']):
                        monster1['基础']['life']=monster1['基础']['life_max']
                    n_effect='造成对手伤害的{}回复了自身的血量'.format(ex_life)

            elif(i=='秒杀'):
                if(int(cal_skill_effect_pr(s_effect[i]['Pr']*100))):
                    n_effect='触发了秒杀效果'
                    if(s_effect[i]['type']=='self'):
                        monster1['基础']['life']=0
                    else:
                        monster2['基础']['life']=0
            elif(i=='反弹'):
                if(int(cal_skill_effect_pr(s_effect[i]['Pr']*100))):
                    monster2['基础']['life']+=(monster1['基础']['life']-monster1['基础']['now_life'])*2
                    n_effect='反弹了{0}伤害'.format((monster1['基础']['life']-monster1['基础']['now_life'])*2)

                    
            elif(i=='能力下降'):
                if(int(cal_skill_effect_pr(s_effect[i]['Pr']*100))):
                    n_effect='能力下降了'
                    if(s_effect[i]['type']=='self'):
                        for j in s_effect[i]['下降内容'].keys():
                            monster1['强化等级'][j]+=s_effect[i]['下降内容'][j]
                    else:
                        for j in s_effect[i]['下降内容'].keys():
                            monster2['强化等级'][j]+=s_effect[i]['下降内容'][j]
            elif(i=='能力上升'):
                if(int(cal_skill_effect_pr(s_effect[i]['Pr']*100))):
                    n_effect='能力上升了'
                    if(s_effect[i]['type']=='self'):
                        for j in s_effect[i]['上升内容'].keys():
                            monster1['强化等级'][j]+=s_effect[i]['上升内容'][j]
                    else:
                        for j in s_effect[i]['上升内容'].keys():
                            monster2['强化等级'][j]+=s_effect[i]['上升内容'][j]

            elif(i=='致命几率'):
                if(int(cal_skill_effect_pr(s_effect[i]['Pr']*100))):
                    n_effect='致命几率上升了'
                    if(s_effect[i]['type']=='self'):
                        monster1['回合类标记']['致命几率']['Isopen']=True
                        monster1['回合类标记']['致命几率']['content']+=s_effect[i]['content']
                        monster1['回合类标记']['致命几率']['round']+=s_effect[i]['round']
                    else:
                        monster2['回合类标记']['致命几率']['Isopen']=True
                        monster2['回合类标记']['致命几率']['content']+=s_effect[i]['content']
                        monster2['回合类标记']['致命几率']['round']+=s_effect[i]['round']

            elif(i=='叠加伤害'):
                if(int(cal_skill_effect_pr(s_effect[i]['Pr']*100))):
                    monster1['回合类标记']['叠加伤害']['Isopen']=True
                    monster1['回合类标记']['叠加伤害']['skill']=skill['s_name']
                    monster1['回合类标记']['叠加伤害']['content']+=s_effect[i]['content']
                    monster1['回合类标记']['叠加伤害']['round']+=s_effect[i]['round']

        if(h):
            return('致命一击：{0}对{1}使用了{2}造成了{3}点伤害\n{4}'.format(\
            monster1['基础']['name'],\
            monster2['基础']['name'],\
            skill['s_name'],\
            damage,n_effect+'\n'))
        else:
            return('{0}对{1}使用了{2}造成了{3}点伤害\n{4}'.format(\
            monster1['基础']['name'],\
            monster2['基础']['name'],\
            skill['s_name'],\
            damage,n_effect+'\n'))








mon1={'level':100,'skill':160,'attack':500,'defend':300,'attr':['圣灵']}
mon2={'level':100,'skill':160,'attack':500,'defend':300,'attr':['圣灵']}




#com=Seer_combat(布布花,布布花2)


