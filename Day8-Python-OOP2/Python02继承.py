# 在python中展现面向对象的三大特征：
# 封装、继承、多态

# 1、封装：指的是把内容封装到某个地方，便于后面的使用
# 它需要：
# ---把内容封装到某个地方
# ---从另外的地方去调用被封装的内容
# 对于封装来说，
# ---其实就是使用初始化构造方法将内容封装到对象中，然后通过对象直接或者self来获取被封装的内容

# 2、继承：和现实生活当中的继承是一样的，子可以继承父的内容【属性和行为】
# （爸爸拥有的儿子都有，儿子有的父亲不一定有）
# 对于面向对象的继承来说，其实就是将多个类的共有方法都提取到了父类中，
# 子类仅需继承父类而不必一一去实现
# 这样可以极大的提高效率，减少代码的重复编写，可以精简代码的层级结构，便于扩展
# class 父类():
#     '''
#     子类可以继承父类中公共的方法
#     '''
#     def 方法
#         pass
#     pass


class Animal(object):
    def eat(self):
        print('吃东西')
        pass

    def drink(self):
        print('喝水水')
        pass


class Cat(Animal):  # Cat继承Animal这个父类
    def voice(self):
        print('喵喵叫')
        pass

    pass


class Dog(Animal):
    def voice(self):
        print('汪汪叫')
        pass

    pass


# cat = Cat()
# cat.eat()
#
# dog = Dog()
# dog.voice()


# 多继承概念：
# 从多个父类中继承方法


class Book(object):
    def Buy(self):
        print('一本书卖1块钱')
        pass
    pass


class People(object):
    def run(self):
        print('人会跑')
        pass
    pass


class CollegeStu(Book,People):
    def study(self):
        print("大学生在学校学习")
        pass
    pass


# liulang = CollegeStu()
#
# liulang.Buy()
# liulang.run()

# 当多个父类中存在相同方法时，应该调用哪一个呢

class A(object):
    def run(self):
        print('A中的run')
        pass
    pass


class B(A):
    # def run(self):
    #     print('B中的run')
    #     pass
    pass


class C(A):
    pass


class On(C,B):
    pass


ll = On()
ll.run()
print(On.__mro__)  # 可以显示类的依次继承关系！！！！







