# 函数的定义
# def printA():
#     '''
#     这个函数是用来打印个人信息的组合
#     :return:
#     '''
#     print('小刘的身高是：%f'%1.70)
#     print('小刘的性别是：%s'%'男')
#     print('小刘的体重是：%f kg'%65)
#     print('小刘的专业是：%s'%'信息工程')
#     pass

# 函数的调用
# printA()
# printA()  # 多次调用

# 1、进一步完善需求【输出不同人的信息】
# 方案：通过传入参数来解决
def printA(name, height, weight, sex, pro):
    '''
    :return:
    '''
    print('%s的身高是：%f' % (name, height))
    print('%s的性别是：%s' % (name, sex))
    print('%s的体重是：%f kg' % (name, weight))
    print('%s的专业是：%s' % (name, pro))
    pass


printA(name='小刘', height=1.70, weight=65, sex='男', pro='信息工程')
printA('小慧', 1.68, 54, '女孩子', '审计学')
