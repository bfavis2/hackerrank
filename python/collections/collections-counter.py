#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:18:50 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_shoes = int(input())
shoe_sizes = input().split()
shoe_sizes = Counter(shoe_sizes)

total = 0
num_customers = int(input())
for _ in range(num_customers):
    customer = input().split()
    if shoe_sizes[customer[0]] > 0:
        total += int(customer[1])
        shoe_sizes[customer[0]] -= 1

print(total)