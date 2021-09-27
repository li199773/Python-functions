"""
glod使用：获取文件的路径
    *：代表多个字符
    ?:代表一个字符
    []匹配指定范围内的字符，如[0-9]匹配数字
    **/*.txt
"""
import glob

path = 'E:/home/x/data/202108/20210806/'


def main():
    filename = "*.txt"
    filename = "*2021071914*.txt"
    filename = "victim_alarm_20210719143402_8087087?.txt"
    # "**/*.txt" 这个经常使用，可以深入子目录下面的目录中去。
    filename = "**/*.txt"
    for file in glob.glob(path + filename, recursive=True):
        print(file)


if __name__ == '__main__':
    main()

def main():
    filename = '*.txt'
    id_file = file_out_dir + filename
    l = {}
    for root, dirs, files in os.walk(file_out_dir):
        if root[-1] != '/':
            root += '/'
        l[root] = files
    for k, v in l.items():
        for j in range(len(v)):
            file = k + l[k][j]
            # print(file)
            global name
            name = l[k][j][:-4]
            text = pd.read_csv(file, encoding='utf-8', sep='\t')
            res = read_file(text, name)