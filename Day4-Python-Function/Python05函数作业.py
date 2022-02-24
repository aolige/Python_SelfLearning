# 【作业1】写函数，接收n个数字，求这些参数数字的和
def receive1(*args):
    '''
    处理可变长参数数据
    :param args:
    :return:
    '''
    sum1 = 0
    for i in args:
        sum1 += i
        pass
    return sum1
    pass


# func1 = receive1(1,2,3,4,5,6)
# print(func1)

# 【作业2????】写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
def Function1(item):
    """
    处理列表数据
    :param item: 接受的是列表或元组
    :return: 返回新列表
    """
    list1 = []
    count = 1
    for i in item:
        if count % 2 == 1:
            list1.append(i)
            pass
        count += 1
        pass
    return list1
    pass


# ra = list(range(1,10))
# aa = Function1(ra)
# print(aa)
# print("asd{}".format(aa))


# 【作业3】写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者。PS：字典中的value只能是字符串或列表
def dictAa(kwargs):
    '''
    处理字典类型的数据
    :param kwargs:字典类型
    :return:返回字典
    '''
    dict1 = {}

    for key,value in kwargs.items():
        if len(value) > 2:
            dict1[key] = value[0:2:1]  # 字典value切片
            pass
        else:
            dict1[key] = value
            pass
        pass
    return dict1
    pass


# dictA = {'name': 'zhagnsan', 'hobby': '1', 'school': '资阳中小学', 'aihao': [1, 2, 3, 4, 45, 5, 2]}
# ds = dictAa(dictA)
# print(ds)
