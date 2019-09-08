# -*- coding: utf-8 -*-
# @Time    : 2019-09-08 14:06
# @Author  : 王碧野
# @FileName: weakref3.py
# @Software: PyCharm

# 循环引用演示

import weakref
import gc


class People(object):

    def __init__(self, name):
        self.name = name
        self.homework_attribution = None

    def __repr__(self):
        return "<%s at 0x%x name=%s>" % (self.__class__.__name__, id(self), self.name)

    def __del__(self):
        print("(__del__ %s)" % self.name)

    # 写作业 attribution: 作业归属
    def write_homework(self, attribution):
        self.homework_attribution = attribution
        print("写{name}的作业".format(name=self.homework_attribution.name))


def demo1():

    li = People('小李')
    zhang = People('小张')

    # 1. 自己直接调用强引用的自己, 最后设为 None 之后并没有释放, 成为垃圾对象
    li.write_homework(li)
    zhang.write_homework(zhang)
    # li = None
    # zhang = None


def demo2():

    li = People('小李')
    zhang = People('小张')

    # 2. 先创建弱引用的自己, 设为 None 之后不会产生垃圾对象
    weak_li = weakref.proxy(li, del_callback)
    weak_zhang = weakref.proxy(zhang)
    li.write_homework(weak_li)
    zhang.write_homework(weak_zhang)


def del_callback(value):
    # 如果这个方法不写入参, 会报错
    # value 无法使用, 已经不存在
    print('del_callback()')


# demo1()
demo2()

gc.collect()  # 收集垃圾
print("垃圾:")
print(gc.garbage)  # 获取垃圾列表
