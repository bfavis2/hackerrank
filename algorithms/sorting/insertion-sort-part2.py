#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:25:52 2020

@author: brianf
"""

def insertionSort2(n, arr):
    for i in range(1, n):
        cur_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur_value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur_value
        print(*arr)
