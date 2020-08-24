#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:11:49 2020

@author: brianf
"""

def insertionSort1(n, arr):
    temp = arr.copy()
    last_value = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] > last_value:
            temp[i+1] = arr[i]
            print_list(temp)
        else:
            temp[i+1] = last_value
            print_list(temp)
            return
    temp[0] = last_value
    print_list(temp)

def print_list(arr):
    for i in arr:
        print(i, end=' ')
    print()
