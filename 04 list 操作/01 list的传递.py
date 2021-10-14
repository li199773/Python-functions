# -*- coding: utf-8 -*-
# @Time : 2021/10/11 10:57
# @Author : O·N·E
# @File : 01 list的传递.py

Empty_list = []


def name(names):
    age = 24
    for name in names:
        print("我的名字是{},年龄是{}".format(name, age))


def demo2(names):
    while names:
        pop = names.pop()  # pop 函数可以从最后一个向第一个进行输出
        print("从右向左名字为:{}".format(pop))
        Empty_list.append(pop)
    print(Empty_list)


def demo3(*toppings):  # 用*toppings进行查看函数传递的所有参数
    print(toppings)


if __name__ == '__main__':
    # name(["li", "zhao", "wang"])
    demo2(["li", "zhao", "wang"])
    demo3('li')
