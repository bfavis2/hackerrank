#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:08:17 2020

@author: brianf
"""

def formingMagicSquare(s):
    possible_ms = [
                    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                    [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
                    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                    [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
                    [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
                    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                   ]
    costs = []
    for ms in possible_ms:
        cost = 0
        for ms_row, s_row in zip(ms, s):
            for i, j in zip(ms_row, s_row):
                if not i == j:
                    cost += max([i, j]) - min([i, j])
        costs.append(cost)
    return min(costs)

