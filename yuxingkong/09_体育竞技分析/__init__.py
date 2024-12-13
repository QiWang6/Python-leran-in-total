# _*_ coding: utf-8 _*_
# @Time: 16.09.2024 14:44
# @Author: Qi Wang
# @File: __init__.py
# @Project: Python
# @Quelle: https://www.youtube.com/watch?v=90c6sGT94dc&list=PLSjGo7VFRWbt3m26Sf9GGEEeiZglGtosE&index=9
# pyrhon学习网站: https://python123.io
# python第三方库网站: https://pypi.org/


from tttttrandom import random


def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():
    a = eval(input("请输入选手A的能力值（0-1）: "))
    b = eval(input("请输入选手B的能力值（0-1）: "))
    n = eval(input("模拟比赛的场次: "))
    return a, b, n


def printSummary(winsA, winsB):
    n = winsA + winsB
    print(f"竞技分析开始，共模拟{n}场比赛")
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))


def gameOver(a, b):
    return a == 15 or b == 15


def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"

        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()
