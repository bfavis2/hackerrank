#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:30:21 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n, m = list(map(int, input().split()))

for i in range(n):
    d[input()].append(i+1)

for _ in range(m):
    value = input()
    if value in d:
        print(*d[value])
    else:
        print(-1)