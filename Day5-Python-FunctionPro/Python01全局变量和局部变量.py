# -----------------局部变量-----------------------
# 【局部变量】：就是在函数内部定义的变量，”作用域仅仅局限于函数的内部“
# 不同的函数可以定义相同的变量，但是各自用各自的，不会产生影响
# 局部变量的作用：为了临时保存数据，需要在函数中定义来存储数据
# -----------------全局变量-----------------------
# 【全局变量】：函数的作用域不同
# 当全局变量和局部变量出现重复定义的时候，程序会优先执行使用函数内部定义的：局部变量【优先级最高】

# 以下为全局变量
subject = '信息工程'  # 全局变量
name = '小慧'


def printInfo():
    name = '小牛'  # 局部变量【优先级最高】
    print("姓名：{},专业是：{}".format(name, subject))
    pass


def testInfo():
    name = '张学友'
    print(name, subject)
    pass


def ChangeGlobal():
    '''
    修改全局变量
    :return:
    '''
    global subject  # 利用 关键字global 修改外部全局变量
    subject = '英格里希'
    pass


ChangeGlobal()
print(subject)

# printInfo()
# testInfo()
