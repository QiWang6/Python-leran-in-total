# @Time: 2024/10/7 
# @Author: Qi Wang
# @File: write_file
# @Project: Python-leran-in-total
# @Quelle:


# w模式会把之前的内容清空，如果该文件不存在，会自动创建一个
with open("./poem.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去， \n又恐琼楼玉宇， \n高处不胜寒。\n")


# a模式会在原有文本的基础上添加内容
with open("./poem.txt", "a", encoding="utf-8") as f:
    f.write("起舞弄清影， \n何似在人间。")