#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/1 18:47
# @Author  : LNR_xiaoyu
# @E-mail    : xxxxxxxxxx@xxx
# @File    : select_sort.py
# @Software: PyCharm


def select_sort(a_list):
    """选择排序"""

    n = len(a_list)
    for i in range(0, n-1):
        min_index = i             # 按顺序选择最小元素的索引。
        for j in range(i+1, n):
            if a_list[min_index] > a_list[j]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
    return a_list


if __name__ == '__main__':
    a_li = [6, 5, 8, 4, 2, 3, 0, 1]
    print(" 原始序列：", a_li)
    sort_list = select_sort(a_li)
    print("排序后序列：", sort_list)
