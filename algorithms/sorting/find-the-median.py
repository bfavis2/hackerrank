#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:24:18 2020

@author: brianf
"""


def findMedian(arr):
    sorted_arr = arr.copy()
    sorted_arr.sort()
    median_index = len(sorted_arr) // 2
    return sorted_arr[median_index]