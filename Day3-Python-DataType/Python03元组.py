# 元组的创建  不能修改
# tuple1 = ()  # 空元组
# print(id(tuple1))
# # print(type(tuple1))
# tuple1 = (1,23,45,'abcd',1.23,'XiaoHui',[1,23,2,4])
# print(id(tuple1))
# print(tuple1)
# 元组的查询
# for i in tuple1:
#     print(i,end=' ')
# print(tuple1[1:5:1])
# print(tuple1[::-2])  # 表示反转字符串，每隔两个取一个数
# print(tuple1[-3:-1:1])

# tuple1[-1][1] = 2131231  # 可以对元组中的列表内的值进行修改
# print(tuple1)

# tupleB = (1,)  # 当元组中只有一个数据项时，需要在数据项后加逗号.
# print(type(tupleB))

tupleC = (1,1,1,1,2,2,2,34,5,45,2,2,46,4)  #  tuple(range(10))
print(type(tupleC))
print(tupleC.count(2))  # 统计元组内元素的个数
