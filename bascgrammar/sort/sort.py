# !/usr/bin/python
# -*- coding: utf-8 -*-

# 冒泡排序
def bubble_sort(arr):
    a = len(arr)
    for i in range(a):
        for j in range(0, a - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = [23, 45, 3, 34, 65, 65, 33, 532, 54, 2]
    bubble_sort(arr)
    print(arr)
