#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 17:51
# @Author  : bgzhou
# 问题：怎样在数据字典中执行一些计算操作（比如求最小值，最大值，排序等等）？

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# zip用于将两个可迭代元素打包成一个元组列表，一一匹配
# 注意的是 zip() 函数创建的是一个只能访问一次的迭代器，无法多次访问
# zip1 = zip(prices.values(), prices.keys())
# print(min(zip1))
# print(max(zip1))

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))


# 普通的用法
print(min(prices, key=lambda k: prices[k]))

# 当多个实体拥有相同的值的时候，键会决定返回结果
prices1 = {
    'AAA': 32,
    'BBB': 32
}
print(min(zip(prices1.values(), prices1.keys())))
print(max(zip(prices1.values(), prices1.keys())))

# 值相同的情况返回第一个值
print(max(prices1, key=lambda k: prices1[k]))
print(min(prices1, key=lambda k: prices1[k]))