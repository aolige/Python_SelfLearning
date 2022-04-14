# 定义类和对象
class Bullet(object):
    '''
    定义一个子弹类
    '''
    def __init__(self,name,color,shape):
        '''
        声明实例属性、初始化实例：
        :param name:
        :param color:
        :param shape:
        :param speed:
        '''
        self.name = name
        self.color = color
        self.shape = shape
        pass

    def BulletMove(self,speed):
        '''
        定义实例方法：子弹运动轨迹
        :param speed:
        :return:
        '''
        print('这是{}的，{}形状的，{}子弹，速度为{}/秒'.format(self.color,self.shape,self.name,speed))
        pass

    def __str__(self):
        return '这是{}的，{}形状的，{}子弹'.format(self.color,self.shape,self.name)
        pass

    pass


Bullut1 = Bullet('终极爆弹','红色','三角')
Bullut2 = Bullet('普通子弹','白色','正方')
Bullut1.BulletMove('20')
Bullut2.BulletMove('10')
print(Bullut1)
print(Bullut2)






