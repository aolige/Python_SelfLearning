# 【例1：猜拳机 小游戏】
# 石头:0 剪刀:1 布:2
# import random
# times = 0
# while times <= 10:
#     people = int(input("请出拳【石头:0 剪刀:1 布:2】："))
#     if people != 0 and people != 1 and people != 2:
#         print('请按照游戏规则出拳!')
#         break
#         pass
#     computer = random.randint(0,2)
#     print('电脑出拳：%d'%computer)
#     if people == computer:
#         print('平局')
#         pass
#     elif people == 0 and computer == 1:
#         print('您赢了电脑')
#         pass
#     elif people == 1 and computer == 2:
#         print("您赢了电脑")
#         pass
#     elif people == 2 and computer == 0:
#         print("您赢了电脑")
#         pass
#     else:
#         print('您输给了人机~')
#         pass
#     times += 1
#

# 【例2：while打印99乘法表】
# hang = 1
# while hang<=9:
#     lie = 1
#     while lie<=hang:
#         print('%d*%d=%d'%(lie,hang,hang*lie),end=' ')
#         lie += 1
#         pass
#     print()
#     hang += 1
#     pass

# 【例3：for打印99乘法表】
# for hang in range(1,10):
#     for lie in range(1,hang+1):
#         print("%d*%d=%d"%(lie,hang,hang*lie),end=" ")
#         pass
#     print()
#     pass

# 【例4：while打印直角三角形】
# hang = 1
# while hang<=5:
#     lie = 1
#     while lie<=hang:
#         print("*",end=" ")
#         lie +=1
#         pass
#     print()
#     hang += 1
#     pass

# 【例4：while打印等腰三角形】
# count_paishu = 1  # 打印的排数量
# while count_paishu<=10:
#     i = 1
#     while i<=10-count_paishu:
#         print("@",end=" ")
#         i += 1
#         pass
#     j = 1
#     while j <= 2*count_paishu-1:  # 每排打印*的个数为，（2*当前排数-1）
#         print("*",end=" ")
#         j += 1
#         pass
#     print()
#     count_paishu += 1
#     pass

# 【例5：求1-100的累加和】
# sum = 0
# for i in range(1,101):
#     sum += i
#     pass
# print("%d"%sum)

# 【例6：求1-100的偶数累加和,和奇数累加和分别为】
# sum_oushu = 0
# sum_jishu = 0
# for i in range(1,101):
#     if i%2==0:
#         sum_oushu += i
#         pass
#     else:
#         sum_jishu += i
#         pass
#     pass
# print('偶数和为%d:'%sum_oushu)
# print('奇数和为%d:'%sum_jishu)


# 【例7：猜年龄小游戏】
# 猜年龄小游戏,有三点需求
# 1.允许用户最多尝试3次
# 2.每尝试3次后，如果还没猜对，就问用户是否还想继续玩，
# 如果回答Y或y,就继续让其猜3次，以此往复，如果回答N或n，就退出程序
# 3.如何猜对了，就直接退出

# age = 25
# count = 1
# while count <= 3:
#     guess_Age = int(input("猜猜我今年多少岁啦："))
#     if guess_Age == age:
#         print("恭喜您，猜对啦！")
#         break
#         pass
#     elif guess_Age > age:
#         print("猜大了，请往小了猜~")
#         pass
#     elif guess_Age < age:
#         print("猜小了，请往大了猜~")
#         pass
#     count += 1
#     if count > 3:
#         play = input('您已经猜错三次了，是否还想继续玩？【是：Y/y，否：N/n】：')
#         if play == 'Y' or play == 'y':
#             print('已为您增加3次游戏机会~')
#             count = 1
#             pass
#         elif play == 'N' or play == 'n':
#             print('游戏结束~')
#             break
#             pass
#         else:
#             print('您未按照游戏规则输入，已退出游戏~')
#         pass

# 【例8：计算BIM指数】
# 小王身高1.75，体重80.5kg。
# 请根据BMI公式（体重除以身高的平方）帮小王计算他的BMI指数
# 并根据BMI指数:
# 低于18.5过轻
# 18.5-25:正常
# 25-28:过重
# 28-32:肥胖
# 高于32:严重肥胖
count = 1
while count <= 10:
    height = float(input("请输入您的身高/m："))
    weight = float(input("请输入您的体重/kg："))
    BMI = weight/height**2
    if BMI < 18.5:
        print("过轻")
        pass
    elif 18.5 <= BMI < 25:
        print("正常")
        pass
    elif 25 <= BMI < 28:
        print("过重，要减肥了")
        pass
    elif 28 <= BMI < 32:
        print("肥胖，请注意控制饮食！")
        pass
    elif BMI >= 32:
        print("严重肥胖")
        pass
    count += 1


