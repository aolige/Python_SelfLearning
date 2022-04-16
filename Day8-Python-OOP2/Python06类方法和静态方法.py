# 类方法的概念：
# 类对象所拥有的方法，需要用装饰器@classmethod来标识其为类方法，对于类方法，
# 第一个参数必须是类对象，一般以cls作为第一个参数，类方法可以通过类对象，实例对象调用


class People(object):
    City = '成都'

    # 类方法，需要用@classmethod来进行修饰
    @classmethod
    def getCity(cls):
        print(cls.City)  # 访问类属性
        pass

    @classmethod
    def changeCity(cls,change):
        cls.City = change

    pass


peo = People()
peo.getCity()

People.changeCity('澳大利亚')
print(peo.City)













