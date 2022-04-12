# # 序列操作： str tuple元组 list
#
# # all() result:bool 对象中的元素：除了是0、空、false 外 都算TRUE
# print(all([]))
# print(all(()))
# print(all([1,23,4,0]))
#
# # any() result:bool 对象中有一个元素为True，则返回值为True
# print(any((1,0,False)))
#
#
# # sort、sorted 排序，
# # sort排序，只能排序列表，并且是在原有列表上修改
# # sorted可以排序列表，元组，不会修改原有的序列
# li = [1,2,3,4,5,6,7,8,9]
# print(sorted(li,reverse=False))
# print(sorted(li,reverse=True))
# print(li)
#
# print('sort排序之后，修改的是原始对象，生成的是新list')
# li.sort(reverse=True)
# print(li)
#
# # reverse 反转序列中的元素
#
# # range()函数可以创建一个整数列表，一般用于for循环中
# # range(起始值，结束值，步长)
#
# # zip() 用来打包数据的,根据相同索引实现打包
# li1 = ['a','b','c','d','e','f']
# li2 = [1,2,3,4,5]
# li3 = [1,2,3,4,5,6]
# print(list(zip(li1,li2,li3)))



def BookInfo():
    '''
    使用zip打包信息
    :return:
    '''
    books=[]
    id = input('请输入编号，每项以空格分隔：')
    bookname = input('请输入书名，每项以空格分隔：')
    bookpostion = input('请输入位置，每项以空格分隔：')
    # 以空格分隔
    idList = id.split(' ')
    booknameList = bookname.split(' ')
    bookpostionList = bookpostion.split(' ')
    # 使用zip打包编号、书名、位置
    BookzipInfo = zip(idList,booknameList,bookpostionList)
    for i in BookzipInfo:
        '''
        遍历图书信息进行存储
        '''
        dictInfo = {'编号':i[0],'书名':i[1],'位置':i[2]}
        books.append(dictInfo)
        pass
    for j in books:
        print(j)
    pass

# BookInfo()


# enumerate()   枚举函数
# 用于将一个可遍历的数据对象（如：列表、元组、字符串）组合为一个索引序列
# 同时列出数据和数据下标，一般用于for循环中

listObj = ['a','b','c','d']
# print(enumerate(listObj))
# for index,item in enumerate(listObj,1):
#     print(index,item)
dicObj = {}
dicObj['name'] = '张三'
dicObj['hobby'] = '唱歌'
dicObj['sex'] = '男'
print(dicObj)
for index,item in enumerate(dicObj,0):
    print(item)


