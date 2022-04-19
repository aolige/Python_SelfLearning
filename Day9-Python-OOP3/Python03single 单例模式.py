# # 单例模式： 是一种常用的软件设计模式
# 目的：确保某一个类只有一个实例存在
# 如果希望在某个系统中，某个类只能出现一个实例的时候，那么这个单例对象就满足要求

# 创建一个单例对象  基于__new__去实现的【推荐使用得一种】

class DataBaseClass(object):

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_danli'):
            cls._danli = super().__new__(cls, *args, **kwargs)  # 需要调用父类的new方法
        return cls._danli

    pass


class Data1(DataBaseClass):
    pass


dd1 = DataBaseClass()
print(id(dd1))
dd2 = DataBaseClass()
print(id(dd2))
dd3 = Data1()
print(id(dd3))










