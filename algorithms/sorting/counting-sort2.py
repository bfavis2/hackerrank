#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:38:43 2020

@author: brianf
"""


def countingSort(arr):
    sorted_arr = []
    count = [0 for _ in range(100)]
    for num in arr:
        count[num] += 1
    
    for i, c in enumerate(count):
        while c > 0:
            sorted_arr.append(i)
            c -= 1
    
    return sorted_arr