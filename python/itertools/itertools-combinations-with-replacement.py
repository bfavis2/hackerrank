#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:11:30 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

string, n = input().split()
combined = list(combinations_with_replacement(sorted(string), int(n)))
for s in combined:
    print(''.join(s))