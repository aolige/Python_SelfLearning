# 类型转换

# 二进制的转换bin()
print(bin(10))  # 2进制
print(hex(17))  # 16进制

# 元组转换为列表
tup = (1,2,3,4,5)
li = list(tup)
li.append('hahaha')
print(li,type(li))

tuplist = tuple(li)
print(tuplist,type(tuplist))

# 字典的操作dict()
dict1 = dict(a=2,b=4,c=4,名字='张三')
print(type(dict1))
# 追加字典内容
dict1['学校']='成都东软'
dict1['姓名']='小刘'
dict1['name']=25
print(dict1)


# bytes转换
print(bytes('你好牛蛙python',encoding='utf-8'))
