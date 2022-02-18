# if-else 的嵌套使用
# 一个场景需要分阶段或者层次，做出不同的处理
# 要执行内部的 if 语句，一定要外部的 if 语句满足条件才可以
Score = int(input('请输入您的学分：'))
if Score > 10:
    Grade = int(input('请输入您的成绩：'))
    if Grade >= 80:
        print('恭喜您，可以升班了！')
    else:
        print('很遗憾，您的成绩不达标')
        pass
    pass
else:
    print('您的学分还不足 10 分，请继续努力！')