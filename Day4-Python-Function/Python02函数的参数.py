# 参数的分类：
# 必选参数、默认参数[缺省参数]、可选参数、关键字参数

# 参数：
# 其实就是函数为了实现某项特定的功能，进而为了得到实现功能所需要的数据
# （为了得到外部数据的）

# 1、必选参数
# def sum(a, b, c):  # 形式参数[形参]：只是意义上的一种参数，在定义的时候是不占内存地址的
#     sum = a + b + c
#     print(sum)
#     pass
#
#
# # 函数调用 在调用的时候，必选参数 必须要赋值，不然会报错
# sum(1, 2, 4)  # 1,2,4 为实际参数[实参]：是实实在在的参数，占用内存地址的
# # print(id(sum(1,2,3)))

# 2、默认参数[缺省参数]
# 默认参数：始终存在于参数列表中的尾部
# def sumA(a=20,b=30):
#     print('默认参数使用=%d'%(a+b))
#     pass
#
#
# # 默认参数调用
# sumA()
# sumA(100)
# sumA(100,100)  # 在调用的时候，如果未赋值，就会用定义函数时给定的默认值

# 3、可选参数[不定长参数]  0-n个
# 当参数的个数不确定时使用，比较灵活
# def GetData(*args):  # 可变长的参数 arges
#     '''
#     可变长的参数类型，计算累加和
#     :param args:
#     :return:
#     '''
#     result = 0
#     for i in args:
#         result += i
#         pass
#     print('result=%d'%result)
#     pass
#
#
# GetData(1)
# GetData(1,2)
# GetData(1,1,10,1,1,1,)

# 4、关键字可变参数  0-n个
# 用 ** 来定义
# 在函数体内，参数关键字是一个 【字典类型】，key 是一个字符串
# def keyFunction(**kwargs):
#     print(kwargs)
#     pass
#
# # keyFunction(1,2,3)  # 不可以正常传递
# dictA = {'name':'刘浪','age':25}
# keyFunction(**dictA)
# keyFunction(name = '刘浪',age = 25)

# 5、可选参数+关键字参数 的 ：组合使用
def complexFunc(*args,**kwargs):
    '''
    可选参数:*args 必须放到 关键字可选参数:**kwargs 之前[有顺序之分]
    可选参数：接受的数据是一个[元组]类型的参数
    关键字可选参数：接受的数据是一个[字典]类型的参数
    :param args:
    :param kwargs:
    :return:
    '''
    print(args)
    print(kwargs)
    pass


# 自动识别，自动填充
complexFunc(1,2,3,5,name = 'liulang',age = 25,hobby = 'soccer')
print('==============================================')
complexFunc(name = 'liulang',age = 25,hobby = 'soccer')