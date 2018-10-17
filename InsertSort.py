#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time         : 2018/10/17 17:22

""" Insert Sort """

__author__ = 'Mht'


def insert_sort(nums):
    """接受一个list，进行插入排序"""
    for i in range(len(nums)):
        j = i - 1
        key = nums[i]  # 记录当前需要做插入操作的值
        while j > -1 and key > nums[j]:  # 寻找插入点，并不断后移
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key  # j+1就是最终需要插入的位置
    return nums


def select_sort(nums):
    """ 选择排序 """
    for i in range(len(nums) - 1):
        temp = i
        for j in range(i, len(nums)):
            if nums[j] < nums[temp]:
                temp = j
        nums[i], nums[temp] = nums[temp], nums[i]
    return nums


test = [2, 1, 3, 5, 0, 3]
print(select_sort(test))
