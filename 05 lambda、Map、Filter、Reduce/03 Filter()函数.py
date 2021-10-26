# -*- coding: utf-8 -*-
# @Time : 2021/10/18 16:35
# @Author : O·N·E
# @File : 03 Filter()函数.py
"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list()来转换。
接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
"""
# demo1:
# 方式一：筛选出大于5的数字
for i in range(10):
    if i > 5:
        print(i)
# 方式二:
numbers = [i for i in range(10)]
print(numbers)
numbers2 = range(10)
print(list(numbers2))
print(list(filter(lambda x: x > 5, numbers)))
"""filter() 类似一个for循环，但它是一个内置的函数，要比for更快"""


# demo2 传入数字，只保留奇数，删掉偶数
def Odd_number(n):
    if n % 2 == 1:
        return True
    else:
        return False


print(list(filter(Odd_number, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# demo3
"""如何认定学生是否偏科呢？符合如下其中一条的学生，将被视为偏科：
    有 2 科成绩在 80 分以上，有一科在 60 分以下。
    有 1 科成绩在 90 分以上，另外 2 科成绩都在 60 分以下。
    有 1 科成绩在 90 分以上，但三科的平均分在 70 分以下。
"""
scores = [("Emma", 89, 90, 59),
          ("Edith", 99, 49, 59),
          ("Sophia", 99, 60, 20),
          ("May", 40, 94, 59),
          ("Ashley", 89, 90, 59),
          ("Arny", 89, 90, 69),
          ("Lucy", 79, 90, 59),
          ("Gloria", 85, 90, 59),
          ("Abby", 89, 91, 90)]


def filter_socers(name_scores):
    score = sorted(name_scores[1:])
    if score[1] >= 80 and score[2] >= 80 and score[0] < 60:
        return True
    if score[2] >= 90 and score[0] < 60 and score[1] < 60:
        return True
    if score[2] >= 90 and sum(score) / len(score) < 70:
        return True
    else:
        return False


res = list(filter(filter_socers, scores))  # 将函数返回的值与列表的进行筛选
print(res)
