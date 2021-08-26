import random



def seer_damage(level,skill,attack,defend,attr,same=True):
    '''
    赛尔号精灵伤害计算,由infinite网上整理
    链接：https://tieba.baidu.com/p/6085129190/
    
    Parameters
    ----------
    level:
        等级
    skill：
        技能伤害
    attack：
        己方精灵攻击力（特攻
    defend：
        对方精灵防御力（特防
    attr：
        克制系数
    same:
        是否使用本系技能出招
    '''

    #等级系数
    factor_level=(level*0.4+2)/50
    #攻防系数
    factor_att=attack/defend
    #随即系数
    factor_random=(random.randint(217,255))/255
    #属性系数
    if(same!=True):
        factor_attr=attr
    else:
        factor_attr=1.5*attr
    #计算伤害
    return (factor_level*skill*factor_att+2)*factor_random*factor_attr

def seer_counter_single(monster1_attr,monster2_attr):
    '''
    赛尔号单属性克制系数，由橙汁整理
    链接：https://www.bilibili.com/read/cv6206519/

    Parameters:
    monster1_attr:
        精灵1属性
    monster2_attr：
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
    链接：https://www.bilibili.com/read/cv6206519/

    Parameters:
    monster1_attr:
        精灵1属性
    monster2_attr：
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

class Seer_combat(object):
    """
    赛尔号对战类

    """
    def __init__(self, monster1, monster2):
        '''
        对战初始化

        Parameter
        ----------
        monster1:dict
            精灵1属性：
                level:等级
                skill:技能伤害
                attack:攻击力
                defend：防御力
                attr：精灵属性
                e.g. mon1={'level':100,'skill':160,'attack':500,'defend':300,'attr':['圣灵']}

        monster2:dict
            精灵2属性

        '''
        self.monster1=monster1
        self.monster2=monster2

    def damage(self):
        return seer_damage(self.monster1['level'],\
                    self.monster1['skill'],\
                    self.monster1['attack'],\
                    self.monster2['defend'],\
                    seer_counter(self.monster1['attr'],\
                                self.monster2['attr']),\
                    same=True)

mon1={'level':100,'skill':160,'attack':500,'defend':300,'attr':['圣灵']}
mon2={'level':100,'skill':160,'attack':500,'defend':300,'attr':['圣灵']}
com=Seer_combat(mon1,mon2)
print(com.damage())