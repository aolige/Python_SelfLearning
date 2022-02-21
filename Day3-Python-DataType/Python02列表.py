# 【列表】
# li = [] 空列表
# list11 = [1,2,3,'张三','李四','wangermazi','哈哈哈哈哈']
# print(len(list11))  # len函数可以获取到列表对象中的数据个数
# print(type(list11))

# list2 = [1,2,3,4.555,'张三','李四','wangermazi','哈哈哈哈哈',True]
# print(list2)  # 输出完整的列表
# print(list2[0:5:1])  # 输出下标0-4的列表值
# print(list2[4::1])  # 输出第4个开始到最后的列表值
# print(list2[::-1])  # 反向输出列表值，负数：从右向左开始输出
# print(list2*2)  # 输出多次列表中的数据【复制*2次】

# print('----------------------------------列表元素增加--------------------------------')
# print('追加之前：',list2)
# list2.append(['dsfaf','32432','2321','24dsff'])  # 追加列表
# list2.append(88888,22)  # 追加数字
# print('追加之后：',list2)
# list2.insert(0,'插入的数据')  # 插入操作，指定一个位置插入
# print(list2)
#
# liData = list(range(10))  # 强制转换为list对象（快速声明一个数字列表）
# # print(type(liData))
# print(liData)
# # list2.extend(liData)  # 扩展列表，等于批量添加
# liData.extend([12,12,23,54,65])
# print(liData)
# print(list2)

# print('----------------------------------修改列表元素--------------------------------')
# list3 = [1,2,3,4.555,'张三','李四','wangermazi','哈哈哈哈哈',True]
# print('修改之前',list3)
# list3[0] = '修改第一个'
# print('修改之后',list3)

print('----------------------------------删除列表元素--------------------------------')
list4 = [1,2,3,1,4.555,'张三','李四','wangermazi','哈哈哈哈哈',True]
# print('删除之前：',list4)
# del list4[0]  # 删除第一个数据
# del list4[0:3]  # 删除0-3下标的数据
# list4.remove(1)  # 移除左边开始找到的第一个元素(remove移除的参数是数据值)
# list4.pop(2)  # 移除指定下标的元素(pop移除的参数是索引值)
# print('删除之后：',list4)

# index
print(list4.index('张三'))  # index 获取指定元素索引号，在整个列表中查询"张三“
print(list4.index('张三',3,8))  # 在3-8的索引当中查找”张三“

