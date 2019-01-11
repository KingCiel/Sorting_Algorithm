#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 8:55
# @Author  : LNR_xiaoyu
# @E-mail    : xxxxxxxxxx@xxx
# @File    : shell_sort.py
# @Software: PyCharm


def shell_sort(a_list):
    """希尔排序"""
    n = len(a_list)

    # 设置步长
    gap = n // 2   # // 表示整除。保留整数部分
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and a_list[j - gap] > a_list[j]:
                a_list[j], a_list[j-gap] = a_list[j-gap], a_list[j]
                j -= gap

        # 计算新的步长
        gap = gap // 2
    return a_list


if __name__ == '__main__':
    a_li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    a_list = shell_sort(a_li)
    print(a_list)
