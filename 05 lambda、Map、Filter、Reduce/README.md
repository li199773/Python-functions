# `lambda`表达式与`Map()`、`Filter()`、`Reduce()`使用
## 01 lambda表达式
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
## 02 map()表达式
### 相关介绍：`map()`的原型是`map(function, iterable, …)`，它的返回结果是一个列表。···表示可以传很多个列表。
    # 匿名函数
    print(list(map(lambda n: n * n, [1, 2, 3, 4, 5]))) # 根据传入的值输出其平方值，传入一个列表即可
