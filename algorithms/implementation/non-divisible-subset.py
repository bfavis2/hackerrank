#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:14:40 2020

@author: brianf
"""

import math

def nonDivisibleSubset(k, s):
    total = 0
    # Store num mod k in a frequency table
    s = [num % k for num in s]
    freq_dict = {key:0 for key in range(k)}
    for num in s:
        freq_dict[num] += 1

    # You can have at most one 0 and one k/2
    if freq_dict.get(0):
        total += 1
        del freq_dict[0]
    if freq_dict.get(k/2):
        total += 1
        del freq_dict[k/2]
    
    # Pick the higher freq value for each compliment pair
    for i in range(1, math.ceil(k/2)):
        total += max(freq_dict[i], freq_dict[k - i])

    return total
