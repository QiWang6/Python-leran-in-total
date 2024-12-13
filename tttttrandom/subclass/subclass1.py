# _*_ coding: utf-8 _*_
# @Time: 23.10.2024 12:38
# @Author: Qi Wang
# @File: subclass
# @Project: In total
# @Quelle: https://blog.csdn.net/weixin_73330544/article/details/136789805?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522D5E7750C-B44A-442F-8E64-0FCF8E042FEB%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=D5E7750C-B44A-442F-8E64-0FCF8E042FEB&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-136789805-null-null.142^v100^pc_search_result_base5&utm_term=python%20subclass&spm=1018.2226.3001.4187


class MyClass:

    """
    __new__方法是一个静态方法，它的第一个参数是cls，表示要实例化的类
    这个方法的主要任务是创建新的实例并返回它。
    """
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # 在这里可以添加一些额外的初始化代码
        return instance

    """
    __init__方法则是一个实例方法，它在__new__方法创建新实例后被调用，用于初始化新创建的实例。
    """
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __init_subclass__(cls, /, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name
        print(f'{cls} is a subclass of BaseClass, default_name: {default_name}')

class SubClass(MyClass, default_name="Bruce"):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2


a = MyClass(1, 2)

b = SubClass(3, 4)
