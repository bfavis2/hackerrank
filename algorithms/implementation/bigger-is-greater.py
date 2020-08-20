#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:35:08 2020

@author: brianf
"""

def biggerIsGreater(w):
    if len(w) <= 1:
        return 'no answer'
    reverse = [char for char in w[::-1]]
    i = 0
    
    while reverse[i] <= reverse[i+1]:
        i += 1
        if i == len(w) - 1: 
            return 'no answer'
    
    # Swap the last char seen (at i+1) with the lowest value that is
    # greater than the last char seen in the remaining chars looked at
    options = [num for num in reverse[:i+1] if num > reverse[i+1]]
    min_value = min(options)
    min_index = reverse[:i+1].index(min_value)
    reverse[min_index] = reverse[i+1]
    reverse[i+1] = min_value
    
    start = reverse[:i+1]
    end = reverse[i+1:]
    start.sort(reverse=True)
    
    result = ''.join(start + end)
    return result[::-1]
    
