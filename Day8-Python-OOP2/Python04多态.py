# 多态：顾名思义，就是多种状态、形态，
# 就是同一种行为对于不同的子类【对象】有不同的行为表现
# 遵守两个前提:
# 1、继承：多态必须发生在父类和子类之间
# 2、重写：子类重写父类的方法

# 多态有什么用：
# (鸭子类型——看起来像鸭子——关注的不是对象类型的本身，而是它是如何使用的)
# 1、可以增加程序的灵活性
# 2、增加程序的扩展性

class Animal(object):
    '''
    父类，基类
    '''
    def Say_who(self):
        print('这是一只动物')
        pass
    pass


class Dog(Animal):
    '''
    子类，派生类
    '''
    def Say_who(self):
        '''
        重写父类方法
        :return:
        '''
        print('这是一只狗')
        pass

    pass


class Chicken(Animal):
    def Say_who(self):
        print('这是一只咯咯鸡')
        pass
    pass


class Bird(Animal):
    def Say_who(self):
        print('这是一只小小鸟')
        pass
    pass


class People(object):
    def Say_who(self):
        print('这里是人类')
        pass
    pass


class Student(People):
    def Say_who(self):
        print('我是小学生，你能给我500块吗')
        pass
    pass


# dog = Dog()
# dog.Say_who()
# chicken = Chicken()
# chicken.Say_who()

# ------------------------------------------
def Func(obj):
    '''
    统一调用，实例“方法”的内容
    :param obj: 对象的实例
    :return:
    '''
    obj.Say_who()


# 将类全部归纳入列表中，通过for循环遍历列表，输出对象的say_who方法内容

listobj = [Dog(),Chicken(),Bird(),Student()]
for item in listobj:
    Func(item)
    pass

# ------------------------------------------











