# Python-Common-functions
# 本章主要介绍常用的有关Python函数
## 01 `glod`函数
### 相关问题：获取文件的路径，还可以获取文件夹下子文件中文件的相关路径。
### 介绍：
        # glod使用：获取文件的路径
        *：代表多个字符
        ?:代表一个字符
        []匹配指定范围内的字符，如[0-9]匹配数字
        **/*.txt 这个经常使用，可以深入子目录下面的目录中去。
## 02 `dict`用法:`defaultdict`
### 相关介绍：
### 1.合并相同键值的字典
        # 使用collections模块中的defaultdict来构造的字典
        l = [('a', 2), ('b', 3), ('a', 1), ('b', 4), ('a', 3), ('a', 1), ('b', 3)]
        d = defaultdict(list) # 输出defaultdict(<class 'list'>, {'a': [2, 1, 3, 1], 'b': [3, 4, 3]}) 将相同键进行合并
### 2.输出键值：
        for x, y in dict.items(): # item用法，只输出键：直接循环即可，输出值使用.values()函数。
## 3.`Class`类和对象
### 相关定义：类(Class)用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
### 相关介绍：
#### 1.类的私有变量
        people = People("li", 24, 60) # 传入参数，直接调用即可
        people.funtion()
        people.funtion1() 
#### 2.类的单层继承
        class Student(People):  # student 继承上面的People这个类,People为父类，student为子类
#### 3.累的多层继承
        class Topic(Student, Speaker): # 创建子类Topic，继承Student, Speaker的父类
        # 及时子类Topic没有funtion2，但是父类Student, Speaker有funtion2，同样可以进行调用。
