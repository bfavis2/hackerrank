#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:34:40 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for _ in range(int(input())):
    method, *n = input().split()
    getattr(d, method)(*n)

print(*d)