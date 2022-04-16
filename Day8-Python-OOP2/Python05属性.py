# 属性：类属性、实例属性
# 类属性——类对象所具有的属性
# 实例属性——实例对象具有的属性

# 小结：
# 类属性可以被类对象，实例对象共同访问
# 实例属性，只能由实例对象访问

class Student(object):
    # 属于类属性，是Student类对象所拥有的
    name = '李华'
    class1 = '一年级4班'

    def __init__(self, age, hobby):
        """
        __init__内定义的属性，为实例属性
        :param age:
        :param hobby:
        """
        self.age = age
        self.hobby = hobby
        pass

    pass


stu1 = Student(18, '唱歌')
print(stu1.name)  # 通过【实例对象】访问【类属性】
print(stu1.age)  # 通过【实例对象】访问【实例属性】
print('_______________________________________')
Student.name = '哈哈哈哈'  # 可以通过类对象，对类属性进行修改
print(Student.name)
# print(Student.age)
# 小结：
# 类属性可以被类对象，实例对象共同访问
# 实例属性，只能由实例对象访问











