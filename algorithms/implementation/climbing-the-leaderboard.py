#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:11:25 2020

@author: brianf

"""

def climbingLeaderboard(scores, alice):
    ranks = []
    leaderboard = list(dict.fromkeys(scores)) # Removes all duplicates
    for score in alice:
        rank = binary_search(score, leaderboard) + 1
        ranks.append(rank)
        print(rank)
    return ranks

def binary_search(target, alist):
    low = 0
    high = len(alist) - 1
    while low <= high:
        mid = (high + low) // 2
        if target < alist[mid]:
            low = mid + 1
        elif target > alist[mid]:
            high = mid - 1
        else:
            return mid
    return low
