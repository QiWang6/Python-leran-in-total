# @Time: 2024/11/12 
# @Author: Qi Wang
# @File: 递归
# @Project: Python-leran-in-total
# @Quelle:

def f(x):
    if x>0:
        return x+f(x-1)
    else:
        return 0

print(f(10))