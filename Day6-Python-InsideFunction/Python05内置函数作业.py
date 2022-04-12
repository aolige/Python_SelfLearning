# 作业一：
# 求三组连续自然数的和：求出1-10,、20-30、30-45的三个和
def NumSum():
    '''
    求连续自然数和
    :return:
    '''
    # sum = 0
    startNum = int(input('请输入起始数:'))
    endNum = int(input('请输入截止数：'))
    # for item in range(startNum,endNum+1):
    #     sum += item
    #     item += 1
    #     pass
    sum1 = sum(range(startNum,endNum+1))  # 利用sum函数求和
    return print('{}''至''{}''的连续自然数和为：{}'.format(startNum,endNum,sum1))
    pass

# a = 1
# while a <= 10:
#     print('---------------自然数求和计算器-------------')
#     print('还可以玩{}次'.format(10-a))
#     NumSum()
#     a += 1
#     pass


# 作业二：
# 100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三人吃1个馒头。请问大小和尚各多少人

def PerCount():
    '''
    计算各多少人
    a:大和尚，100-a:小和尚
    :return:
    '''
    for a in range(1,100):
        if a*3+(100-a)*(1/3) == 100:
            return print('大和尚{}人，小和尚{}人'.format(a,100-a))
            pass
    pass

# PerCount()


# 作业三：
# 指定一个列表，列表里面含有唯一一个只出现过一次的数字。写程序找出这个”独一无二“的数字
# li = [1,1,2,2,3,3,4,4,6,56,3,2]


li = [1,1,2,2,3,3,4,4,56,6,3,2]
set1 = set(li)  # 利用set去重，得到具有唯一值的集合
print(set1)
for item in set1:
    # 将集合和列表作比较，删除列表中含有集合内的元素
    # （这时列表内只出现过一次的值就不存在列表中了）
    li.remove(item)
    pass
set2 = set(li)
print(set2)
for item in set1:
    # 将set1 和 set2 作比较，得出唯一值
    if item not in set2:
        print(item)
        pass
    pass
pass


















