# 类的传递过程中，我们把父类又称为基类，子类又称派生类，父类的属性和方法
# 可以一级一级传递到子类。（理论上多少级都可以传递，实际上不建议超过三级）
# ---------------------------------------------
# 继承中，父类方法重写：子类中存在和父类中相同的方法，
# 此时子类中的方法会覆盖父类的方法
# ---------------------------------------------
# 为什么要重写：
# 父类中的方法已经满足不了子类的需求，子类就可以重写父类或者完善父类的方法

# ---------------------------------------------

class Grandfather(object):
    # 父类方法，用于子类继承
    def __init__(self,name,hobby):
        self.name = name
        self.hobby = hobby
        pass

    def eat(self):
        print('爷爷吃饭米饭')
        pass
    pass


class Father(Grandfather):
    def __init__(self,name,hobby,height,weight):
        # 既要重写父类方法，由要在父类的方法上扩展
        # 这时需要调用父类的方法，执行完毕，就可以具备父类的两个属性了

        # Grandfather.__init__(self,name,hobby)  # 调用父类方法，手动

        # super()是自动找到父类，进而调用方法,如果继承了多个父类，会按照顺序逐个去查找，直至调用
        super().__init__(name,hobby)

        # 拓展自己独有的属性
        self.height = height
        self.weight = weight
        pass

    def __str__(self):
        return '名字：{}，兴趣爱好：{}，身高：{}，体重：{}'.format(self.name,self.hobby,self.height,self.weight)
        pass

    def eat(self):
        print('父亲吃面条')
        pass

    pass


# class Son(Father):
#     pass


zs = Father('张三','抽烟',100,23)
zs.eat()
print(zs)
# print(Son.__mro__)  # 打印继承的过程顺序






