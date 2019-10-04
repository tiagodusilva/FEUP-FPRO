#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:12:40 2018

@author: exame
"""

def recursive_dot(l1, l2):
    res = 0
    for i in range(len(l1)):
        if isinstance(l1[i], list):
           res += recursive_dot(l1[i], l2[i])
        else:
          res += l1[i] * l2[i]    
    return res


print(recursive_dot([1, [2, 3]], [4, [5, 6]]))
print(recursive_dot([[5, 3, 1], [2, 4]], [[4, 2, 0], [1, 3]]))
print(recursive_dot([2], [1]))
