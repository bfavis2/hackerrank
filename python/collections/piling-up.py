#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:37:26 2020

@author: brianf
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque


def can_stack(cubes):
    cur_value = max(cubes)
    while len(cubes) != 0:
        if cubes[0] > cur_value or cubes[-1] > cur_value:
            print('No')
            return
        elif cubes[0] >= cubes[-1]:
            cur_value = cubes.popleft()
        else:
            cur_value = cubes.pop()

    print('Yes')
    return

n_tests = int(input())
for _ in range(n_tests):
    n = int(input())
    cubes = deque(map(int, input().split()))
    can_stack(cubes)