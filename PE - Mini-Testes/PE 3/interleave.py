#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:13:00 2018

@author: exame
"""

def interleave(l1, l2):
    res = []
    for i in range(min(len(l1), len(l2))):
        if isinstance(l1[i], list):
           res += interleave(l1[i], l2[i])
        else:
          res += [l1[i], l2[i]] 
    return res


print(interleave([1, [4,2]], [3, [7,4]]))
print(interleave(['a','b','c'], [1,2,3,4,5]))
print(interleave([], [1,2]))
