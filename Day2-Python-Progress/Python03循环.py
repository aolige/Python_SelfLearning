# 循环的分类
# while使用，适用于对未知的循环次数，用于判断
# for使用：适用于已知的循环次数【可迭代对象遍历】

# 【while 循环】，基本语法结构
# while 条件表达式：
#     代码指令

# 语法特点：
# 1、有初始值
# 2、条件表达式
# 3、【循环体内计数变量】为：自增 或 自减，否则会造成死循环
# 使用条件：循环的次数不确定，是依靠循环条件来结束
# 目的：为了将相似或者相同的代码操作变得更加简洁，使代码可以重复利用

# 【案例1】输出1-100之间的数据
# a = 1
# while a < 100:
#     print(a)
#     a += 1
#     pass

# 【案例2】改进-猜拳机 小游戏
# 石头：0 剪刀：1 布：2
# import random # 直接导入产生随机数的模块
# # 变量：计算机  人
# count = 1
# while count<=10:
#     People = int(input('请出拳：[0:石头 1:剪刀 2:布]'))
#     Computer = random.randint(0,2)
#     print('电脑出的是：%d'%Computer)
#     if People==0 and Computer==1:
#         print('你赢了！')
#         pass
#     elif People==1 and Computer==2:
#         print('你比电脑厉害')
#         pass
#     elif People==2 and Computer==0:
#         print('你赢过了电脑')
#         pass
#     elif People==Computer:
#         print('平局')
#         pass
#     else:
#         print('你没干过电脑哦')
#         pass
#     count += 1

# 【案例3】while打印九九乘法表
# hang = 9 #行
# while hang>=1:
#     lie = 1 #列
#     while lie<=hang:
#         print('%d*%d=%d'%(hang,lie,hang*lie),end=' ')
#         lie += 1
#         pass
#     print()
#     hang -= 1
#     pass

# # 【案例4】while打印直角三角形
# row = 10 # 行
# while row>=1:
#     a = 1 #列
#     while a<=row:
#         print('*',end=" ")
#         a += 1
#         pass
#     print()
#     row -= 1

# 【拓展练习】while打印等腰三角形
# row = 1
# while row <= 10:
#     j = 1
#     while j <= 10-row:  # 控制打印空格个数
#         print(' ',end="")
#         j += 1
#         pass
#     k = 1
#     while k <= 2*row-1: #控制打印*号
#         print("&",end="")
#         k += 1
#         pass
#     print()
#     row += 1


# 【for循环】
# 语法特点：遍历操作，依次的取集合容器中的每个值
# for 临时变量 in 容器:
#     执行代码块

# tages = '我的名字叫刘浪' #字符串类型本身就是一个字符类型的集合
# for item in tages:
#     print(item)
#     pass

# 【range:此函数可以生成一个数据集合列表】
# range(起始值：结束：步长)   步长不能为零
# sum = 0
# for data in range(1,101):
#     sum += data # 求累加和
#     pass
# print('1-100累加和为：%d'%sum)


# print('-----------------for的使用----------------')
# 【求0-100之间偶数的累加和】
# sum = 0
# for data in range(0,101):
#     if data%2==0:
#         sum += data
#         pass
#     pass
# print('0-100之间的偶数累加和为：%d'%sum)

# 【for打印九九乘法表】
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end=" ")
        pass
    print()
    pass


# 【break和continue】
# break 代表中断 结束，满足条件直接结束本层循环
# continue:结束本次循环，继续进行下次循环（满足continue条件，
# 本次循环剩下的语句将不再执行，后面的循环继续）
# 这两个关键字只能用在循环中

# 【例1：break】
# sum = 0
# for item in range(1,50):
#     #如果累加和>100,停止
#     if sum > 100:
#         print('当前执行到%d就停止了'%item)
#         break #退出循环系统
#         pass
#     sum += item
#     pass
# print('当前累加和为：%d'%sum)

# 【例2：continue】
# for item in range(1,100):
#     if item%2==0: # 遇到偶数不打印
#         continue
#         pass
#     print(item)
#     pass

# for item in 'I LOVE XIAOXIAOCHEN':
#     # if item == 'O':
#     #     break # 彻底中断循环
#     #     pass
#     if item == ' ':
#         continue # 跳过该层循环，下一个循环继续
#         pass
#     print(item)