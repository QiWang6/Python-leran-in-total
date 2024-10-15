# _*_ coding: utf-8 _*_
# @Time: 09.10.2024 12:52
# @Author: Qi Wang
# @File: test_datetime
# @Project: Python-leran-in-total

from datetime import datetime, date


print(date(1915, 10, 22))
print(datetime(2024, 2, 9))

dict1={'国家':'中国','首都':'北京'}
print(dict1.get('国家'))
print(dict1.get('首都'))
print(dict1.get('省会'))
f = ['hardware.get']
print(type(f))


response_codes = {401: {'derf':"gzjhn"}, 403: {}, 422: {}}
print(response_codes.get(401))

