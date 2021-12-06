# -*- coding: utf-8 -*-
# @Time : 2021/11/2 15:31
# @Author : O·N·E
# @File : 02 base64加密.py
"""
base64：
    1.邮件传输
    2.降低传输过程中的出错几率
编码原则：
    1.把原来8位二进制转换成6位二进制进行计算，从A-Z,a-z,0-9,+ / 一共64个编码，对应不同的0-63数字
    2.base64最低为4个字节，不够的其余补0即可 补充的0编码成'='即可,因为不知道是不是base64中的0还是补充的0
    3.补0凑齐24位二进制的数，如果0全部为补充的那么就为=，如果有原始的0+补充的0 那么为A
字符编码：
    Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
    UTF是为unicode编码设计的一种在存储和传输时节省空间的编码方案。
总结：
    Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
"""
import base64

# 加密
"""写法一"""
content = "你好中国"
content_utf8_byte = content.encode("utf-8")  # 一个汉字这utf-8中表示3个字节，一个字节表示8个二进制数
content_base64 = base64.b64encode(content_utf8_byte)
print(content_base64.decode('utf-8'))
"""写法二"""
content1 = base64.b64encode(content.encode('utf-8'))
print(content1.decode('utf-8'))
"""写法三"""
content2 = base64.encodebytes(bytes(content.encode('utf-8'))).decode('utf-8')  # b64encode函数的参数为byte类型
print(content2)  # 这种写法会多一个换行符

# 解密
res = base64.b64decode(content_base64)
print(res.decode("utf-8"))

# base64对图片的加密解密
with open("02 test.jpg", 'rb') as fp:
    content3 = base64.b64encode(fp.read())
    print(content3.decode())  # 传入图片之后进行直接加密即可

# 对url进行编码：为了防止有歧义，编码时使用'-' 替换'+' 使用 '_'替换'/'
url = "https://docs.python.org/3/library/base64.htm?a=~"
content4 = base64.b64encode(url.encode('utf-8'))
print(content4.decode('utf-8'))
res1 = base64.b64decode(content4)
print(res1.decode('utf-8'))

test_url = 'https://docs.python.org/3/library/base64.htm?a=~'

encode_url = base64.encodebytes(test_url.encode())  # 普通编码
print(encode_url.decode())

safe_encode_url = base64.urlsafe_b64encode(test_url.encode())  # URL安全编码
print(safe_encode_url.decode())

safe_encode_url = base64.b64encode(test_url.encode(), b'-_')  # 编码时使用'-' 替换'+' 使用 '_'替换'/' ，效果与前例相同
print(safe_encode_url.decode())
