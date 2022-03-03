# 小结：
# 1、在Python中，万物皆对象，在函数调用的时候，实参传递的就是对象的引用
# 2、了解了原理之后，就可以更好的把控 在函数内部的处理是否会影响到外部数据变化
# 3、参数传递是通过对象引用来完成

a = 1  # 不可变类型
def func(x):
    print('x的地址：{}'.format(id(x)))
    x = 2
    print('修改后x的地址：{}'.format(id(x)))
    pass


# print('a的地址：{}'.format(id(a)))
# func(a)
# print('a的地址：{}'.format(id(a)))

# 可变类型
li = []


def TestFunc(parms):
    print(id(parms))
    li.append([1,2,2,3,4,5,5])
    print('内部的对象：{}'.format(parms))
    pass


print(id(li))
TestFunc(li)
print('外部的变量对象：{}'.format(li))