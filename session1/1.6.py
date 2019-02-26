#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 14:11
# @Author  : bgzhou
# 问题：字典中的键映射多个值

from collections import defaultdict

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

# 可以方便的使用collections里面的defaultdict来构造这样的字典

d1 = defaultdict(list)
d1['a'].append(1)
d1['b'].append(2)
d1['a'].append(4)

d2 = defaultdict(set)
d2['a'].add(1)
d2['b'].add(2)
d2['a'].add(1)
d2['c'].add(3)

for key in d2:
    print(key)

