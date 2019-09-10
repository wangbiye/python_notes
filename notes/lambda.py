# -*- coding: utf-8 -*-
# @Time    : 2019-09-10 16:50
# @Author  : 王碧野
# @FileName: lambda.py
# @Software: PyCharm


def sum_method():
    return lambda x: x + x


f = sum_method()
print(f)
print(f(1))

