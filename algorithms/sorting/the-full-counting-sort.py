#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:27:47 2020

@author: brianf
"""


def countSort(arr):
    mod_arr = [[int(x[0]), '-'] if i < len(arr)//2 else [int(x[0]), x[1]] for i, x in enumerate(arr)]

    sorted_arr = [[] for _ in range(len(arr)//2 + 1)]

    for pair in mod_arr:
        sorted_arr[pair[0]].append(pair[1])

    print_arr(sorted_arr)

def print_arr(sorted_arr):
    for i in sorted_arr:
        for j in i:
            print(j, end=' ')