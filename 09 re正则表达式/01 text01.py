# -*- coding: utf-8 -*-
# @Time : 2021/12/6 16:33
# @Author : O·N·E
# @File : 01 ElasticSearch介绍 text01.py
import re

# re的语法规则
s = 'adds231f'
temp_list1 = re.match("[0-9]", s)
temp_list2 = re.search("[0-9]", s)
temp_list3 = re.findall("[0-9]", s)
print(temp_list1)  # re.math 从头开始匹配，没有匹配到返回None
print(temp_list2)  # re.seach 匹配包含，，没有匹配到返回None
print(temp_list3)  # re.findall 把所有匹配到的字符，以列表的形式返回，没有匹配到返回空列表[]
# math、seach匹配到后返回的是一个对象，若要获取匹配到的值要取greap()
print(temp_list2.group())
print(type(temp_list3))

# 常用的re表达式
line = "this hdr-biz 123 model server 456"
pattern = r"123"
matchObj = re.match(pattern, line)
print(matchObj)

# 全局匹配,失败返回None
line = "this hdr-biz model server"
pattern = r"hdr-biz"
m = re.findall(pattern, line)
print(m)

# demo
with open("01 text.txt", encoding='utf-8') as fp:
    for line in fp:
        name, age, tel = line.split()
        if tel.startswith('2'):
            print(tel)
