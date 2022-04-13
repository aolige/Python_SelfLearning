# class Car(object):
#
#     def __init__(self):
#         '''
#         实例属性的声明
#         '''
#         self.name = '宝马'
#         self.sign = '川M231231'
#         self.color = '曜石黑'
#
#     def run(self):
#         '''
#         车的运动行为
#         :return:
#         '''
#         print('百公里加速4.5秒')
#         pass
#     pass
#
# BaoMa = Car()
# BaoMa.run()
# # BaoMa.name = '宝马车车'  # 添加实例属性
# # BaoMa.sign = '川A12312'  # 添加实例属性
# print(BaoMa.name,BaoMa.sign,BaoMa.color)
#
# BenChi = Car()
# # BenChi.name = '奔驰车车'  # 添加实例属性
# # BenChi.sign = '川C12312'  # 添加实例属性
# BenChi.run()
# print(BenChi.name,BenChi.sign,BenChi.color)

# __init__(self)  初始化方法


# ——————————————————————————————————————————————————————
# __init__(self)传递参数改进
class Car(object):
    # 传递参数
    def __init__(self,name,sign,color):
        '''
        实例属性的声明
        '''
        self.name = name
        self.sign = sign
        self.color = color

    def run(self):
        '''
        车的运动行为
        :return:
        '''
        print('{} {} {}百公里加速4.5秒'.format(self.sign,self.color,self.name))
        pass
    pass


BaoMa = Car('宝马','川W213213','骚气红')
BaoMa.run()
# print(BaoMa.name,BaoMa.sign,BaoMa.color)

BenChi = Car('奔驰','川W213243','漆黑')
BenChi.run()
# print(BenChi.name,BenChi.sign,BenChi.color)


# -----------------------------------------------------------
# 总结__init__
# 1、python自带的内置函数，具有特殊的函数   使用双下划线包起来的【魔术方法】
# 2、是一个初始化的方法，主要是用来定义实例属性和初始化数据的，并且这个函数是在创建对象的时候自动调用的
# 3、可以利用__init__ 传参的机制，可以定义功能更加强大，并且方便的 类



