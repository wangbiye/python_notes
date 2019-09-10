# -*- coding: utf-8 -*-
# @Time    : 2019-09-09 13:51
# @Author  : 王碧野
# @FileName: method2.py
# @Software: PyCharm

# 方法的继承


class Father(object):

    slogan = 'class slogan'

    def __init__(self):
        self.slogan = 'I am your father'

    def print_slogan(self):
        print(self.slogan)

    @classmethod
    def class_print_slogan(cls):
        print(cls.slogan)

    def static_print_slogan(self):
        print('Father static method')


class Son(Father):

    def __init__(self):
        # override 父类方法, 以下方式二选一
        # Father.__init__(self)
        # self.slogan = 'son of ...'
        # or
        super().__init__()

    @classmethod
    def class_print_slogan(cls):
        Father.class_print_slogan()
        print(cls.slogan)

    @staticmethod
    def static_print_slogan():
        print('Son static method')


f = Father()
f.print_slogan()
f.class_print_slogan()
# f.static_print_slogan()
