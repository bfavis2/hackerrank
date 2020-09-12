#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 21:03:56 2020

@author: brianf
"""


def getWays(n, c):
    # each index in memo stores how many of the coin combinations add up to the index number
    memo = [1] + [0]*n
    for coin in c:
        for j in range(n - coin + 1):
            if memo[j] > 0:
                memo[j+coin] += memo[j]

    return memo[-1]

n = 10
c = [2,5,3,6]

ans = getWays(n,c)