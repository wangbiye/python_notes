# -*- coding: utf-8 -*-
# @Time    : 2019-09-08 18:06
# @Author  : 王碧野
# @FileName: set.py
# @Software: PyCharm

list1 = ['aa', 'aa']

s1 = set(list1)
print(list1)
# ['aa', 'aa']
print(s1)
# set(['aa'])

# set 中不能存 list, 以下代码会报错
# list2 = ['bb', 'cc']
# s2 = set(list1, list2)

