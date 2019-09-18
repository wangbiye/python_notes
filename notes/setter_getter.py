# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 11:36
# @Author  : 王碧野
# @FileName: setter_getter.py
# @Software: PyCharm


class People(object):

    def __init__(self):
        self.age = 38

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


p = People()
p.age = 18

