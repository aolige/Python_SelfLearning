import time

# 1、什么是类，什么是对象
# 类：相当于模板
# 对象:是根据模板创建的实例

# 2、python中定义一个类的语法格式是什么
# class 类名(object):

# 3、类（class）由哪三个部分构成
# 类名、属性、方法

# 4、init方法有什么作用，如何定义
# init方法是用于初始化实例的
# 定义方式：
# def __init__(self):

# 5、方法中的“self”代表什么
# self代表实例自身

# 6、在类中定义init方法的时候第一个形参必须是self吗？self可以用其他东西代替吗
# 不是必须为self，self可以用其他代替，列如：her，但是必须有一个默认的形参

# 7、Python面向对象中的魔术方法，是如何定义的，魔术方法需要开发人员去调用吗
# 定义方式：def __init__(self):、def __new__(self):、def __str__(self):
# 魔术方法不需要开发人员调用，系统自动调用

# 8、str 方法可以没有返回值，这句话正确吗
# __str__需要有返回值，return 返回打印的内容

# 9、查看下列代码，请写出那些是属性，哪些是实例方法
class Person(object):
    # 以下为类属性
    foot = 2
    eye = 2
    mouth =1

    def __init__(self,name,age):
        '''
        初始化实例
        :param name:
        :param age:
        '''
        # 以下为实例属性
        self.name = name
        self.age = age
        print("self=%s" % id(self))
        pass

    # 实例方法：run、eat
    def run(self):
        print('跑得飞快')
        pass

    def eat(self):
        print('一顿能吃两钵钵')
        pass
    pass


# xiaoming = Person('小明',18)
# print("xiaoming=%s" % id(xiaoming))

# 实操题
# 1、python中如何通过类创建对象，请用代码举例说明
# 2、如何在类中定义一个方法，请用代码举例说明
# 3、定义一个水果类，然后通过水果类，创建苹果对象，橘子对象，西瓜对象，并添加上颜色属性
# 4、编写代码，证明self就是实例本身
class Fruit(object):
    '''
    定义一个水果类
    '''
    def __init__(self,name,color):
        '''
        初始化实例的属性：颜色
        :param color:
        '''
        self.name = name
        self.color = color
        print("%s self= %s" % (self.name,id(self)))
        pass

    def Buy(self):
        print('水果大甩卖，10元一斤')
        pass
    pass


# apple = Fruit('苹果','红色')
# print('苹果 self= %s' % id(apple))
# print('{}是{}的'.format(apple.name,apple.color))
#
# orange = Fruit('橘子','橙色')
# print('橘子 self= %s' % id(orange))
# print('{}是{}的'.format(orange.name,orange.color))
#
# watermelon = Fruit('西瓜','绿色')
# print('西瓜 self= %s' % id(watermelon))
# print('{}是{}的'.format(watermelon.name,watermelon.color))

# 5、定义一个Animal类
class Animal(object):
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
        pass

    def run(self):
        print('{}正在狂奔~~~~'.format(self.name))
        pass

    def eat(self):
        print('{}正在吃草~~~'.format(self.name))
        pass

    def __str__(self):
        return '{}今年{}岁，它的身上是{}的'.format(self.name,self.age,self.color)
        pass
    pass


# niuniu = Animal('牛牛','8','棕色')
# niuniu.eat()
# niuniu.run()
# print(niuniu)


# 6、重写一遍紫禁之巅
# 决战紫禁之巅
# 问题分析
# ·决战紫禁之巅有两个人物，西门吹雪以及叶孤城
# ·属性:
# name玩家的名字. blood玩家血量
# ·方法:
# tong()捅对方一刀,对方掉血10滴
# kanren()砍对方一刀，对方掉血15滴
# chiyao()吃一颗药，补血10滴
# __str__打印玩家状态。

class XiaKe:
    '''
    侠客类
    '''
    def __init__(self,name,blood):
        '''
        初始化实例属性
        :param name:
        :param blood:
        '''
        self.name = name
        self.blood = blood

        pass

    def tong(self,enemy):
        '''
        动作：捅人
        :param enemy:
        :return:
        '''
        print('【{}】捅了【{}】一刀'.format(self.name,enemy.name))
        enemy.blood -= 10
        pass

    def kanren(self,enemy):
        '''
        动作：砍人
        :param enemy:
        :return:
        '''
        print('【{}】砍了【{}】一刀'.format(self.name,enemy.name))
        enemy.blood -= 15
        pass

    def chiyao(self):
        '''
        动作：回血
        :return:
        '''
        print('【{}】耍无赖，用了回血药'.format(self.name))
        self.blood += 10
        pass

    def __str__(self):
        return '【{}】还剩下【{}】点血量'.format(self.name,self.blood)
        pass

    pass


XMCX = XiaKe('西门吹雪',int(input('请输入西门吹雪的血量：')))
YGC = XiaKe('叶孤城',int(input('请输入叶孤城的血量：')))
print('--------------战斗开始！--------------')


while True:
    if XMCX.blood <= 0:
        print('西门吹雪死翘翘了，游戏已经结束嘞~')
        break
        pass
    if YGC.blood <= 0:
        print('叶孤城死翘翘了，游戏已经结束嘞~')
        break
        pass
    if XMCX.blood >= YGC.blood:
        YGC.tong(XMCX)
        XMCX.kanren(YGC)
        print(XMCX)
        print(YGC)
        print('________________________________________')
    else:
        XMCX.tong(YGC)
        YGC.kanren(XMCX)
        print(XMCX)
        print(YGC)
        print('________________________________________')
    # print('________________________________________')
    # XMCX.tong(YGC)
    # print(XMCX)
    # print(YGC)
    # print('________________________________________')
    # XMCX.kanren(YGC)
    # print(XMCX)
    # print(YGC)
    # print('________________________________________')
    # XMCX.chiyao()
    # print(XMCX)
    # print(YGC)

    time.sleep(1)
    pass











