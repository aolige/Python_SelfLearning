# 递归满足的条件
# 1、自己调用自己
# 2、必须有一个明确的结束条件
# 优点：
# 1、逻辑简单、定义简单
# 缺点：
# 1、容易导致 栈（空间）溢出，内存资源紧张，甚至内存泄露


# 求阶乘
# 循环的方式实现
def jiecheng(a):
    result = 1
    for i in range(1,a+1):
        result *= i
        pass
    return result
    pass


# x = int(input('请输入您想求得几的阶乘？'))
# print('{}的阶乘值为：{}'.format(x,jiecheng(x)))

# 递归方式去实现阶乘

def diguiJc(b):
    '''
    递归方式实现阶乘
    :param b:
    :return:
    '''
    if b == 1:
        return 1
    else:
        return b*diguiJc(b-1)
    pass


# print(diguiJc(5))


# 【案例1】模拟实现树形结构的遍历

import os  # 引入文件操作模块


def findFile(file_Path):
    '''
    遍历文件路径下的所有文件
    :param file_Path:
    :return:
    '''
    listRs = os.listdir(file_Path)  # os.listdir得到该路径下所有的文件夹
    for file_item in listRs:
        full_path = os.path.join(file_Path,file_item)  # 获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是不是文件夹
            findFile(full_path)  # 如果是文件夹，则再次去递归
            pass
        else:
            print(file_Path,file_item)
            pass
    else:
        return
    pass


# 调用搜索文件函数findFile
findFile('E:\\桌面文件\\美景公司-工作文件')


# # 【案例1】模拟实现树形结构的遍历
#
# import os
# def Find_Files(file_name):
#     '''
#     递归查找目录下文件名
#     :param file_name:
#     :return:
#     '''
#     List_file = os.listdir(file_name)
#     for item_file in List_file:
#         file_path = os.path.join(file_name,item_file)
#         if os.path.isdir(file_path):
#             Find_Files(file_path)
#             pass
#         else:
#             print(file_path)
#     else:
#         return
#     pass
#
#
# Find_Files('G:\\迅雷下载')

