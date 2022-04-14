# 决战紫禁之巅
# 问题分析
# ·决战紫禁之巅有两个人物，西门吹雪以及叶孤城
# ·属性:
# name玩家的名字. blood玩家血量
# ·方法:
# tong()捅对方一刀,对方掉血10滴
# kanren()砍对方一刀，对方掉血15滴
# chiyao()吃一颗药，补血10滴
# _str_打印玩家状态。


import time


# 第一步，定义一个英雄 类
class Hero(object):
    '''
    类：英雄
    '''
    def __init__(self,name,blood,blue):
        '''
        初始化实例属性
        :param name:
        :param blood:
        :param blue:
        '''
        self.name = name
        self.blood = blood
        # self.blue = blue
        pass

    def tong(self,enemy):
        '''
        实例方法：捅一刀
        :param enemy:敌人
        :return:
        '''
        # 捅对方一刀, 对方掉血10滴
        enemy.blood -= 10
        InfoPrint = '{}捅了{}一刀'.format(self.name,enemy.name)
        print(InfoPrint)
        pass

    def kanren(self,enemy):
        '''
        砍人
        :param enemy:
        :return:
        '''
        # kanren()砍对方一刀，对方掉血15滴
        enemy.blood -= 15
        InfoPrint = '{}砍了{}一刀'.format(self.name,enemy.name)
        print(InfoPrint)
        pass

    def chiyao(self):
        '''
        吃药补血
        :return:
        '''
        # 吃一颗药，补血10滴
        self.blood += 10
        InfoPrint = '{}吃了一颗药'.format(self.name)
        print(InfoPrint)
        pass
    def __str__(self):
        return '{} 血量还剩 {}'.format(self.name,self.blood)
    pass


# 第二步，创建两个实例化对象

XMCX = Hero('西门吹雪',100,100)
YGC = Hero('叶孤城',100,100)
while True:
    if XMCX.blood <= 0 or YGC.blood <= 0:
        print('战斗结束')
        break

    XMCX.tong(YGC)
    print(XMCX)
    print(YGC)
    print('****************************************')
    YGC.kanren(XMCX)
    print(XMCX)
    print(YGC)
    print('****************************************')
    XMCX.chiyao()
    print(XMCX)
    print(YGC)
    print('****************************************')

    time.sleep(1) # 休眠一秒钟，暂停一秒钟
    pass







