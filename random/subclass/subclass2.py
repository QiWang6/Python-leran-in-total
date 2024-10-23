# _*_ coding: utf-8 _*_
# @Time: 23.10.2024 12:53
# @Author: Qi Wang
# @File: subclass2
# @Project: In total
# @Quelle:
from email.policy import default


class PluginBase:
    subclasses = []
    NameList = []

    def __init_subclass__(cls, /, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
        cls.default_name = default_name
        cls.NameList.append(default_name)

class Plugin1(PluginBase, default_name = "Jack"):
    pass

class Plugin2(PluginBase, default_name = "Rose"):
    pass

class Plugin3(PluginBase, default_name = "Lucas"):
    pass




print(PluginBase.subclasses)
# 输出: [<class '__main__.Plugin1'>, <class '__main__.Plugin2'>]

