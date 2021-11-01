# Python-Common-functions
# 本章主要学习常用的有关Python函数
## 01 `Try Exception`异常处理
### `python`里面异常处理，具体文件查看`READER.ME`文件
## 02 文件读取:`glod()`函数,`os.walk()`函数
### 02.01 `glod()`函数
### 相关问题：获取文件的路径，还可以获取文件夹下子文件中文件的相关路径。
### 介绍：
        # glod使用：获取文件的路径
        *：代表多个字符
        ?:代表一个字符
        []匹配指定范围内的字符，如[0-9]匹配数字
        **/*.txt 这个经常使用，可以深入子目录下面的目录中去。
### 02.02 os.walk()函数：可以遍历出指定路径下面的文件夹和文件内容
        for dirname in dir:  # 遍历指定文件夹下面的所有的文件夹名字
        print(os.path.join(root, dirname))
        for filename in files:
        print(os.path.join(root, filename))  # 遍历指定文件夹下面的所有的文件的名字
### 02.03 文件读写
#### 相关说明：
#### (1) open()文件写入
#### (2) csv()文件写入
#### (3) 文件的读取：全部读取；按行读取
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
#### 3.类的多层继承
        class Topic(Student, Speaker): # 创建子类Topic，继承Student, Speaker的父类
        # 及时子类Topic没有funtion2，但是父类Student, Speaker有funtion2，同样可以进行调用。
## 04 `list`操作：具体查看list文件夹
## 05 `lambda`表达式:包括`lambda`表达式，与`map()`函数，`filter()`函数，`reduce()`函数组合使用，具体查看lambda表达式文件夹。
