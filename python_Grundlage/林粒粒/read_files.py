# @Time: 2024/10/7 
# @Author: Qi Wang
# @File: read_files
# @Project: Python-leran-in-total
# @Quelle:

'''
# 要读的文件和python文件处于同一文件夹之下
f = open("./data.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()
'''


# 下面这种方法不需要单独关闭文件
with open("./data.txt", "r", encoding="utf-8") as f:
    # content = f.read()
    # print(content)
    # print('-*'*30)
    # print('下面演示逐行读取')
    # print(f.readline())
    # print(f.readline())
    lines = f.readlines()
    for line in lines:
        print(line)
