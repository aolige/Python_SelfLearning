# 单分支：
# if 条件表达式（比较运算符、逻辑运算符、/符合的条件表达式）:
#     代码指令
#     。。。
# score = 40
# if score >= 60:     #满足条件就会输出该分支打印的提示
#     print('成绩及格！')
#     pass #空语句
# print("输出结尾")


#双分支：
# if 条件表达式（比较运算符、逻辑运算符、/符合的条件表达式）:
#     代码指令
#     。。。
# else:
#     代码指令
#     。。。
# score = int(input('请输入您的成绩：'))
# if score >= 60:  #True时执行
#     print("您的成绩合格！")
#     pass
# else:            #False时执行
#     print("您的成绩不合格，请继续加油！")
#     pass
# print('分支流程结束。')



#多分支：
# if 条件表达式（比较运算符、逻辑运算符、/符合的条件表达式）:
#     代码指令
#     。。。
# elif 条件表达式:
#     代码指令
#     。。。
# elif 条件表达式:
#     代码指令
#     。。。
# 。。。
# else:  （此处为选配，不一定有）
#     代码指令
#     。。。
# 特征：
# 1、只要满足其中一个分支，就会退出本层if语句结构【必定会执行其中一个分支】
# 2、至少有两种情况可以选择
# 3、elif后面必须得写上条件 和 语句
# 4、else是选配，根据实际的情况来编写
# score = int(input("请输入您的分数查询等级："))
# print(type(score))
# if 60 <= score < 80:
#     print('您的成绩等级为：下等')
#     pass
# elif 80<=score<90:
#     print('您的成绩等级为：中等')
#     pass
# elif 90<=score:
#     print('您的成绩等级为：优秀')
#     pass
# else:
#     print('您的成绩不合格，还需要多多努力哦！')
# print('成绩等级查询程序运行结束！')


# 多分支，多条件的练习
# 猜拳机 小游戏
#石头 剪刀 布

# 【while打印等腰三角形】
count = 1
while count <= 10:
    space = 1
    while space <= 10-count:
        print("@",end=" ")
        space += 1
        pass
    star = 1
    while star <= count*2-1:
        print("*",end=" ")
        star += 1
        pass
    print()
    count += 1
    pass