#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:10:35 2020

@author: brianf
"""


cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))