#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 9:41
# @Author  : bgzhou
# 问题：字典排序

# OrderedDict将会保持元素插入的顺序
from collections import OrderedDict
import json

d1 = OrderedDict()
d1['foo'] = 1
d1['bar'] = 2
d1['ha'] = 3

# for key in d1:
#     print(key, d1[key])

# 对于需要后续序列化为比如json形式数据的字典，使用这个意义非常大
# 需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
# 哨兵节点：next指向头节点和pre指向尾节点，如果链表为空，next和pre都会指向哨兵节点的key

# print(json.dumps(d1))


def trim(strs):
    l1 = list(strs)
    for index in range(len(l1)):
        if l1[index] == " ":
            continue
        else:
            l1 = l1[index:]
            break
    for index in reversed(range(len(l1))):
        if l1[index] == " ":
            continue
        else:
            l1 = l1[:index+1]
            break
    return "".join(l1)


if __name__ == '__main__':
    print(trim("  abcde  "))


