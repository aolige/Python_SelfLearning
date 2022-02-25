# #a = 0
# #while a < 100:
# #    a += 1
# #    if (a % 7 == 0 or a % 10 == 7 or a // 10 == 7):
# #       continue
# #    else:
# #        print(a)
#
# for a in range(1,101):
#     if(a % 7 == 0 or a % 10 == 7 or a // 10 == 7):
#         continue
#     else:
#         print(a)

# 【作业1】写函数，接收n个数字，求这些参数数字的和
def Recive_Func(args):
    '''
    接收参数求和
    :param args: 传入数字n个
    :return: 返回值之和：sum
    '''
    sum = 0
    for i in args:
        sum += i
        pass
    return sum
    pass


# print(Recive_Func((1,2,3,4,5)))

# 【作业2????】写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
def Send_Func(a):
    '''
    传入列表或元组，返回新列表
    :param a: 列表、元组
    :return: new_list
    '''
    list1 = []
    count = 1
    for i in a:
        if count%2==1:
            list1.append(i)
            pass
        count += 1
        pass
    return list1
    pass


# send1 = (1,23,4,5,6)
# df = Send_Func(send1)
# print(df)


# 【作业3】写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者。PS：字典中的value只能是字符串或列表
def Dict_value(a):
    '''
    传入字典，返回新字典
    :param a: 字典
    :return: 保留value前两位的字典
    '''
    DictNew = {}
    for key,value in a.items():
        if len(value)>2:
            DictNew[key] = value[0:2:1]
            pass
        else:
            DictNew[key] = value
            pass
        pass
    return DictNew
    pass


# di1 = {'zhagnsan':'123','lisi':'345'}
# Di1 = di1
# print(Dict_value(Di1))
