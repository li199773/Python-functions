# -- coding: utf-8 --
# @Time : 2021/9/28 23:54
# @Author : O·N·E
# @File : 04 文件拷贝压缩.py

import shutil
import zipfile

"""
文件的拷贝：将一个文件拷贝到指定的目录下
"""
# path_before = r"F:\PycharmProjects\Python函数\dict_write.txt"  # 原始的文件目录路径
# path_after = r"F:\PycharmProjects\Python函数\02 文件处理\0401.txt"  # 复制之后的文件目录路径
# shutil.copyfile(path_before, path_after)  # 文件复制
# # 图片的拷贝复制
# path_before_img = r"C:\Users\ONE\Desktop\论文\img.png"
# path_after_img = r"F:\PycharmProjects\Python函数\02 文件处理\img_text.png"
# shutil.copyfile(path_before_img, path_after_img)

"""
文件夹的拷贝 
"""
# 情况一：文件夹下面的所有文件的拷贝
# dir_before = r"F:\PycharmProjects\Python函数\02 文件处理\04_before"
# dir_after = r"F:\PycharmProjects\Python函数\02 文件处理\04_after"
# shutil.copytree(dir_before, dir_after)  # 只有拷贝之后没有这个文件夹才会执行，否则会进行报错
# 情况二：文件夹下面指定文件的拷贝 ignore
# dir_before = r"F:\PycharmProjects\Python函数\02 文件处理\04_before"
# dir_after = r"F:\PycharmProjects\Python函数\02 文件处理\04_after"
# shutil.copytree(dir_before, dir_after, ignore=shutil.ignore_patterns("*.png"))  # ignore方法会把除指定格式文件复制到指定的文件夹下面

"""
文件的压缩
"""
# 方式一：
# ys_before = r"F:\PycharmProjects\Python函数\02 文件处理\04_before"
# ys_after = r"F:\PycharmProjects\Python函数\02 文件处理\04_yasuo\yasuo"
# shutil.make_archive(ys_after, "zip", ys_before)
# 方式二：zipfile模块
ys_before = r"F:\PycharmProjects\Python函数\02 文件处理\04_before\1.txt"  # 压缩之后的路径是这个，以这个为主
zf = zipfile.ZipFile(r"F:\PycharmProjects\Python函数\02 文件处理\z.zip", "w")  # 只能在存在的文件夹下面进行保存
zf.write(ys_before)
zf.close()
