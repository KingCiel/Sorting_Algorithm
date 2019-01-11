#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/1 19:22
# @Author  : LNR_xiaoyu
# @E-mail    : xxxxxxxxxx@xxx
# @File    : insert_sort.py
# @Software: PyCharm


def insert_sort(a_list):
    """插入排序算法"""
    n = len(a_list)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if a_list[j] < a_list[j-1]:
                a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            else:
                break
    return a_list


def my_insert_sort(a_list):
    """插入排序算法"""
    n = len(a_list)

    for i in range(1, n):
        com_index = i
        for j in range(0, i):
            if a_list[com_index] < a_list[j]:
                a_list[j], a_list[com_index] = a_list[com_index], a_list[j]
    return a_list


def other_insert_sort(a_list):
    """优化插入排序"""
    n = len(a_list)
    for i in range(1, n):

        j = i
        while j > 0:
            if a_list[j] < a_list[j-1]:
                a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
                j -= 1
            else:
                break
    return a_list


if __name__ == '__main__':
    a_li = [6, 5, 8, 4, 2, 3, 0, 1]
    print("rwa_list", a_li)
    sort_list = other_insert_sort(a_li)
    print("sorted_list", sort_list)
