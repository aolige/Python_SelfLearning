
class Father1(object):
    '''
    定义一个父类
    '''
    def __init__(self,name,hobby):
        '''
        父类初始化实例属性
        :param name:
        :param hobby:
        '''
        self.name = name
        self.hobby = hobby
        pass


    def run(self):
        '''
        father1所具有的run方法
        :return:
        '''
        print('father1爸爸我会跑，跑的还非快')
        pass

    def eat(self):
        '''
        father1具有的eat方法
        :return:
        '''
        print('father1爸爸吃饭，一顿一斤')
        pass

    pass


class Father2(object):
    '''
    Father2类
    '''
    def eat(self):
        print('Father2的吃方法')
        pass



    pass


class Son(Father2,Father1):
    '''
    Son子类继承Father1
    '''
    def __init__(self,name,hobby,sports,job):
        '''
        继承父类的同时，重写父类，新增两个实例属性
        :param sports:
        :param job:
        '''
        # Father1.__init__(self,name,hobby)
        super().__init__(name,hobby)
        self.sports = sports
        self.job = job
        pass

    def __str__(self):
        return '{}{}{}{}'.format(self.name,self.hobby,self.sports,self.job)

    pass


son = Son('张三','唱歌','跑步','IT')
son.run()
son.eat()
print(son)
print(Son.__mro__)











