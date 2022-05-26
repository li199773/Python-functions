# -*- coding: utf-8 -*-
# @Time : 2022/2/11 10:52
# @Author : O·N·E
# @File : 02 生成器.py
"""
生成器generator：
    自己写得能够实现迭代器的函数
    1.生成器函数
    2.生成器表达式
"""


# 1.生成器函数
# demo1
class Product():
    def fun1(self):
        for i in range(10):
            # print("正在生产第{}份".format(i))
            yield "正在生产第{}份".format(i + 1)


product = Product().fun1()
print(product.__next__())
print(product.__next__())
print(product.__next__())


def fun2():
    for i in range(10):
        # print("正在生产第{}份".format(i))
        yield "正在生产第{}份".format(i + 1)


a = fun2()
print(a.__next__())
print(a.__next__())
print(a.__next__())

# demo2
# 生成器生成不大于max的偶数
print("*" * 100)


def generator_data(max):
    for i in range(1, max + 1):
        if i % 2 == 0:
            yield i
            # return i

print(generator_data(10))
for i in generator_data(10):
    print(i, end=" ") # 跟return进行区别
# 2.生成器表达式
a = ["学生{}".format(i + 1) for i in range(10)]
print(a)

a = ("学生{}".format(i + 1) for i in range(10))
print(a)  # <generator object <genexpr> at 0x00000228733D3D60> 生成器表达式
# 可以按照生成器的语法进行调用

print(next(a))
print(next(a))
print(next(a))
print(a.__next__())
print(a.__next__())
print(a.__next__())  # 两种方法 都可以使用


# 作用
# 1.延迟计算，减少内存的占有
# print(sum([i for i in range(100000000)]))
# print(a)  # 内存占有太严重，程序容易崩溃,程序会把所有的数字先放到一个列表里面然后在进行计算

# a = (i for i in range(100000000))  # 使用生成器的话几乎不占用内存
# a = [i for i in range(100000000)]


# 2.提高代码的可读性


# demo
def demo():
    for i in range(4):
        yield i


g = demo()
g1 = (i for i in g)
g2 = (i for i in g1)

print(g1)
print(g2)
print(list(g1))
print(list(g2))

# 生成器只能使用一次
generator_data = (i * i for i in range(10))
for i in generator_data:
    print(i, end=" ")
print("*" * 10)
for i in generator_data:
    print(i, end=" ")  # 第二次调用的话无显示结果
