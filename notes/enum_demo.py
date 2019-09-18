# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 13:25
# @Author  : 王碧野
# @FileName: enum_demo.py
# @Software: PyCharm

# 枚举类

from enum import Enum


class UserType(Enum):

    Driver = 1
    Passenger = 2


print(UserType.Driver.value)  # 使用枚举
print(UserType(1))  # 通过值获得枚举
