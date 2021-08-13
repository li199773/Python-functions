from collections import defaultdict
from matplotlib import pyplot

# 使用 collections 模块中的 defaultdict 来构造这样的字典

l = [('a', 2), ('b', 3), ('a', 1), ('b', 4), ('a', 3), ('a', 1), ('b', 3)]

d = defaultdict(list)

for key, value in l:
    d[key].append(value)
print(d)
print(d['a'])
b = d['b']
print(b)
print(b[0])
print("*" * 100)

# dict字典取键值的方式
dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(dict)
# 逐个打印所有的键名：
for x in dict:
    print(x)
# 逐个打印所有键值对应的值:
# 方式一：
for y in dict:
    print(dict[y])
# 方式二：.values
for z in dict.values():
    print(z)
# 输出键值使用循环
for x, y in dict.items():
    # print(x)
    # print(type(x))
    # print(y)
    # print(type(y))
    print("{}+{}".format(x, y))


# dir的用法:可以展开可以使用的函数方法
x = dir(pyplot)
# print(type(x))
for i in x:
    if "xlim" in i:
        print("ylim在列表里面")

