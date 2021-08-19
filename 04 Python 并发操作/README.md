# python 进程 线程 线程池学习
## 01 进程基础
### 相关介绍：主线程与子线程一起运行
#### 1.导入模块
        import threading # 多进程模块
#### 2.语法：
        t = threading.Thread(target=fun)
        t.start() # 当调用Thread的时候不会创建线程，当调用创建出来的实例对象star方法的时候才会创建线程
