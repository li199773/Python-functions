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
except:
    print("输出错误")

try:
    print("setp 1")
    a = 3 / 0  # 程序在这里会报错，0不能作为除数 跳过这个然后执行下面的程序
    print("setp 2")
except BaseException as e:
    print("setp 3")
    print(e)
