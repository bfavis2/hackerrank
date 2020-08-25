#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:22:21 2020

@author: brianf
"""


def quick_sort_in_place(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        print(*arr)
        quick_sort_in_place(arr, low, i - 1)
        quick_sort_in_place(arr, i + 1, high)
               
    return

n = input().strip().split()
arr = [int(x) for x in input().strip().split()]
quick_sort_in_place(arr, 0, len(arr) - 1)

# arr = [1,3,9,8,2,7,5]
# quick_sort_in_place(arr, 0, len(arr) - 1)
