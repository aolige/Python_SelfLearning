# 【作业1】写函数，接收n个数字，求这些参数数字的和
def receive1(*args):
    sum1 = 0
    for i in args:
        sum1 += i
        pass
    return sum1
    pass


# func1 = receive1(1,2,3,4,5,6)
# print(func1)

# 【作业2????】写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
def Function1(args):
    list1 = [ ]
    for item in range(len(args)):
        if item % 2 == 1:
            list1.append(args[item])
        else:
            pass
    return list1

# li = [1,23,4,5,5]
# df = Function1(li)
# print(df)

# 【作业3】写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者。PS：字典中的value只能是字符串或列表
def dict1(**kwargs):

    pass