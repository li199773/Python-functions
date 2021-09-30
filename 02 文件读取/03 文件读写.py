"""
文件的写入：
"""
# 1 open 文件写入
"""
open 一共有4种写入模式
"r" - 读取 - 默认值。打开文件进行读取，如果文件不存在则报错。
"a" - 追加 - 打开供追加的文件，如果不存在则创建该文件。
"w" - 写入 - 打开文件进行写入，如果文件不存在则创建该文件。
"x" - 创建 - 创建指定的文件，如果文件存在则返回错误。
"""
content = "你好 中国"
path = "E:/home/x/data/ni.txt"
# f = open(path, "a") # 没有文件的话首先先进行创建一个，写入情况下会在末尾源源不断地进行写入，不会删除
# f = open(path, "w")  # 没有文件的话首先也会进行创建一个，写入情况下只会写入传入的内容，原来的内容会进行删除在进行写入
f = open(path, "r")  # 首先进行判断，有的话报错，没有的话进行写入文件

# f.write(content)
# print("写入完成")
a = f.read()
print(a)

# 例子：
import csv

content = {'RecruitPostName': 'CSIG15-智能平台产品部-高级后台开发工程师（智平）', 'CountryName': '中国', 'LocationName': '深圳',
           'CategoryName': '技术'}
f = open("text.csv", "a", encoding='utf-8', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow([content["RecruitPostName"], content["CountryName"], content["LocationName"], content["CategoryName"]])

data = content["RecruitPostName"] + "," + content["CountryName"] + "," + content["LocationName"] + "," + content[
    "CategoryName"]
print(data)
data_1 = [content["RecruitPostName"], content["CountryName"], content["LocationName"], content["CategoryName"]]
data_2 = content["RecruitPostName"] + content["CountryName"] + content["LocationName"] + content["CategoryName"]
print(data_1)
with open("open_write.csv", "a", encoding='utf-8') as fp:
    for i in range(5):
        fp.write(data_1 + "\n")  # 使用with open的话要用,进行分开

# """
# 2.csv 函数的使用写入
# """
# (1) 方式一
import csv

headers = ["工作岗位", "工作国家", "工作地点", "岗位名称"]
f = open("csv_write.txt", 'a', encoding='utf-8', newline="")
csv_write = csv.writer(f)
for i in range(5):
    csv_write.writerow([content["RecruitPostName"], content["CountryName"], content["LocationName"], content["CategoryName"]])

# (2) 方式二：主要是进行字典变成csv文件的形式
import csv

# 添加表头的标题 要对的上
content["工作岗位"] = content.pop("RecruitPostName")
content["工作国家"] = content.pop("CountryName")
content["工作地点"] = content.pop("LocationName")
content["岗位名称"] = content.pop("CategoryName")
headers = ["工作岗位", "工作国家", "工作地点", "岗位名称"]
with open('../dict_write.txt', 'a', newline='', encoding='utf-8') as f:
    f_csv = csv.DictWriter(f, headers)  # 定义参数
    f_csv.writeheader()  # 写入表头
    for i in range(3):
        f_csv.writerows([content])  # 写入内容

"""
文件的读取操作:
"""
# 1.文件全部读取：read
with open("../dict_write.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 2.按行进行读取:
with open("../dict_write.txt", "r", encoding="utf-8") as f:
    for line in f:  # 使用迭代器
        if "中国" in line:
            print(line.strip())
            # print(line, end="") # 消除中间空行的2中方式 都可以，因为文字的末尾有个换行print还会在打印一次换行
with open("../dict_write.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    print(content)

"""
读取文件的文件名字f.name
"""
with open("../dict_write.txt", "r", encoding="utf-8") as f:
    print("文件名字是:{}".format(f.name))

"""
清空txt cvs 文件里面全部的内容
"""
with open("../dict_write.txt", "w") as f:  # 注意：仅当以 "r+"   "rb+"    "w"   "wb" "wb+"等以可写模式打开的文件才可以执行该功能。
    f.truncate()
