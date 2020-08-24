#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:17:11 2020

@author: brianf


"""

def gridSearch(G, P):
    for i in range(len(G)):
        j = 0
        start_index = 0
        offset = 0
        while P[j] in G[i][offset:]:
            start_index = G[i][offset:].index(P[j])
            k = i
            while P[j] in G[k][offset:][start_index : len(P[0])+start_index]:
                j += 1
                k += 1
                if j == len(P):
                    return 'YES'
            offset += 1
            j = 0
                
    return 'NO'
