#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:12:03 2018

@author: exame
"""

def treasure(clues):
    total = len(clues)
    n = 0
    pos = (0, 0)
    while (n < total):
        try:
            n += 1
            new_pos = clues[pos]
            del clues[pos]
            pos = new_pos
        except KeyError:
            return pos
    return pos


print(treasure({(0,0): (1,0), (1,0): (2,0), (2,0): (3,0)}))
print(treasure({(0,0): (1,0), (2,1): (3,5), (1,0): (2,1)}))
print(treasure({(0,0): (5,6), (7,8): (6,7), (5,6): (6,7), (6,7):(7,8)}))
print(treasure({(-1,1): (3,2), (0,0): (0,0), (1,0): (-1,1)}))
