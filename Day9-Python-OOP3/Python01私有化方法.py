# 使用私有属性的场景
# 1、把特定的一个属性隐藏起来，不想让类的外部进行直接调用
# 2、想保护这个属性，不想让属性的值随意的改变
# 3、保护这个属性，不想让派生类【子类】去调用

# 小结：
# 1、私有化的【实例】属性，不能在外部直接访问，可以在类的内部随意使用
# 2、子类不能继承父类的私有化属性【只能继承父类公共的属性和行为】
# 3、在属性前面加“__” 就可以变为私有化了


class Person:
    __hobby = '唱歌'

    def __init__(self):
        self.name = '小牛'
        self.__age = 18  # __age 为实例的私有属性（可以在类里面被调用，不可以被外部调用）
        pass

    def __str__(self):
        return '{}今年{}岁了'.format(self.name, self.__age)
        pass

    def changevalue(self):
        # self.__hobby = '打篮球'
        self.__eat()
        pass

    def __eat(self):
        print('hello，我是一个私有化方法，我正在被调用')
        pass

    # def get_hobby(self):
    #     return self.__hobby
    #     pass
    #
    # def set_hobby(self,hobby):
    #     self.__hobby = hobby
    #     pass

    # hobby = property(get_hobby, set_hobby)

    #  ————————————————————————————————————————————————

    # 通过装饰器方式去声明

    @property  # 用装饰器修饰，添加属性标志,提供一个getter方法
    def hobby(self):
        return self.hobby()
        pass

    @hobby.setter  # 提供一个setter方法
    def hobby(self, a):
        self.__hobby = a
        pass

    # ————————————————————————————————————————————————

    pass


class student(Person):
    pass


# hh = Person()
# print(hh.__hobby)
# print(Person.__hobby)

xl = Person()
# # print(xl.__age)
xl.changevalue()
# xl.hobby
# print(xl.hobby)

stu = student()  # 子类无法直接访问父类中的私有属性
# print(stu.__age)
