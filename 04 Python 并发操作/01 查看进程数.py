import threading
import time

def fun1():
    for i in range(5):
        print("---python---{}".format(i))
        time.sleep(1)
        # 5秒钟之后线程1结束


def fun2():
    for i in range(10):
        print("***python***{}".format(i))
        time.sleep(1)
        # 在上面基础上又过了5秒钟之后整个线程结束，打印全部的线程数之后一个主线程在运行


def main():
    # 子线程
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t1.start()
    t2.start()

    # 主线程：与子线程一起运行
    while True:  # 进行死循环这个打印
        print(threading.enumerate())
        if len(threading.enumerate()) == 1:
            break
        time.sleep(1)


if __name__ == '__main__':
    main()
# 当调用Thread的时候不会创建线程，当调用创建出来的实例对象star方法的时候才会创建线程

# 调用线程的另一种方法：类方法
class threading(threading.Thread):
    def run(self):  # 一定要是run 才可以进行调用
        for i in range(5):
            print(i)


if __name__ == '__main__':
    time.sleep(1)
    t = threading()
    t.start()
    for i in range(5, 10):
        print(i)
