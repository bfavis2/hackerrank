#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:33:47 2020

@author: brianf
"""


def countingSort(arr):
    count = [0 for _ in range(100)]
    for num in arr:
        count[num] += 1
    return count