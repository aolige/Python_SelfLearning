# 定义类和对象
# 类结构：类名、属性、方法
# class 类名：（大驼峰命名法）
#     属性
#     方法


class Person(object):
    '''
    定义人，这个类的特征
    '''
    # 类属性
    name = '浪锅'
    age = '25'
    height = '170cm'
    weight = '65kg'
    # 实例属性：在方法内部定义的【通过类似self.变量名】 变量，称为实例属性

    def __init__(self):
        self.hobby = '唱歌'
        pass

    # 实例方法
    '''
    方法对应人的行为   实例方法
    '''
    def eat(self):
        print('一顿吃一斤')
        pass

    def run(self):
        print('100米冲刺只要6.5秒')
        pass

    pass

# 创建一个Python对象【类的实例化】
liulang = Person()

# 调用类中定义的函数
liulang.run()
liulang.eat()
# 引用类中的属性
liulang.name = '刘浪大哥'
print('{}的年龄是{}，身高是{}，体重是{}'.format(liulang.name,liulang.age,liulang.height,liulang.weight))

# 创建另一个实例
qiqi = Person()
qiqi.eat()
qiqi.run()












