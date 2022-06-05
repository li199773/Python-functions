# -*- coding: utf-8 -*-
# @Time : 2022/6/5 12:21
# @Author : O·N·E
# @File : 01 uuid
"""
UUID是什么：
1.UUID： 通用唯一标识符 (Universally Unique Identifier)，对于所有的UUID它可以保证在空间和时间上的唯一性，也称为GUID，
    全称为：它是通过MAC地址、 时间戳、 命名空间、 随机数、 伪随机数来保证生成ID的唯一性,，有着固定的大小( 128 bit位 )，通常由 32 字节的字符串（十六进制）表示。
2.UUID有什么用?
　　很多应用场景需要一个id，但是又不要求这个id 有具体的意义，仅仅用来标识一个对象。常见的用处有数据库表的id字段；另一个例子是前端的各种UI库，
    因为它们通常需要动态创建各种UI元素，这些元素需要唯一的id， 这时候就需要使用UUID了。例如：一个网站在存储视频、图片等格式的文件时，
    这些文件的命名方式就可以采用 UUID生成的随机标识符，避免重名的出现。
"""
import uuid

"""
1. uuid.uuid1([node[, clock_seq]]) -- 基于时间戳
由 MAC 地址（主机物理地址）、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
但 MAC 的使用同时带来安全性问题，局域网中可以使用 IP 来代替MAC。
该函数有两个参数, 如果 node 参数未指定, 系统将会自动调用 getnode() 函数来获取主机的硬件地址. 如果 clock_seq  参数未指定系统会使用一个随机产生的14位序列号来代替.
"""
print(uuid.uuid1())

"""
2.uuid3()——基于名字和MD5散列值
通过计算命名空间和名字的MD5散列值来生成UUID，可以保证同一命名空间中不同名字的唯一性和不同命名空间的唯一性，同一命名空间的同一名字生成的UUID相同。
"""
print(uuid.uuid3(uuid.NAMESPACE_DNS, "one"))
print(uuid.uuid3(uuid.NAMESPACE_DNS, "two"))  # 根据算法生成唯一的uuid

"""
3.uuid4()——基于随机数
uuid.uuid4()
通过随机数来生成UUID，使用的是伪随机数，有一定的重复概率
"""
print(uuid.uuid4())

"""
4.uuid5()——基于名字的SHA-1散列值
uuid.uuid5(namespace, name）
通过计算命名空间和名字的SHA-1散列值来生成UUID，算法与uuid.uuid3()相同。
"""
print(uuid.uuid5(uuid.NAMESPACE_DNS, "one"))

"""
首先，Python中没有基于DCE的，所以uuid2可以忽略；
其次，uuid4存在概率性重复，由无映射性，最好不用；
再次，若在Global的分布式计算环境下，最好用uuid1；
最后，若有名字的唯一性要求，最好用uuid3或uuid5。
"""