# 【1】
# Test = 'liuLang Learn Python'
# print(type(Test))
# print('获取第一个字符：%s'%Test[0])
# print('获取第二个字符：%s'%Test[1])
# for i in Test:
#     print(i,end='')

# 【2】
# name = '     liulang    '
# a = name  # 在此只是把name的内存地址赋给了a
# print("name的内存地址为：%d"%id(name))
# print("a的内存地址为：%d"%id(a))

# 【3】
# print('姓名首字母大写：%s'%name.capitalize()) # capitalize()首字母变大写
# a = name.strip()  # strip()去除字符串两侧的空格
# b = name.lstrip()  # lstrip()去除字符串左边(left)的空格
# c = name.rstrip()  # rstrip()去除字符串右边(right)的空格
# print(c)
# print(name.lstrip())
# print(Test.title())  # title()把每个单词的首字母变成大写

# 【4】
e = 'hELLo Pyhon'
# print(e.find("o"))  # 检测目标对象是否在序列中，如果存在，返回对象所在下标值；如果不存在，返回-1
# print(e.index('o'))  # 检测字符串中是否包含字符串，返回的是下标值；如果不存在，返回报错异常

# print(e.startswith('h'))
# print(e.endswith('o'))  # 检测字符串是否以x开始，或结尾，返回结果为：true false

# print(e.lower())
# print(e.upper())  # 将字符串全部转换为小写 or 大写

# 【5】切片实践
f = 'Hello XiaoXiaoChen'
# slice [start:end:step]
# print(f)
# print(f[2])
# print(f[1:5:1])  # 取1-5下标中的数据
# print(f[1::1])  # 取1下标，及之后的数据
# print(f[::-1])  # step为负，倒序输出；负号表示方向，从右往左去遍历


