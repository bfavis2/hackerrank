#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:02:35 2020

@author: brianf
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[0]
    left = []
    equal = []
    right = []
    
    for num in arr:
        if num < p:
            left.append(num)
        elif num > p:
            right.append(num)
        else:
            equal.append(num)
    
    left = quick_sort(left)
    right = quick_sort(right)

    print(*left, *equal, *right)
    return left + equal + right

n = input().strip().split()
arr = [int(x) for x in input().strip().split()]
quick_sort(arr)