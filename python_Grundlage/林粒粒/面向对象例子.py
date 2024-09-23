# @Time: 2024/9/23 
# @Author: Qi Wang
# @File: 面向对象例子
# @Project: Python-leran-in-total
# @Quelle: https://www.bilibili.com/video/BV1ug411R7Yz/?spm_id_from=pageDriver&vd_source=edaa7c180a2e4b42b2b256823b55fcbf

class student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.grades = {"语文": 0, "数学": 0, "英语": 0}


    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade


    def print_grades(self):
        print(f"Student {self.name}, number: {self.number}\ngrade: ")
        for course in self.grades:
            print(f"{course}: {self.grades[course]} notes")


chen = student("chen", "156")
chen.set_grade("语文", 95)
chen.set_grade("英语", 94)
chen.print_grades()
# zeng = student("zeng", "115")
# print(chen.name)
# print(zeng.name)
# zeng.set_grade("语文", 100)
# print(zeng.grades)
