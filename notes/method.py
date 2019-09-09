# -*- coding: utf-8 -*-
# @Time    : 2019-09-09 10:04
# @Author  : 王碧野
# @FileName: method.py
# @Software: PyCharm


class People:

    def __init__(self):
        self.__age = 18  # __表示是私有变量

    def __get_age(self):  # 私有方法
        print("get age: {age}".format(age=self.__age))
        return self.__age

    def show(self):
        print(self.__age)


p = People()
print(dir(p))  # 查看p对象的变量和方法
p._People__age = 38  # 访问私有变量
p._People__get_age()  # 访问私有方法，python私有变量的本质
