import os

path = r'E:\home\x\data\202107'

for root, dir, files in os.walk(path):
    # print(root)
    # for dirname in dir:  # 遍历指定文件夹下面的所有的文件夹名字
    #     print(os.path.join(root, dirname))
    for filename in files:
        print(os.path.join(root, filename))  # 遍历指定文件夹下面的所有的文件的名字
