#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:49:56 2020

@author: brianf
"""

def quickSort(arr):
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
    
    return left + equal + right

arr = [4,5,3,7,2]
a = quickSort(arr)