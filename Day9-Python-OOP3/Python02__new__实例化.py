


class Animal():
    def __init__(self):
        self.name = '大老虎'
        pass

    # 在python中，如果不重写__new__方法，，默认会调用如下创建实例方法
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
        pass

    pass


tiger = Animal()  # 实例化的过程会自动调用__new__() 去创建实例

