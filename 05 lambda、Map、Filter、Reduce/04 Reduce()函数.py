# -- coding: utf-8 --
# @Time : 2021/10/26 21:13
# @Author : O·N·E
# @File : 04 Reduce()函数.py
from functools import reduce

"""
reduce()作用：对序列中的元素进行积累，作用于这个列表的整体 map()是将定义的函数作用于列表的每个值
"""
# demo1 对传入的数据进行累加的操作
"""方式一：使用for循环"""
numbers = [1, 2, 3, 4]
num = 0
for number in numbers:
    num += number
print(num)
"""方式二:使用reduce"""


def res(x, y):
    return x + y


print(reduce(res, numbers))  # 这里不用加上list 计算过程 ((((1 + 2) + 3) + 4) + 5)
"""方式三 使用lambda进行整合"""
print(reduce(lambda x, y: x + y, numbers))

# demo 有初始值的情况下 假设初始值为5时 进行数值的累加
print(reduce(lambda x, y: x * y, [1, 2, 3], 5))  # 初始值默认情况下是None

# demo2 阶乘
print(reduce(lambda x, y: x * y, range(1, 6)))  # 输出5的阶乘

