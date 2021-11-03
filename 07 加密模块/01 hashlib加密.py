# -- coding: utf-8 --
# @Time : 2021/10/28 22:20
# @Author : O·N·E
# @File : 01 hashlib加密.py
"""
hash
    一般称为“散列”,也可以音译为"哈希"，可以把任意长度的输入，通过散列算法，变成固定唱的的输出，该输出就是散列值，这种转换是一种映射压缩，散列值的空间
    一般远小于输入的长度，不同的输入可能散列成相同的输出，而不可能从散列值来唯一的确定值。
    例如：sdadsadasd 可能会输出：123456
        asadasdasasdasd 也可能会输出：123456
        当然这种情况会非常的小，这种情况几率会非常的小
    简单来说就是将一种任意长度的消息压缩成固定长度的消息摘要的函数

哈希不是一个加密的算法，他只是一个散列的算法，真正的加密算法是衍生出来的MD5算法

哈希特性
    不可逆：在具备编码功能的同时，哈希算法也作为一种加密算法存在。即，你无法通过分析哈希值计算出源文件的样子。
    计算极快：20G高清电影和一个5K文本文件复杂度相同，计算量都极小，可以在0.1秒内得出结果。

MD5
    MD5讯息摘要演算法，一种广泛使用的密码杂凑函数，可以产生出一个128位的散列值，用于确保信息传输完整一致，MD5的前身有MD2，MD3,MD5(已过期)，
    主流还是MD5
    功能：输入任意长度的信息，经过处理，输出128位的信息(数字指纹):
    唯一性：不同的输入得到不同的结果

MD5算法的特点
    压缩性：任意长度的数据，算出的MD5值的长度都是固定的。
    容易计算：从原数据计算出MD5值很容易。
    抗修改性：对原数据进行任何改动，修改一个字节生成的MD5值区别也会很大。
    强抗碰撞：已知原数据和MD5，想找到一个具有相同MD5值的数据（即伪造数据）是非常困难的。
"""
# demo1 每次输出的值都不一样子
content = hash("a")
print(content)  # 每次输出值都不是一样子

# demo2 MD5
import hashlib
import time

m = hashlib.md5()
m.update(b"li")
print(m.digest())  # 将字符串进行消化
print(m.hexdigest())  # 转换成16进制的数字进行输出
# MD5的拼接：输入多少最后输出的话还是全部拼接之后进行输出的值
m.update("大家好".encode('utf-8'))
print(m.hexdigest())

m1 = hashlib.md5()
m1.update("li大家好".encode("utf-8"))
print(m1.hexdigest())  # 跟直接进行拼接作用其实是一样子的
m2 = hashlib.md5(b"asd")  # 直接进行写入即可
print(m2.hexdigest())  # 输出一个32位的16进制的数，一个16进制转换2进制的话占4位，所以转换成2进制占128位

"""
SHA-1
安全哈希算法（Secure Hash Algorithm）主要适用于数字签名标准（Digital Signature Standard DSS）里面定义的数字签名算法（Digital Signature Algorithm DSA）。
对于长度小于2^64位的消息，SHA1会产生一个160位的消息摘要。当接收到消息的时候，这个消息摘要可以用来验证数据的完整性。
"""
m3 = hashlib.sha1(b"asd")
print(m3.hexdigest())  # 明显是要比md5()加密算法是要长的 160位二进制数

"""
用于加密相关的操作，3.x里用hashlib代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
"""
m4 = hashlib.sha256(b"asd")
print(m4.hexdigest())  # 64位二进制数

m5 = hashlib.sha512(b"asd")
print(m5.hexdigest())  # 加密之后的位数会更多 128位二进制数

print("*" * 100)
m6 = hashlib.md5(b"ca28977.lottojp.ga:443\ncasino.3658801.com:443")
print(m6.hexdigest())

# 按照函数进行封装 传入内容即可
def exchange_to_md5(content):
    '''
    传入内容进行md5加密
    :param content: 内容
    :return: 返回加密后的内容
    '''
    # 创建md5对象
    md_obj = hashlib.md5()
    # 传入信息进行加密，注意传入的信息必须进行encode编码，否则报错
    md_obj.update(content.encode("utf-8"))
    # 获取加密后的信息
    md_res = md_obj.hexdigest()
    return md_res


# content1 = exchange_to_md5("asd")
# print(content1)

"""实例"""
if __name__ == '__main__':
    with open("01 test.txt") as fp:
        res = fp.read()
    print(res)
    content1 = exchange_to_md5(res)
    print(content1)
