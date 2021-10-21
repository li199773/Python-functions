# -*- coding: utf-8 -*-
# @Time : 2021/10/15 16:40
# @Author : O·N·E
# @File : 02 map()函数.py
"""
map()的原型是map(function, iterable, …)，它的返回结果是一个列表。
参数function:传的是一个函数名，可以是python内置的，也可以是自定义的。就像上面的匿名函数lambda
参数iterable:传的是一个可以迭代的对象，例如列表，元组，字符串这样的。
这个函数的意思就是将function应用于iterable的每一个元素，结果以列表的形式返回。
"""

"""把名字首先大写然后传入空列表中进行输出"""
# 方式一:直接循环插入即可
names = ['tom', 'li', 'zhao']
empty_list = []  # 建立一个空列表
for name in names:
    empty_list.append(name.title())  # 将每个名字的第一个字母大写，然后插入到列表中
print(empty_list)
# 方式二:map()与lambda()结合使用
arr = list(map(lambda x: x.title(), names))
print(arr)

"""根据输入的数字输出平方值"""


# demo1
def mul(n):
    return n * n


numbers = [1, 2, 3, 4, 5]
result = list(map(mul, numbers))
print(result)
# demo2
# 匿名函数
print(list(map(lambda n: n * n, [1, 2, 3, 4, 5])))
"""
iterable后面可以传很多个iterable，如果有额外的iterable参数，并行的从这些参数中取元素，并调用function。
如果一个iterable参数比另外的iterable参数要短，将以None扩展该参数元素。
"""


# demo1
def add(x, y, z):
    return x * y * z


list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 3]
res = list(map(add, list1, list2, list3))
print(res)  # 加很多的实施并行：既1+1+1,2+2+2,3+3+3这样子


# demo2
def add(x, y, z):
    return x, y, z


list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]
list3 = [1, 2, 3, 4, 5]
res = list(map(add, list1, list2, list3))
print(res)

print([i for i in range(10)])
