#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:57:09 2020

@author: brianf
"""


def countingSort(arr):
    culmulative_count = []
    count = [0 for _ in range(100)]
    for num in arr:
        count[num] += 1
    
    total = 0
    for c in count:
        total += c
        culmulative_count.append(total)

    return culmulative_count

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input().split()[0]))
result = countingSort(arr)
print(*result)