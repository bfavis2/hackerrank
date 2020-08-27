#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:31:49 2020

@author: brianf
"""


from collections import OrderedDict

d = OrderedDict()
n = int(input())
for _ in range(n):
    item, space, price = input().rpartition(' ')
    if item in d:
        d[item] += int(price)
    else:
        d[item] = int(price)

for item, total in d.items():
    print(item, total)