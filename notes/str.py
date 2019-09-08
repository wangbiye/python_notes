# -*- coding: utf-8 -*-
# @Time    : 2019-09-08 18:15
# @Author  : 王碧野
# @FileName: str.py
# @Software: PyCharm


import ctypes

if __name__ == '__main__':
    s1 = 'abc'
    print(s1)
    address = id(s1)
    print(address)
    s2 = s1.replace('b', 'a')
    print(s2)
    print(id(s2))
    # 重新打印原有地址的内容
    print(ctypes.cast(address, ctypes.py_object).value)

    # abc
    # 4386906032
    # aac
    # 4386995248
    # abc

