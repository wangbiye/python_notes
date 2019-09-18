# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 13:09
# @Author  : 王碧野
# @FileName: multiple_inheritance.py
# @Software: PyCharm

# 多重继承


class Father(object):

    def eye(self):
        print('Father\'s eye')

    def nose(self):
        print('Father\'s nose')


class Mother(object):

    def eye(self):
        print('Mother\'s eye');

    def mouth(self):
        print('Mother\'s mouth')


class Son(Mother, Father):

    def eye(self):
        super().eye()

    def nose(self):
        super().nose()

    def mouth(self):
        super().mouth()


son = Son()
son.eye()
son.nose()
son.mouth()

print(type(son) == Son)
print(type(son) == Father)
print(type(son) == Mother)

print(isinstance(son, Son))
print(isinstance(son, Father))
print(isinstance(son, Mother))
