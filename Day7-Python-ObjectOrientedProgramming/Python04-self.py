class Animal(object):

    # 如果不特殊定义，__new__是默认运行的，如果定义了，则以定义的规则为准
    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法 ：每调用一次就会生成一个新的对象，cls 是class 的缩写

        场景：可以控制创建对象的一些属性限定 经常用来做单例模式的时候来使用
        :param args:
        :param kwargs:
        '''
        print('__new__函数执行了')
        return object.__new__(cls)  # 在这里是真正创建对象实例的
        pass

    '''
    定义类
    '''

    def __init__(self, sex, weight):
        '''
        初始化实例，传参
        :param name:
        '''
        self.sex = sex
        self.weight = weight
        print('__init__函数执行了')
        pass

    def GetSelf(self, name, age):
        '''
        实例方法
        :return:
        '''
        # print(id(self))
        # **********   self.sex,self.weight相当于调用实例自己的数据
        print('{}今年{}岁啦,性别：{}，体重：{}'.format(name, age, self.sex, self.weight))
        pass

    def __str__(self):
        '''
        将对象转化成字符串str(对象)测试的时候，打印对象的信息
        :return:
        '''
        return '打印:  {}   {}  '.format(self.sex, self.weight)


zx = Animal('girl', '46')
print(zx)

# Tiger = Animal('女','76kg')
# # print(id(Tiger))
# print(Tiger)

# 小结 self 特点
# 1、self只有在类中定义 实例方法的时候才有意义，在调用的时候不必传入相应的参数，而是由解释器 自动去指向
# 2、self的名字是可以更改的，可以定义成其他名字，只是约定俗成的定义成了 self
# 3、self指向的是 类实例对象本身，相当于Java中的 this


#  __new__ 和 __init__ 函数的区别
# __new__ 类的实例化方法，必须返回（return）该实例,否则对象就创建不成功
# __init__ 用来做数据属性初始化的，也可以认为是实例的构造方法，接受类的实例 self 并对其构造
# __new__ 有一个参数，至少是cls,代表要实例化的类，此参数在实例化时，由Python解释器自动提供
# __new__ 比 __init__ 要更早执行


