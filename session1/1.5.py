#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 14:00
# @Author  : bgzhou
# 问题：怎样实现一个优先级排序的队列？并且在这个队列上面每次pop操作总是返回优先级最高的那个元素

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


if __name__ == '__main__':
    q = PriorityQueue()
    q.push("bgzhou", 1)
    q.push("cooky", 2)
    q.push("wangxc", 1)
    print(q.pop())
    print(q.pop())