class Animal(object):
    '''
    定义类
    '''
    def __init__(self,sex,weight):
        '''
        初始化实例，传参
        :param name:
        '''
        self.sex = sex
        self.weight = weight
        pass

    def GetSelf(self,name,age):
        '''
        实例方法
        :return:
        '''
        # print(id(self))
        # **********   self.sex,self.weight相当于调用实例自己的数据
        print('{}今年{}岁啦,性别：{}，体重：{}'.format(name,age,self.sex,self.weight))
        pass

    def __str__(self):
        '''
        将对象转化成字符串str(对象)测试的时候，打印对象的信息
        :return:
        '''
        return '打印:  {}   {}  '.format(self.sex,self.weight)




Tiger = Animal('女','76kg')
print(id(Tiger))
Tiger.GetSelf('小狮子','5')
print(Tiger)

# 小结 self 特点
# 1、self只有在类中定义 实例方法的时候才有意义，在调用的时候不必传入相应的参数，而是由解释器 自动去指向
# 2、self的名字是可以更改的，可以定义成其他名字，只是约定俗成的定义成了 self
# 3、self指向的是 类实例对象本身，相当于Java中的 this















