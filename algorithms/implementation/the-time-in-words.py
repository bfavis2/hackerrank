#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:11:28 2020

@author: brianf
"""

def timeInWords(h, m):
    h = int(h)
    m = int(m)
    
    lookup = {
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'quarter',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
        20 : 'twenty',
        21 : 'twenty one',
        22 : 'twenty two',
        23 : 'twenty three',
        24 : 'twenty four',
        25 : 'twenty five',
        26 : 'twenty six',
        27 : 'twenty seven',
        28 : 'twenty eight',
        29 : 'twenty nine',
        30 : 'half'
        }
    
    # if m == 0:
    #     result = f"{lookup[h]} o' clock"
    # elif m == 1:
    #     result = f'{lookup[m]} minute past {lookup[h]}'
    # elif m == 15 or m == 30:
    #     result = f'{lookup[m]} past {lookup[h]}'
    # elif m <= 29:
    #     result = f'{lookup[m]} minutes past {lookup[h]}'
    # elif m == 45:
    #     result = f'{lookup[15]} to {lookup[(h+1) % 12]}'
    # elif m == 59:
    #     result = f'{lookup[1]} minute to {lookup[(h+1) % 12]}'
    # else:
    #     result = f'{lookup[60 - m]} minutes to {lookup[(h+1) % 12]}'
        
    if m == 0:
        result = "{} o' clock".format(lookup[h])
    elif m == 1:
        result = '{} minute past {}'.format(lookup[m], lookup[h])
    elif m == 15 or m == 30:
        result = '{} past {}'.format(lookup[m], lookup[h])
    elif m <= 29:
        result = '{} minutes past {}'.format(lookup[m], lookup[h])
    elif m == 45:
        result = '{} to {}'.format(lookup[15], lookup[(h+1) % 12])
    elif m == 59:
        result = '{} minute to {}'.format(lookup[1], lookup[(h+1) % 12])
    else:
        result = '{} minutes to {}'.format(lookup[60 - m], lookup[(h+1) % 12]) 
        
    return result