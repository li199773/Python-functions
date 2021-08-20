# 线程之间是共享的机制
# 多任务共享一般是搭配使用，例如在爬虫中使用信息共享，一方面在抓取数据，一方面在下载数据进行保存
import threading
import time

sum = 100
a = [11, 22]


def threading1(temp):
    global sum
    sum += 1
    temp.append(33)
    print(sum)
    print(temp)


def threading2():
    print(sum)


def main():
    t1 = threading.Thread(target=threading1, args=(a,))  # args=(a,)传入数据，必须为元祖,隔开
    t2 = threading.Thread(target=threading2)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print(sum)


if __name__ == '__main__':
    main()
输出结果显示2个线程之间数据是共享的,包括主线程里面的输出也是共享的

多线程共享全局变量
数字很小的情况下一般不会出现问题
sum = 0


def threading1(a):
    global sum
    for i in range(a):
        sum += 1  # 这句话可以分为3步，1是将sum值拿到 2。自加1 3.将处理后的sum值返回，cpu可能运行前两步之后就不让线程1继续运行。
    print(sum)  # 会导致程序的出错
    # 输出结果100,


def threading2(a):
    global sum
    for i in range(a):
        sum += 1
    print(sum)


def main():
    t1 = threading.Thread(target=threading1, args=(1000000,))
    t2 = threading.Thread(target=threading2, args=(1000000,))
    t1.start()  # 执行完之后输出结果为100
    t2.start()  # 执行完之后输出结果为200
    time.sleep(5)
    print(sum)


if __name__ == '__main__':
    main()
"""
在多任务多线程中，共享全局变量一定会出错，因为有些还未执行。
事务的原子性：要不不做，要不就全部做完
"""

# 互斥锁解决资源竞争的问题
# 锁：mutex = threading.Lock()
# mutex 互斥的意思
sum = 0

mutex = threading.Lock()


def threading1(a):
    global sum
    mutex.acquire()  # 上锁
    for i in range(a):
        sum += 1
    mutex.release()  # 解锁
    print(sum)


def threading2(a):
    global sum
    mutex.acquire()  # 上锁
    for i in range(a):
        sum += 1
    mutex.release()  # 解锁
    print(sum)


def main():
    t1 = threading.Thread(target=threading1, args=(10000000,))
    t2 = threading.Thread(target=threading2, args=(10000000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print(sum)


if __name__ == '__main__':
    main()
