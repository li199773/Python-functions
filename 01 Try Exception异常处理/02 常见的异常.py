# 介绍几种常见的异常的解决
# 异常基本上都派生于BaseException类

# 1.SyntaxError 语法错误
# 例如: int a = 3 在python不需要进行标注数据的类型

# 2.NameError 尝试访问一个没有声明的变量
# print(a)

# 3.ZeroDivisionError:除数为0错误
# print(3 / 0)
# ZeroDivisionError: division by zero

# 4.数值错误:ValueError
# float("adasdas")
# ValueError: could not convert string to float: 'adasdas'

# 5.类型错误：TypeError
# 123+"abc"
# TypeError: unsupported operand type(s) for +: 'int' and 'str' 数字类型与字符串类型不能直接相加

# 6.访问对象不存在的属性:AttributeError
# a=100
# a.sayhi()
# AttributeError: 'int' object has no attribute 'sayhi'

# 7.索引越界异常:IndexError
# a=[1,3,5]
# a[3]
# IndexError: list index out of range 找不到a的底4个元素

# 8.字典关键字不存在:KeyError
# a={"a":1,"b":2}
# print(a["c"])
# KeyError: 'c' 在上述定义的字典中找不到相关的c的关键字