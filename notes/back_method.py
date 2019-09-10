# -*- coding: utf-8 -*-
# @Time    : 2019-09-10 10:07
# @Author  : 王碧野
# @FileName: back_method.py
# @Software: PyCharm

# 返回函数


def back_method(*args):

    def sum_method():
        sum_value = 0
        for n in args:
            sum_value += n
        return sum_value

    return sum_method  # 这里返回的时候没有()


f = back_method(1, 2, 3)
print(f)
print(f())
