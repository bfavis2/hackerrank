#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:44:52 2020

@author: brianf
"""

def runningTime(arr):
    total = 0
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
            total += 1 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return total
