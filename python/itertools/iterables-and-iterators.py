#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:37:06 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combos = list(combinations(letters, k))
filtered = filter(lambda x: 'a' in x, combos)
print("{0:.3}".format(len(list(filtered))/len(combos)))