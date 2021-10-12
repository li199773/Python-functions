# 02 文件读取:`glod()`函数,`os.walk()`函数，`shutil`函数，`zipfile`函数
## 02.01 `glod()`函数
## 相关问题：获取文件的路径，还可以获取文件夹下子文件中文件的相关路径。
## 介绍：
        # glod使用：获取文件的路径
        *：代表多个字符
        ?:代表一个字符
        []匹配指定范围内的字符，如[0-9]匹配数字
        **/*.txt 这个经常使用，可以深入子目录下面的目录中去。
## 02.02 os.walk()函数：可以遍历出指定路径下面的文件夹和文件内容
        for dirname in dir:  # 遍历指定文件夹下面的所有的文件夹名字
        print(os.path.join(root, dirname))
        for filename in files:
        print(os.path.join(root, filename))  # 遍历指定文件夹下面的所有的文件的名字
## 02.03 文件读写
### 相关说明：
### (1) open()文件写入，详细查看py文件
### (2) csv()文件写入，详细查看py文件
### (3) 文件的读取：全部读取；按行读取
## 02.04 文件拷贝压缩：`shutil`函数，`zipfile`函数
### (1)文件拷贝:`shutil`函数
        shutil.copyfile(path_before, path_after)  # 文件复制 path_before:文件之前的路径，path_after:保存文件的路径
        shutil.copytree(dir_before, dir_after)  # 只有拷贝之后没有这个文件夹才会执行，否则会进行报错
### (2)文件压缩:`zipfile`函数
        # 方式一:`shutil.make_archive`
        shutil.make_archive(压缩之后文件的路径, "zip", 压缩之前文件的路径)
        # 方式二:`zipfile.ZipFile`
        zf = zipfile.ZipFile
        zf.write(压缩之前文件的路径, arcname="xxx")  # arcname可以将路径消除，并且可以修改压缩之后文件的名称
        zf.close()
### `zipfile.ZipFile`的缺点是只能进行压缩一个文件，例如txt,csv文件，但是`shutil`函数既可以压缩文件也可以进行压缩文件夹。
        # 文件夹的压缩
        with zipfile.ZipFile("文件名称.zip", "w") as target: # 另一种格式
        for root, dir, files in os.walk(path): # 遍历目录下面所有的文件名称
                target.write(os.path.join(root, file), arcname=file)  # 将每个问价写入压缩包中即可，同样
