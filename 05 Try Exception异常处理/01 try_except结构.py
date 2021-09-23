"""
python 中一切都是对象，异常采取对象的方式处理，处理过程是：
1.异常抛出:在执行一个方法的时候，如果发生异常，则这个方法生成代表该异常的一个对象，停止当前执行路径，并且把异常对象提交给解释器
2.捕获异常：解释器得到该异常之后，寻找相应的代码处理该异常。
"""
# demo
# a = 3 / 0  # 分母不能为0
# print(a)

try:
    a = 3 / 0  # 分母不能为0
    print(a)
except ZeroDivisionError:
    print("输入的分母为0")
except ValueError:
    print("不能将字符串转换成数字")

# 可以将上述所有的异常用下面进行概括：
except BaseException as e:
    print("输出错误")
    print(e)

try:  # 尝试进行执行，有错误的情况下进行执行except下面语句
    print("setp 1")
    a = 3 / 0  # 程序在这里会报错，0不能作为除数 跳过这个然后执行下面的程序
    print("setp 2")
except BaseException as e:
    print("setp 3")
    print(e)  # 输出division by zero 说明错误点

# demo
while True:
    try:  # 只有输入数字的时候才会继续向下运行
        number = int(input("请输入一个数字:"))
        print("输入的数字是:{}".format(number))
        if number == 88:
            print("输入数字正好是88")
            break  # 当输入的程序数字正好为88的时候程序会停止
    except BaseException as e:  # 当输入的不为数字，例如as
        print(e)
        print("程序出错")
    finally:# 不论程序是否出错都会打印这句话
        print("无论程序是否出错，语句都会被打印")