# 标准的写入文件的异常处理
"""
open操作:普通的文件写入操作
"""
try:
    f = open("03_01.txt", "a", encoding='utf-8')
    content = "我爱中国\n"
    f.write(content)
except BaseException as e:
    print(e)
finally:  # 最后一定要关闭打开的写入文，否则会一直占用计算机的资源
    f.close()

"""
with操作:上下文管理器
不论什么原因跳出with块之后，都能确保文件的正确的进行关闭
"""
content = "我爱你中国\n"
with open("03_02.txt", "a", encoding="utf-8") as f:
    f.write(content)
