#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:15:18 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

string, num = input().split()
permutations = list(permutations(sorted(string), int(num)))
for p in permutations:
    print(''.join(p))
