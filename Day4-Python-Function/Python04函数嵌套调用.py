# 函数嵌套
def func1():
    print('-----------开始执行11111----------')
    print('-----------执行代码11111----------')
    print('-----------结束执行11111----------')
    pass


def func2():
    print('-----------开始执行2----------')
    # 调用第一个函数
    func1()
    print('-----------结束执行2----------')
    pass


func2()

# 函数的分类：根据函数的返回值和函数的参数
# 有参数无返回值的
# 有参数有返回值的
# 无参数无返回值的
# 无参数有返回值的
