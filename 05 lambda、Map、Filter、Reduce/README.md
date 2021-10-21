# lambda表达式与`Map()`、`Filter()`、`Reduce()`使用
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
