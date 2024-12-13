# _*_ coding: utf-8 _*_
# @Time: 23.10.2024 13:00
# @Author: Qi Wang
# @File: config
# @Project: In total
# @Quelle:

from subclass2 import PluginBase

class Plugin4(PluginBase, default_name = "Julia"):
    pass

print(Plugin4.NameList)