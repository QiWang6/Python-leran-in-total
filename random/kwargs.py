# _*_ coding: utf-8 _*_
# @Time: 23.10.2024 13:50
# @Author: Qi Wang
# @File: kwargs
# @Project: In total
# @Quelle:

def fun(a, b, c):
    print(a, b, c)

fun(1,2,3)

l = [1,2]
fun(8,*l)


def fun2(*args):
    print(args)

fun2(5)
fun2(4,8,6)


def fun3(a, *args):
    print(f'a is {a}, args is {args}')

fun3(45,12,65,99)
fun3(52)


def fun4(a, *args):
    print(a)
    print("args can receive a tuple of any number of arguments, let's print all that.")
    for arg in args:
            print(arg)

fun4(1,5,6,7)


def calculate_sum(*args):
    return sum(args)

def ignore_first_calculate_sum(a,*iargs):
    required_sum = calculate_sum(*iargs)
    print(f"sum is {required_sum}")

ignore_first_calculate_sum(12, 1,4,5)


def fun5(a, b, c):
    print(a, b, c)

d={'b':5, 'c':7}
fun5(1, **d) # unpack字典，并将字典中的数据项作为键值参数传给函数。因此,"fun(1, **d)"的写法与"fun(1, b=5, c=7)"等效

d = {'a':7, 'b':3, 'c':8}
fun5(**d)

# 人为错误
'''d = {'a':7, 'b':3, 'c':8, 'd':90}
fun5(**d)'''


def fun6(a, **kwargs):
    print (f"a is {a}")
    print (f"We expect kwargs 'b' and 'c' in this function")
    print (f"b is {kwargs['b']}")
    print (f"c is {kwargs['c']}")

fun6(1, c=5, b=3, d=78)

fun6(1, **{'b':2, 'c':34})  # 在一个字典前使用"**"可以unpack字典,传字典中的数据项作为键值参数


class Model(object):
    def __init__(self, name):
            self.name = name
    def save(self, force_update=False, force_insert=False):
            if force_update and force_insert:
                    raise ValueError("Cannot perform both operations")
            if force_update:
                    print("Updated an existing record")
            if force_insert:
                    print("Created a new record")
            print(self.name)


class ChildModel(Model):
    def save(self, *args, **kwargs):
            if self.name=='abcd':
                    super(ChildModel, self).save(*args, **kwargs)
            else:
                    return None

c=ChildModel('abcd')
c.save(force_insert=True)
