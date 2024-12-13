# @Time: 2024/10/27 
# @Author: Qi Wang
# @File: subclass4
# @Project: Python-leran-in-total
# @Quelle:

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

print(Animal.__subclasses__())  # 输出: [<class '__main__.Dog'>, <class '__main__.Cat'>]

