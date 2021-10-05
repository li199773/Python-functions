# -- coding: utf-8 --
# @Time : 2021/10/04 23:54
# @Author : O·N·E
# @File : 04 文件拷贝压缩.py
import os
import shutil
import zipfile

"""
文件的拷贝：将一个文件拷贝到指定的目录下
"""
path_before = r"F:\PycharmProjects\Python函数\dict_write.txt"  # 原始的文件目录路径
path_after = r"F:\PycharmProjects\Python函数\02 文件处理\0401.txt"  # 复制之后的文件目录路径
shutil.copyfile(path_before, path_after)  # 文件复制
# 图片的拷贝复制
path_before_img = r"C:\Users\ONE\Desktop\论文\img.png"
path_after_img = r"F:\PycharmProjects\Python函数\02 文件处理\img_text.png"
shutil.copyfile(path_before_img, path_after_img)

"""
文件夹的拷贝 
"""
# 情况一：文件夹下面的所有文件的拷贝
dir_before = r"F:\PycharmProjects\Python函数\02 文件处理\04_before"
dir_after = r"F:\PycharmProjects\Python函数\02 文件处理\04_after"
shutil.copytree(dir_before, dir_after)  # 只有拷贝之后没有这个文件夹才会执行，否则会进行报错
# 情况二：文件夹下面指定文件的拷贝 ignore
dir_before = r"F:\PycharmProjects\Python函数\02 文件处理\04_before"
dir_after = r"F:\PycharmProjects\Python函数\02 文件处理\04_after"
shutil.copytree(dir_before, dir_after, ignore=shutil.ignore_patterns("*.png"))  # ignore方法会把除指定格式文件复制到指定的文件夹下面

"""
文件的压缩
"""
# 方式一：
ys_before = r"F:\PycharmProjects\Python函数\02 文件处理\04_before"
ys_after = r"F:\PycharmProjects\Python函数\02 文件处理\04_yasuo\yasuo"
shutil.make_archive(ys_after, "zip", ys_before)
# 方式二：zipfile模块
# 1.单个文件的压缩
ys_before = r"F:\PycharmProjects\Python函数\02 文件处理\04_before\1.txt"  # 压缩之后的路径是这个，以这个为主
zf = zipfile.ZipFile(r"F:\PycharmProjects\Python函数\02 文件处理\z.zip", "w")  # 只能在存在的文件夹下面进行保存
zf.write(ys_before, arcname="2.txt")  # arcname可以将路径消除，并且可以修改压缩之后文件的名称
zf.close()
# 2.文件夹的压缩
path = r"E:\home\x\data\202107\20210730_ok"
with zipfile.ZipFile("wjj.zip", "w") as target:
    for root, dir, files in os.walk(path):
        for file in files:
            # arcname 同样子是修改名称，打开文件夹就是
            target.write(os.path.join(root, file), arcname=file)  # 首先循环遍历在指定文件夹下面的文件，将每个问价写入压缩包中即可
