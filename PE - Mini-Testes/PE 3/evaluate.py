#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:12:27 2018

@author: exame
"""

def evaluate(a, x):
    from functools import reduce
    a.insert(0, 0)
    return reduce(lambda j, i: j + (x**(i - 1))*a[i], range(len(a)))


print(evaluate([1, 2, 4], 5))
print(evaluate([1, 2, 4], 10))
print(evaluate([1, 2, 4, 6, 8], 2))
