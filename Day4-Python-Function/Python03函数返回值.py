# 函数返回值
# 概念：函数执行完以后，会返回一个对象，如果在函数的内部有return，
# 就可以返回实际的值，否则返回none空
# 类型：可以返回任意类型，返回值类型应该取决于return后面的类型
# 用途：给调用方返回数据
# 在一个函数体内，可以出现多个return关键字，但肯定只能返回有一个return
# 如果在一个函数体内，执行了return，意味着函数就退出了，return后面的代码
# 将不会再执行

def sumA(a, b):
    sum1 = a + b
    return sum1  # 将计算的结果返回
    pass


# func = sumA(10, 30)  # 将返回值赋给其他的变量
# print(func)  # 函数的返回值返回到调用的地方

def CalComputer(sum):
    listA = []
    result = 0
    i = 1
    while i <= sum:
        result += i
        i += 1
        listA.append(result)
        pass
    return listA  # 返回值的类型由return决定
    pass


# func1 = CalComputer(5)
# print(type(func1))
# print(func1)


# 返回元组类型的值
def TupleReturn(a):
    '''
    返回元组类型的值
    :param a:
    :return:
    '''
    tuple1 = (a, a + 2, a + 3)
    return tuple1
    pass


print(type(TupleReturn(1)))
print(TupleReturn(1))
