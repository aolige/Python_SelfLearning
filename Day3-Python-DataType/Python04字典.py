# 如何创建一个字典
# 创建一个空字典
dictA = {'Class':'三年级二班','School':'成都东软学院'}
# 添加字典数据
dictA['name'] = '刘二哥'  # key:value
dictA['age'] = 25
dictA['job'] = '程序员'
# 结束添加
print(dictA)
print(len(dictA))  # 数据项长度

print(dictA['name'])  # 通过键获取对应的值
dictA['name'] = '周星驰'
print(dictA)
print(dictA.keys())  # .keys()获取字典所有的键
print(dictA.values())  # .values()获取字典所有的值
print(dictA.items())  # .items()获取字典所有的键值对
dictA.update({'age':46,'sex':"男"})  # .update()更新字典内键值对
del dictA['sex']  # del通过指定键删除字典的值

# 遍历字典
# for i,j in dictA.items():
#     print('%s == %s'%(i,j))

print("---------------------------字典排序-----------------------------")

dictB = {'Class':4,'School':3}
print(dictB)
# 对字典进行排序
# 按照 key键 的ASCII码顺序进行排序
print(sorted(dictB.items(),key=lambda d:d[0]))

# 按照 value值 的大小进行排序
print(sorted(dictB.items(),key=lambda d:d[1]))

