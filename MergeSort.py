#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time         : 2018/11/6 16:20

""" 归并排序，递归实现 """


def merge(la, lb):
    """
    将两个已经有序的列表合并为新的并返回
    :return: a new sorted list
    """
    i, j, k = 0, 0, 0
    new_list = list(la + lb)            # Python中无法直接指定列表长度，或者for迭代实现

    # 比较两个list中元素的大小，并赋值给新list。直到某一list已全部添加完毕。
    while i != len(la) and j != len(lb):
        if la[i] < lb[j]:
            new_list[k] = la[i]
            i += 1
        else:
            new_list[k] = lb[j]
            j += 1
        k += 1

    # 处理还剩下元素未放入新list的列表
    if i == len(la):                    # la已经全部插入新列表
        for item in range(j, len(lb)):
            new_list[k] = lb[item]
            k += 1
    else:                               # lb已经全部插入新列表，只剩下la
        for item in range(i, len(la)):
            new_list[k] = la[item]
            k += 1
    return new_list


def merge_sort(l):
    """
    归并比较的是从中间分开的，左右两个list
    :param l: the list need sort
    :return: a sorted list
    """
    length = len(l)
    if length > 1:
        la = merge_sort(l[0:length // 2])
        lb = merge_sort(l[length // 2:])
        return merge(la, lb)
    else:
        return l


if __name__ == '__main__':
    assert merge_sort([1, 5, 9, 78, 100, 12, 10]) == [1, 5, 9, 10, 12, 78, 100]
    assert merge_sort([1, 1]) == [1, 1]
    assert merge_sort([3, 2, 1, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    print('Ok')
