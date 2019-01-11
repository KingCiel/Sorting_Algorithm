#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/1 15:33
# @Author  : LNR_xiaoyu
# @E-mail    : xxxxxxxxxx@xxx
# @File    : bubble_sort.py
# @Software: PyCharm


def bubble_sort(a_list):
    """冒泡排序"""
    n = len(a_list)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]   # 把最大的放在最后面。
    return a_list


def new_bubble_sort(a_list):
    """改进的冒泡排序"""
    """
    判断： 如果 is_exchange=False 没有交换则退出循环
    """
    n = len(a_list)
    for i in range(0, n - 1):
        is_exchange = False
        for j in range(0, n - 1 - i):
            if a_list[j] > a_list[j + 1]:
                is_exchange = True
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]  # 把最大的放在最后面。
        if is_exchange is False:
            return a_list
    return a_list


if __name__ == '__main__':
    import time
    li = [10, 2, 55, 20, 6, 9, 35, 7, 15]
    big_list_1 = list(range(10000))[::-1]
    big_list_2 = list(range(10000))[::-1]
    big_list_3 = list(range(10000))
    big_list_4 = list(range(10000))
    print(big_list_1)
    print("raw_list:", li)

    print("raw_bubble")
    t1 = time.time()
    sorted_list = bubble_sort(big_list_3)
    print("时间：", time.time()-t1)
    print("sorted_list:", sorted_list)

    print("\nnew_bubble")
    t1 = time.time()
    sorted_list = new_bubble_sort(big_list_4)
    print("时间：", time.time()-t1)
    print("sorted_list:", sorted_list)
