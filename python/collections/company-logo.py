#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:35:53 2020

@author: brianf
"""


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()

counter = Counter(s)
counter = counter.most_common()
counter_sorted = sorted(counter, key=lambda x:(-int(x[1]), x[0]))
for i in range(3):
    print(*counter_sorted[i])