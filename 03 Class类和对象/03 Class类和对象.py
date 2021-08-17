class Person:
    name = "li"
    age = 20

    # 类的构造：
    def __init__(self):
        # 构造器
        print("我爱中国")

    # 都没有形参的
    def funtion(self):
        print("中国爱我")


# 类的实例化：
person = Person()  # 首先进行输出构造函数的值
# print(person.name)
# print(person.age)
person.funtion()


# 2.类的私有变量：
class People:

    def __init__(self, name, age, weigth):
        self.name = name
        self.age = age
        self.__weight = weigth

    def funtion(self):
        print("%s年龄是%s" % (self.name, self.age))

    def funtion1(self):
        print("%s的体重是%s千克" % (self.name, self.__weight))


# people = People("li", 24, 60)
# people.funtion()
# people.funtion1()

# 3.类的继承：单层继承
# 继承上面的people类
class Student(People):  # student 继承上面的People这个类,People为父类，student为子类

    def __init__(self, name, age, weight, grade):
        # 调用父类
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 覆写父类的方式：
    def funtion(self):
        print("%s年龄是%s,%s" % (self.name, self.age, self.grade))


student = Student("li", 24, 60, "研究生一年级")
student.funtion()


# 2 super() 单层继承
class Reader(People):
    def __init__(self, name, age, weigth):
        super().__init__(name, age, weigth)


reader = Reader("zhao", 24, 55)
reader.funtion()
reader.funtion1()


# 4.多重继承：
class Speaker():
    def __init__(self, topic):
        self.topic = topic

    def funtion2(self):
        print("我演讲的主题是%s" % self.topic)


# speaker = Speaker("我爱中国")
# speaker.funtion2()

# 创建子类Topic，继承Student, Speaker的父类
class Topic(Student, Speaker):
    def __init__(self, name, age, weight, grade, topic):
        Student.__init__(self, name, age, weight, grade)
        Speaker.__init__(self, topic)

    def funtion3(self):
        print("%s年龄是%s,%s,演讲的主题是%s" % (self.name, self.age, self.grade, self.topic))


topic = Topic("li", 24, 60, "硕士一年级", "我爱中国")
topic.funtion3
# 及时子类Topic没有funtion2，但是父类Student, Speaker有funtion2，同样可以进行调用
topic.funtion2()
