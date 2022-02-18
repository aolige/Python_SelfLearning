# 【作业1：猜年龄小游戏】
# count = 0
# age = 15
# while count < 3:
#     guess_age = int(input("猜猜我的年龄："))
#     if guess_age == age:
#         print("恭喜您，猜对啦！")
#         break
#         pass
#     elif guess_age > age:
#         print("您猜大啦，请再试试~")
#         pass
#     else:
#         print("您猜小啦，请再试试~")
#         pass
#     count += 1
#     if count == 3:
#         play = input("您已经猜错3次啦，是否还想继续？【是：Y/y，否：N/n】:")
#         if play == 'Y' or play == 'y':
#             print('请您继续猜~')
#             count = 0 # 次数重置为初始值
#             pass
#         elif play == 'N' or play == 'n':
#             print('您已经退出游戏~')
#             break
#             pass
#         else:
#             print("请输入正确的指令，谢谢配合！")
#             pass


# 【作业2：计算BMI指数】BMI=weight/(height*height)
times = 0
while times <= 10:  # 循环执行10次
    height = float(input("请输入您的身高/m："))
    weight = float(input("请输入您的体重/kg："))
    BMI = float(weight / (height * height))
    print('您的BMI指数为：%.2f'%BMI)  # %.2f 表示取float浮点型的2位小数
    if BMI<=18.5:
        print('过轻')
        pass
    elif 18.5<=BMI<= 25:
        print('正常')
        pass
    elif 25<BMI<=28:
        print('过重')
        pass
    elif 28<BMI<=32:
        print('肥胖')
        pass
    elif BMI>32:
        print('严重肥胖')
        pass
    times += 1