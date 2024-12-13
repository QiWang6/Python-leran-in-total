# _*_ coding: utf-8 _*_
# @Time: 23.10.2024 13:31
# @Author: Qi Wang
# @File: subclass3
# @Project: In total
# @Quelle:

class AbstractBase:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'foo'):
            raise TypeError('Subclasses must define foo method')

class GoodSubclass(AbstractBase):
    def foo(self):
        pass

class BadSubclass(AbstractBase):
    pass
# 抛出错误: TypeError: Subclasses must define foo method

