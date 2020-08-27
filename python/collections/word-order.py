#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:33:28 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

d = OrderedDict()
n = int(input())
for _ in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(len(d.keys()))
for value in d.values():
    print(value, end=' ')
