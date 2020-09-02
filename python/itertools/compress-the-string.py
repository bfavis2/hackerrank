#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:25:53 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

result = [(len(list(g)), int(k)) for k, g in groupby(input())]
print(*result)
