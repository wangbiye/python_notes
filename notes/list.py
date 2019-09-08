# -*- coding: utf-8 -*-
# @Time    : 2019-09-08 17:13
# @Author  : 王碧野
# @FileName: list.py
# @Software: PyCharm

# 数组

# 点进去可以看所有的系统方法
test_list = list()
name = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']

# 常规 for in 遍历
for value in name:
    print(value)

# 同时遍历下标和 value
for i, value in enumerate(name):
    print(i, value)

# 切片 取前 3 个元组
print(name[0:3])
# 如果第一个 index 是 0, 可以省略
print(name[:3])
# 倒数切片
print(name[-2:-1])
# 省略 0
print(name[-2:])

# 打印数组长度
print(len(name))

# 打印数组最后一个元素 1
print(name[len(name) - 1])

# 打印数组最后一个元素 2
print(name[-1])

# 删除末尾元素
name.pop()
print(name)

# 删除指定索引的元素
name.pop(1)
print(name)

# 替换索引位置的元素, 直接针对该位置赋值
name[0] = 'xxx'
print(name)

# list 中的元素类型可以不同
values = ['abc', 12, True]
print(values)

# 二维数组
td = [['aaa', 'bbb'], [1, 2, 3]]
print(td)
