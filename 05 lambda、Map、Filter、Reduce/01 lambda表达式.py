# -*- coding: utf-8 -*-
# @Time : 2021/10/14 15:46
# @Author : O·N·E
# @File : 01 lambda表达式.py
"""
介绍：
    lambda表达式是python中一种快递定义单行的表达式
    lambda表达式可以在任何需要函数的地方。
    它只是一个表达式，所以函数体比def简单很多，主题其实是一个表达式，不是一个完整的代码块，因此在lambda中无法写复杂的
    逻辑控制，lambda表达式拥有自己的命名空间，并且不能访问自己参数之外的参数。
"""
# lambda形式：冒号前面是传入的参数，后面是想要输出的值
a = lambda x, y, z: y
print(a(4, 5, 6))

# demo
a = lambda x, y: x if x > y else y
print(a(4, 3))


# lambda表达式与def之间的对比
def mul(x, y):
    return x * y


print(mul(3, 3))

m = lambda x, y: x * y
print(m(3, 6))

# 字符串的拼接功能
# demo1
str = lambda x, y, z: x + y + z
print(str("li", "love", "zhao"))
# demo2
s = "this is\na\ttest"  # 不加入r的话\n表示换行，加上r的话\n表示只是一个\和一个字母n
content = s.split()  # 什么不加的情况下，分割默认情况下分割:空格，换行符，TAB
print(''.join(s.split()))

# 与列表进行组合使用
lists = [lambda x: x ** 2, lambda x: x ** 4]
for list in lists:
    print(list(2))

# 实际的应用:主要是排序有很大的功能(xx,xx),(xxx,xxx,xxx)诸如多个元祖的排序
a = [(14, 5), (2, 0), (5, 9), (4, 4)]
a.sort(key=lambda x: x[1])
print(a)
# demo:将01数据集按照人口数量进行排序
countries = []
with open("01 database.txt", "r", encoding="utf-8") as fp:
    for line in fp:
        line = line.strip()
        arr = line.split(",")
        country = arr[1]
        capital = arr[3]
        population = int(arr[4])
        countries.append((country, capital, population))
"""
方式一：lambda表达式
"""
# countries.sort(key=lambda x: x[2]) #lambda表达式 参入参数X，传出x的第3项
"""
方式二：写一个函数进行返回第3项
"""


def get_countries(content):
    return content[2]


countries.sort(key=get_countries)

for content in countries:
    print(content)


# 函数的嵌套
def quadratic(a, b, c):
    return lambda x: a ** x + b * x + c


f = quadratic(2, 3, 4)
print(f(2))
print(quadratic(2, 3, 4)(2))  # 更为简洁
