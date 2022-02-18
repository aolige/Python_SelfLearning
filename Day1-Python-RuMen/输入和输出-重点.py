#输入和输出
#输出 %占位符,%s，代表字符串占位，%d代表数字占位

'''
Name = '小牛'
HomeTown = '四川资阳'
Age = 25
print('我的名字是：%s，来自：%s,今年%d岁了'%(Name,HomeTown,Age))

#\n换行效果
print('我要换行\n测试')
'''

# 以下为输出练习
# 姓名：刘浪
# # QQ：879029518
# # 手机号：18190283818
# # 公司地址：成都美景舒适家客服服务中心
# Name = '刘浪'
# QQ_Num = '879029518'
# Phone_Num = '18190283818'
# Company_Add = '成都美景舒适家客服服务中心'
# Age = 25
# print('----------------直接拼接-----------------')
# print('姓名：'+Name+'\n''QQ：'+QQ_Num+'\n''手机号：'+Phone_Num+'\n''公司地址：'+Company_Add)
# print('----------------%s占位符拼接-----------------')
# print('年龄：%s'%Name)
# print('QQ：%s'%QQ_Num)
# print('手机号：%s'%Phone_Num)
# print('公司地址：%s'%Company_Add)
# print('-----------------.format()拼接----------------')
# print('姓名：{}，年龄：{}'.format(Name,Age))
# print('QQ：{}'.format(QQ_Num))
# print('手机号：{}'.format(Phone_Num))
# print('公司地址：{}'.format(Company_Add))
# print('-------------------结尾--------------')



#以下为输入练习
#input的练习
Name = input('请输入您的姓名：')
Age = int(input('请输入您的年龄：'))#转换输入的str类型数据，为int类型
QQ_Num = input('请输入您的QQ号：')
Phone_Num = input('请输入您的手机号：')
Company_Add = input('请输入您的公司地址：')

print('姓名：{}，年龄：{}'.format(Name,Age))
print('QQ：{}'.format(QQ_Num))
print('手机号：{}'.format(Phone_Num))
print('公司地址：{}'.format(Company_Add))