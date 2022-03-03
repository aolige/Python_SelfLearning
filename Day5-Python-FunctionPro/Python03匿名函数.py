# 匿名函数
# 语法规则：
# lambda 参数1，参数2，参数3：表达式
# lambda x,y:x+y
# 特点：
# 1、使用lambda关键字去创建函数
# 2、没有名字的函数
# 3、匿名函数冒号后面的表达式有且只有一个，注意：是表达式，而不是语句
# 4、匿名函数自带return，而这个return的结果就是表达式计算后的结果

# 缺点：
# 1、lambda只能是单个表达式，不是代码块，lambda的设计就是为了简单函数的场景
# 仅仅能封装有限的逻辑，复杂逻辑实现不了，必须使用def处理 


def sum(x, y):
    '''
    计算参数和
    :param x:
    :param y:
    :return:
    '''
    return x + y
    pass


# print(sum(30, 20))

# 匿名函数简化函数封装
# m = lambda x, y:x+y
# print(m(20,34))

# Test = lambda a,b,c,d:a*b+c*d
# print(Test(1,2,4,5))

# age = int(input("请输入您的年龄："))
# print('未成年' if age < 18 else '你已经是个成年人了')  # 可以替换传统双分支的写法

# func1 = lambda x,y:x if x<y else y
# print(func1(2,1))

res = (lambda x,y:x if x<y else y)(2,3)  # 直接的调用
print(res)
