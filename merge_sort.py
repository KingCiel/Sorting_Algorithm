#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 9:23
# @Author  : LNR_xiaoyu
# @E-mail    : xxxxxxxxxx@xxx
# @File    : merge_sort.py
# @Software: PyCharm


def merge_sort(a_list):
    """归并排序"""

    if len(a_list) <= 1:
        return a_list

    # 二分分解
    num = len(a_list) // 2
    left = merge_sort(a_list[:num])
    right = merge_sort(a_list[num:])

    # 合并

    return merge(left, right)


def merge(left, right):
    """合并操作，将两个有序数据 left[] 和 right[] 合并成一个大的有序数据"""

    # left 与 right 的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


alist = [54,26,93,17,77,31,44,55,20]
sorted_alist = merge_sort(alist)
print(sorted_alist)