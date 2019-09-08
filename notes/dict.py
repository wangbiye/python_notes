# -*- coding: utf-8 -*-
# @Time    : 2019-09-08 17:53
# @Author  : 王碧野
# @FileName: dict.py
# @Software: PyCharm


my_dict = {'key': 'value'}
print(my_dict['key'])

# 方括号取值不能取不存在的 key
# print(my_dict['keyxx'])

if 'keyxx' in my_dict:
    print(my_dict['keyxx'])
else:
    print('没有这个东西')


# get 取值
print(my_dict.get('key'))
# get 取值在没有时会返回 None
print(my_dict.get('keyxx'))
# 或者自己指定返回值
print(my_dict.get('keyxx', 'fuxx'))

