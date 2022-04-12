# set 是python中的一种数据类型，是一个无序且不重复的元素集合（容器）
# 类似于字典，但是只有key，没有value 。不支持索引和切片
# 创建集合

set1 = {'a','b','c','d'}  # set只有key，没有value
set2 = {'a','b','e','z'}
print(type(set1))
# 添加操作add()
# set1.add('y')

# 清空操作clear()
# set1.clear()

# 取差集difference()
re = set1.difference(set2)
re2 = set2.difference(set1)
print(set1)
print(set2)
print('set1和set2差集',re)
print('set2和set1差集',re2)

# 取交集 intersection()
JiaoJi =set1.intersection(set2)
print('取交集',JiaoJi)

# 取并集 union()
BinJi = set1.union(set2)
print('取并集',BinJi)

# pop 从集合中随机拿出数据，同时删除该数据
# print(set1)
# pop1 = set1.pop()
# print(pop1)
# print(set1)

# discard() 指定删除某个集合中的数据
# print(set1)
# set1.discard('c')
# print(set1)

# update() 更新集合
print(set1)
print(set2)
set1.update('m')
print(set1)






