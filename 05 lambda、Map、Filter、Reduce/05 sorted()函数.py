# -*- coding: utf-8 -*-
# @Time : 2021/11/3 22:16
# @Author : O·N·E
# @File : 05 sorted()函数.py
"""
sorted()作为 Python 内置函数之一，其功能是对序列（列表、元组、字典、集合、还包括字符串）进行排序。
sorted()函数的基本语法格式如下：
list=sorted(iterable, key=None, reverse=False)
其中，iterable 表示指定的序列，key 参数可以自定义排序规则；reverse 参数指定以升序（False，默认）还是降序（True）进行排序。
sorted() 函数会返回一个排好序的列表。
"""
# 普通排序
a = [5, 4, 3, 2, 1]
print(sorted(a))  # 默认情况下是从小向大进行排列
# 绝对值排列
a = [-5, 0, 1, -2, -3]
print(sorted(a, key=abs))
print(a)  # 按照绝对值的大小进行排列原始的数据，原始的数据并不会进行改变
# 字典进行排列
a = {
    4: 1,
    5: 2,
    3: 3,
    2: 6,
    1: 8
}

print(sorted(a.items()))  # 按照字典的key进行排序
# 降序排序
a = [1, 2, 3, 4, 5]
print(sorted(a, reverse=True))
# 使用lambda进行组合使用
a = ['55555', '4444', '333', '22', '1']
print(sorted(a, key=lambda x: len(x), reverse=True))  # 按照长度的大小进行降序排列

student_tuples = [
    ('John', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# 按照学生的年龄进行降序排序
"""方式一"""
print(sorted(student_tuples, key=lambda x: x[2], reverse=True))
"""方式二"""
# 引入operator模块 更为简介
import operator

print(sorted(student_tuples, key=operator.itemgetter(2), reverse=True))
# 按照学生名字进行排序
print(sorted(student_tuples, key=lambda y: y[0]))  # 大写字母的顺序在小写字母的前面
# 上述的条件下忽略大小写进行排序
print(sorted(student_tuples, key=lambda z: z[0].lower()))
