# 析构方法 __del__(self)
# 程序运行结束后，自动调用del函数，释放内存空间

class Animal(object):
    def __init__(self,name):
        self.name = name
        print('执行初始化实例')
        pass

    def __del__(self):
        print('执行对象删除操作')
        pass

    pass


Tiger = Animal('老虎')
print(Tiger.name)
del Tiger # 用del释放内存资源
# print(Tiger.name)



















