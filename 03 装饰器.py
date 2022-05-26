# -*- coding: utf-8 -*-
# @Time : 2022/2/11 16:25
# @Author : O·N·E
# @File : 03 装饰器.py
"""
装饰器:decorator
    本职：函数闭包(funtion closure)的语法糖(syntactic sugar)
        函数闭包:funtion closure
        语法糖:syntactic sugar
"""
# demo 函数闭包：funtion closure
"""
下面的主体函数(查找奇数)和计算时间函数耦合在一起
缺点:不方便修改，容易引起bug
"""

# demo1:2个功能紧紧关联在一起
import time


# def print_data():
#     """
#     输出1-100之间的全部奇数
#     """
#     start_time = time.perf_counter()
#     for i in range(1, 100):
#         if i % 2 == 1:
#             print(i, end=" ")
#     end_time = time.perf_counter()
#     print(end_time - start_time)
#
#
# print_data()


# demo2:将2个功能进行解耦 分开写
# def count_time(fun):  # 单独计算时间函数 将函数传入里面
#     start_time = time.perf_counter()
#     fun()
#     end_time = time.perf_counter()
#     print(end_time - start_time)
#
#
# def print_data():
#     """
#     输出1-100之间的全部奇数
#     """
#     for i in range(1, 100):
#         if i % 2 == 1:
#             print(i, end=" ")
#     print()
#
#
# count_time(print_data)


# 虽然上述写法的可读性强，但是写法上不是很好，在书写时候一般都是传入函数主程序，隐藏辅助函数，不会传入隐藏函数。既首选传入主程序同时也会
# 一并带着辅助程序进行运行

# demo3 引入闭包
# 闭包函数
# 函数闭包：一个函数，其参数和返回值都是函数
#         用于增强函数功能
#         面向切面编程

# def fun_wrapper(fun):
#     def count_time():
#         start_time = time.perf_counter()
#         fun()
#         end_time = time.perf_counter()
#         print(end_time - start_time)
#
#     return count_time
#
#
# def print_data():
#     """
#     输出1-100之间的全部奇数
#     """
#     for i in range(1, 100):
#         if i % 2 == 1:
#             print(i, end=" ")
#     print()
#
#
# if __name__ == '__main__':
#     # 增强函数
#     fun = fun_wrapper(print_data)
#     fun()

# demo4 调用函数不用每次都要写增强函数

# def fun_wrapper(fun):
#     def count_time():
#         start_time = time.perf_counter()
#         fun()
#         end_time = time.perf_counter()
#         print(end_time - start_time)
#
#     return count_time
#
#
# @fun_wrapper
# def print_data():
#     """
#     输出1-100之间的全部奇数
#     """
#     for i in range(1, 100):
#         if i % 2 == 1:
#             print(i, end=" ")
#     print()
#
#
# if __name__ == '__main__':
#     print_data()

# demo5 装饰器面试题
def wrapper1(fun1):
    print("set 1")

    def print1():
        print("call 1")
        fun1()

    return print1


def wrapper2(fun2):
    print("set 2")

    def print2():
        print("call 2")
        fun2()

    return print2


@wrapper1
@wrapper2
def print_():
    pass


if __name__ == '__main__':
    # print_ = wrapper2(print_)
    # print(print_.__name__)
    # print_ = wrapper1(print_)
    # print(print_.__name__)

    print_()
    print("-----")
    print_()  # 只会增强一次
