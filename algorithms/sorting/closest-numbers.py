#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:12:33 2020

@author: brianf
"""


def closestNumbers(arr):
    sorted_arr = arr.copy()
    sorted_arr.sort()
    min_diff = sorted_arr[-1] - sorted_arr[0]
    for i in range(len(arr)-1):
        cur_diff = sorted_arr[i+1] - sorted_arr[i]
        min_diff = min(min_diff, cur_diff)
    
    result = []
    for i in range(len(arr)-1):
        if min_diff == sorted_arr[i+1] - sorted_arr[i]:
            result.append(sorted_arr[i])
            result.append(sorted_arr[i+1])
    
    return result

arr = [5,3,1,2,4]
a = closestNumbers(arr)