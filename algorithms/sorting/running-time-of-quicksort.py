#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:31:22 2020

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

count = 0
def quick_sort_in_place(arr, low, high):
    global count
    if low < high:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                count += 1
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        count += 1
        quick_sort_in_place(arr, low, i - 1)
        quick_sort_in_place(arr, i + 1, high)
               
    return count

n = input().strip().split()
arr = [int(x) for x in input().strip().split()]
qs = quick_sort_in_place(arr.copy(), 0, len(arr) - 1)
ins = runningTime(arr.copy())
print(ins - qs)