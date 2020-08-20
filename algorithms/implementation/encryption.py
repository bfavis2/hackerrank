#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:18:13 2020

@author: brianf
"""

import math

def encryption(s):
    s = s.replace(' ', '')
    l = len(s)
    row = math.floor(math.sqrt(l))
    col = math.ceil(math.sqrt(l))
    if row * col < l:
        row += 1
    result = ''
    for i in range(col):
        result += s[i::col] + ' '
    return result.strip()
