# -*- coding: utf-8 -*-
# @Time : 2022/2/10 11:17
# @Author : O·N·E
# @File : 01 ElasticSearch介绍 迭代器.py
"""
迭代器：iterator
"""
import time

# demo1
list = [1, 2, 3, 4, 5, 6]
for i in list:
    print(i)  # 可以被正常的输出

# demo2
# for i in 123456:
#     print(i)  # 报错 TypeError: 'int' object is not iterable 该类型不可以被迭代
# iterable 迭代的
# 证明以下的类型是可以被迭代的
from collections.abc import Iterable

list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)
dict = {"a": 1, "b": 2}
set_ = {1, 2, 3, 4, 5}

print(isinstance(list, Iterable))
print(isinstance(tuple, Iterable))
print(isinstance(dict, Iterable))
print(isinstance(set_, Iterable))

# 可迭代协议
print(dir([1, 2]))  # __iter__
print(dir((1, 2)))  # __iter__ 集合是无序的

print(dir([1, 2].__iter__()))  # 列表迭代器
# 方法对比(增加的方式)
print(set(dir([1, 2].__iter__())) - set(dir([1, 2])))  # {'__setstate__', '__next__', '__length_hint__'}

# 迭代器函数iter和next
list = [1, 2, 3]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # 报错

# while循环
l_ = [1, 2, 3, 4, 5, 6]
it_l = iter(l_)

while True:
    try:
        print(next(it_l))
    except StopIteration:
        break
# 迭代器必须遵循的协议:必须要有__iter__()和__next__()方法才可以
# __iter__()将可迭代对象变成迭代器
# __next__()将迭代器进行取值

# range()是否是迭代器
print(dir(i for i in range(1, 6)))  # __iter__ 同样子也有
print(isinstance((i for i in range(1, 6)), Iterable))

# 迭代器的优势:
"""
    现在有for方法的情况下为什么还需要使用迭代器?
    for 方法是对迭代器的一种方法封装，假如对列表数据进行处理需要对列表数据进行遍历在处理
    迭代器的话是直接进行取值，按照next方法一个一个进行取值，调用next方法的话才会进行取值
"""


# 时间效率对比
# start_time = time.time()
# for i in range(10000000):
#     print(i, end=" ")
# end_time = time.time()  # 83.00707030296326
#
# start_time = time.time()
# list = [i for i in range(10000000)]
# it = iter(list)
# for i in it:
#     print(i, end=' ')
# end_time = time.time()  # 82.19881129264832
# print(end_time - start_time)


# # 文本文档
# for line in open("01 ElasticSearch介绍 text.txt", encoding="utf-8"):
#     print(line)


# demo3 自己定义迭代器
# Fibonacci 一般
# a = 0
# b = 1
# c = int(input("请输入输入的Fibonacci个数:"))
# Fibonacci = []
#
# i = 0
# while i < c:
#     Fibonacci.append(a)
#     a, b = b, a + b
#     i += 1
# print(Fibonacci)


# 迭代器
# class Fibonacci(object):
#     """斐波那契数列得迭代器"""
#
#     def __init__(self, nums):
#         self.nums = nums  # 传入参数，生成斐波那契数列的个数
#         self.a = 0
#         self.b = 1
#         self.i = 0  # 用于记忆生成的个数
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         ret = self.a  # 记忆第一个数
#         if self.i < self.nums:
#             self.a, self.b = self.b, self.a + self.b
#             self.i += 1
#             return ret
#         else:
#             raise StopIteration  # 停止迭代
#
#
# nums = int(input("请输入需要生成Fibonacci数列项的个数："))
# fobo = Fibonacci(nums)
# for num in fobo:
#     print(num, end=" ")

# 自定义一个迭代器
class Student(object):
    def __init__(self):
        self.list = []
        self.currrent = 0

    def __iter__(self):
        return self

    def add(self):
        # 添加信息
        name = input("请输入学生的姓名:")
        age = input("请输入学生的年龄:")
        sex = input("请输入学生的性别:")

        dict = {}
        dict["name"] = name
        dict["age"] = age
        dict["sex"] = sex

        self.list.append(dict)

    def __next__(self):
        if self.currrent < len(self.list):
            ret = self.list[self.currrent]
            self.currrent += 1
            return ret
        else:
            self.currrent = 0
            raise StopIteration


student = Student()
student.add()
student.add()
print(next(student))
