# -*- coding: utf-8 -*-
# @Time    : 2019-09-10 10:30
# @Author  : 王碧野
# @FileName: block.py
# @Software: PyCharm

# 用返回函数实现类似 iOS 的 block

import weakref
import gc


class Son(object):

    def __init__(self):
        self.money = 0
        self.father_wallet = None

    def get_wallet(self, wallet):
        self.father_wallet = wallet

    def get_money(self):
        self.money += self.father_wallet()
        print('儿子的钱: {money}'.format(money=self.money))


class Father(object):

    def __init__(self):
        self.money = 100
        self.son = None

    def wallet(self):

        weak_self = weakref.proxy(self)  # 本示例并没有造成内存泄漏, 此处不用 weakref 也可以

        def lost_money():
            if weak_self.money == 0:
                print('爹没钱了')
                return 0
            step = 10
            weak_self.money -= step
            print('爹的钱: {money}'.format(money=weak_self.money))
            return step

        return lost_money

    def get_son(self):
        self.son = Son()
        self.son.father_wallet = self.wallet()


f = Father()
f.get_son()
f.son.get_money()
f.son.get_money()

gc.collect()  # 收集垃圾
print("垃圾:")
print(gc.garbage)  # 获取垃圾列表
