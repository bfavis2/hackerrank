#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:41:24 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

string, n = input().split()
for i in range(1,int(n)+1):
    combined = list(combinations(sorted(string), i))
    for s in combined:
        print(''.join(s))