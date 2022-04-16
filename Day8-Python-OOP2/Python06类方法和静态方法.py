# 类方法的概念：
# 类对象所拥有的方法，需要用装饰器@classmethod来标识其为类方法，对于类方法，
# 第一个参数必须是类对象，一般以cls作为第一个参数，类方法可以通过类对象，实例对象调用


class People(object):
    City = '成都'

    # 类方法，需要用@classmethod来进行修饰，第一个参数是cls
    @classmethod
    def getCity(cls):
        print(cls.City)  # 访问类属性
        pass

    @classmethod
    def changeCity(cls, change):
        cls.City = change
        pass

    @staticmethod
    def Getdata():
        return People.City
        pass

    pass


# peo = People()
# peo.getCity()
#
# People.changeCity('澳大利亚')
# print(peo.City)

px = People()
print(People.Getdata())

print(px.Getdata())  # 一般不会通过实例对象去访问静态方法，会浪费空间

# 为什么要使用静态方法？
# 由于静态方法主要用于存放【逻辑性的代码】，本身和类 以及 实例对象 没有交互
# 在静态方法 中不会涉及到类中【方法】和【属性】的操作
# 数据资源能够得到有效的充分利用

# ———————————————————————————————————————————————————————————————
# 从方法的形式可以看出来：
# 1、类方法 的第一个参数是类对象:cls 进而去引用类对象的属性和方法
#     必须用装饰器@classmethod 来修饰
# 2、实例方法 的第一个参数必须是：self 通过这个self 可以去引用类属性或者实例属性，
#     若存在相同名称的实例属性和类属性的话，实例属性的优先级最高
# 3、静态方法 不需要定义额外的参数，若是要引用属性的话，则可以通过类对象或者实例对象引用即可
#     必须用装饰器@staticmethod 来修饰

# ———————————————————————————————————————————————————————————————




# demo：返回当前的系统时间
import time  # 引入第三方的时间模块


class TimeTest:
    def __init__(self, hour, min, secend):
        self.hour = hour
        self.min = min
        self.secend = secend
        pass

    @staticmethod  # 功能完全独立时，使用静态方法
    def showtime():
        return time.strftime("当前系统时间为：%H:%M:%S", time.localtime())
        pass

    @staticmethod
    def add(x,y):
        return x+y
        pass

    pass


print(TimeTest.showtime())
print(TimeTest.add(10,20))