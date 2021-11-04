# `lambda`表达式与`Map()`、`Filter()`、`Reduce()`使用，`sorted()`函数排序
## 01 `lambda`表达式
### 相关介绍：lambda表达式是`python`中一种快递定义单行的表达式。
#### 形式：
    lambda x, y, z: y # 冒号前面是传入的参数，后面是想要输出的值
#### (1) 与列表进行组合使用
    lists = [lambda x: x ** 2, lambda x: x ** 4]
    for list in lists:
        print(list(2))
#### (2) 排序有很大的功能(xx,xx),(xxx,xxx,xxx)诸如多个元祖的排序
    a = [(14, 5), (2, 0), (5, 9), (4, 4)]
    a.sort(key=lambda x: x[1])
    print(a) # 按照元祖里面的第二项进行排序
## 02 `map()`函数
### 相关介绍：`map()`的原型是`map(function, iterable, …)`，它的返回结果是一个列表。···表示可以传很多个列表。
    # 匿名函数
    print(list(map(lambda n: n * n, [1, 2, 3, 4, 5]))) # 根据传入的值输出其平方值，传入一个列表即可
    # 并行相加
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 3]
    res = list(map(add, list1, list2, list3))
    print(res)  # 加很多的实施并行：既1+1+1,2+2+2,3+3+3这样子
## 03 `filter()`函数
### 相关介绍：`filter()`函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象。接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
#### 1.选择筛选功能
    # 方式一：筛选出大于5的数字
    for i in range(10):
        if i > 5:
        print(i)
    # 方式二:
    print(list(filter(lambda x: x > 5, numbers))) # 如果要转换为列表，可以使用 list()来转换。
    filter() 类似一个for循环，但它是一个内置的函数，要比for更快
#### 2.字符的拼接和选择
## 04 `Reduce()`函数
### 相关介绍：`reduce()`作用：对序列中的元素进行积累，作用于这个列表的整体`map()`是将定义的函数作用于列表的每个值
    # 累加操作
    print(reduce(lambda x, y: x + y, numbers)) # 默认情况下第一项为1
    print(reduce(lambda x, y: x + y, numbers),2) # 从2开始进行累加
    # 阶乘操作
    print(reduce(lambda x, y: x * y, range(1, 6)))  # 输出5的阶乘
