#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 9:45
# @Author  : LNR_xiaoyu
# @E-mail    : xxxxxxxxxx@xxx
# @File    : quick_sort.py
# @Software: PyCharm


def quick_sort(a_list, start, end):
    """快速排序"""

    # 递归退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = a_list[start]

    # low 为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的，由右向左移动的游标
    high = end

    while low < high:
        # 如果low 与 high 未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and a_list[high] >= mid:
            high -= 1
        # 将 high 指向的元素放到 low 的位置
        a_list[low] = a_list[high]

        # 如果 low 与 high 未重合，low 指向的元素比基准元素小，则low向右移动
        while low < high and a_list[low] < mid:
            low += 1

        # 将 low 指向的元素放到 high 的位置
        a_list[high] = a_list[low]

    # 退出循环后， low与high重合，此时所指位置为基准的正确位置。
    # 将基准元素放到该位置
    a_list[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(a_list, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(a_list, low + 1, end)


if __name__ == "__main__":
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(a_list, 0, len(a_list) - 1)
    print(a_list)
