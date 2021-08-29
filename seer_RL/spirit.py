布布花={
    '基础':{
    'name':'布布花',
    'level':100,
    'life':331,
    'life_max':331,
    'attack_p':254,
    'defend_p':246,
    'attack_s':186,
    'defend_s':206,
    'speed':148,
    'attr':['草'],
    'state':1,
    'heart':1/16,
    'heart_normal':1/16},

    '强化等级':{
    'r_hit':0,
    'r_ap':0,
    'r_dp':0,
    'r_as':0,
    'r_ds':0,
    'r_s':0,
    },
    '回合类标记':{
    '致命几率':{'Isopen':False,'content':0,'round':0},
    '叠加伤害':{'Isopen':False,'content':0,'name':'','round':0},
    },

    '技能':{'skill_1':{
            's_name':'光合作用',
            's_attr':['普通'],
            's_hit':101,
            's_type':'属性',
            's_damage':0,
            's_effect':{'回复':{'hp':0.5,'Pr':1}},
            's_pp_max':5,
            's_pp':5,
            's_early':0,#先制
            's_times':[1,1],
    },
    'skill_2':{
            's_name':'咬碎',
            's_attr':['普通'],
            's_hit':100,
            's_type':'物理',
            's_damage':100,
            's_effect':{'能力下降':{'type':'self','下降内容':{'r_dp':-2},'Pr':0.15}},
            's_pp_max':15,
            's_pp':15,
            's_early':0,#先制
            's_times':[1,1],
    },
    'skill_3':{
            's_name':'超级吸取',
            's_attr':['草'],
            's_hit':101,
            's_type':'特殊',
            's_damage':60,
            's_effect':{'吸血':{'hp':0.5,'Pr':1}},
            's_pp_max':10,
            's_pp':10,
            's_early':0,#先制
            's_times':[1,1],
    },
    'skill_4':{
            's_name':'飞叶风暴',
            's_attr':['草'],
            's_hit':101,
            's_type':'特殊',
            's_damage':140,
            's_effect':{'能力下降':{'type':'self','下降内容':{'r_as':-1},'Pr':1}},
            's_pp_max':5,
            's_pp':5,
            's_early':0,#先制
            's_times':[1,1],
    },
    'skill_hp':{
        's_early':0,#先制
    },
    'skill_pp':{
        's_early':0,#先制
    }

    }
}



魔焰猩猩={
    '基础':{
    'name':'魔焰猩猩',
    'level':100,
    'life':1081,
    'life_max':1081,
    'attack_p':260,
    'defend_p':196,
    'attack_s':260,
    'defend_s':196,
    'speed':264,
    'attr':['火'],
    'state':1,    
    'heart':1/16,
    'heart_normal':1/16},

    '强化等级':{
    'r_hit':0,
    'r_ap':0,
    'r_dp':0,
    'r_as':0,
    'r_ds':0,
    'r_s':0,
    },
    '回合类标记':{
    '致命几率':{'Isopen':False,'content':0,'round':0},
    '叠加伤害':{'Isopen':False,'content':0,'name':'','round':0},
    },

    '技能':{'skill_1':{
            's_name':'音速火拳',
            's_attr':['火'],
            's_hit':101,
            's_type':'物理',
            's_damage':70,
            's_damage_raw':70,
            's_effect':{},
            's_pp_max':5,
            's_pp':5,
            's_early':1,#先制
            's_times':[1,1],
    },
    'skill_2':{
            's_name':'绝密火焰',
            's_attr':['火'],
            's_hit':100,
            's_type':'物理',
            's_damage':100,
            's_damage_raw':100,
            's_effect':{'秒杀':{'type':'oppo','Pr':0.05}},
            's_pp_max':10,
            's_pp':10,
            's_early':0,#先制
            's_times':[1,1],

    },
    'skill_3':{
            's_name':'觉醒',
            's_attr':['普通'],
            's_hit':101,
            's_type':'属性',
            's_damage':0,
            's_damage_raw':0,
            's_effect':{'能力上升':{'type':'self','上升内容':{'r_ap':2,'r_as':2},'Pr':1}},
            's_pp_max':10,
            's_pp':10,
            's_early':0,#先制
            's_times':[1,1],
    },
    'skill_4':{
            's_name':'魔焰裂空击',
            's_attr':['火'],
            's_hit':101,
            's_type':'物理',
            's_damage':150,
            's_damage_raw':150,
            's_effect':{'致命几率':{'type':'self','round':5,'content':1/16,'Pr':1}},
            's_pp_max':5,
            's_pp':5,
            's_early':0,#先制
            's_times':[1,1],
    },
    'skill_hp':{
        's_name':'hp',
        's_early':0,#先制
        's_attr':['普通'],
        's_hit':101,
        's_type':'属性',
        's_damage':0,
        's_damage_raw':0,
        's_effect':{},
        's_pp_max':10,
        's_pp':10,
    },
    'skill_pp':{
        's_name':'pp',
        's_early':0,#先制
        's_attr':['普通'],
        's_hit':101,
        's_type':'属性',
        's_damage':0,
        's_damage_raw':0,
        's_effect':{},
        's_pp_max':10,
        's_pp':10,
    }


    }
}



鲁斯王={
    '基础':{
    'name':'鲁斯王',
    'level':100,
    'life':389,
    'life_max':389,
    'attack_p':276,
    'defend_p':222,
    'attack_s':226,
    'defend_s':220,
    'speed':208,
    'attr':['水'],
    'state':1,    
    'heart':1/16,
    'heart_normal':1/16},

    '强化等级':{
    'r_hit':0,
    'r_ap':0,
    'r_dp':0,
    'r_as':0,
    'r_ds':0,
    'r_s':0,
    },
    '回合类标记':{
    '致命几率':{'Isopen':False,'content':0,'round':0},
    '叠加伤害':{'Isopen':False,'content':0,'name':'','round':0},
    },

    '技能':{'skill_1':{
            's_name':'克制',
            's_attr':['普通'],
            's_hit':101,
            's_type':'属性',
            's_damage':0,
            's_damage_raw':0,
            's_effect':{'反弹':{'type':'oppo','Pr':1}},
            's_pp_max':5,
            's_pp':5,
            's_early':-6,#先制
            's_times':[1,1],
    },
    'skill_2':{
            's_name':'浪打千斤',
            's_attr':['水'],
            's_hit':100,
            's_type':'物理',
            's_damage':20,
            's_damage_raw':20,
            's_effect':{},
            's_pp_max':30,
            's_pp':30,
            's_early':0,#先制
            's_times':[5,8],

    },
    'skill_3':{
            's_name':'剑舞',
            's_attr':['普通'],
            's_hit':101,
            's_type':'属性',
            's_damage':0,
            's_damage_raw':0,
            's_effect':{'能力上升':{'type':'self','上升内容':{'r_ap':2},'Pr':1}},
            's_pp_max':15,
            's_pp':15,
            's_early':0,#先制
            's_times':[1,1],
    },
    'skill_4':{
            's_name':'湍流龙击打',
            's_attr':['水'],
            's_hit':101,
            's_type':'物理',
            's_damage':150,
            's_damage_raw':150,
            's_effect':{'叠加伤害':{'type':'self','round':1,'content':20,'Pr':1}},
            's_pp_max':5,
            's_pp':5,
            's_early':0,#先制
            's_times':[1,1],
    },
    'skill_hp':{
        's_name':'hp',
        's_early':0,#先制
        's_attr':['普通'],
        's_hit':101,
        's_type':'属性',
        's_damage':0,
        's_damage_raw':0,
        's_effect':{},
        's_pp_max':10,
        's_pp':10,
    },
    'skill_pp':{
        's_name':'pp',
        's_early':0,#先制
        's_attr':['普通'],
        's_hit':101,
        's_type':'属性',
        's_damage':0,
        's_damage_raw':0,
        's_effect':{},
        's_pp_max':10,
        's_pp':10,
    }

    }
}