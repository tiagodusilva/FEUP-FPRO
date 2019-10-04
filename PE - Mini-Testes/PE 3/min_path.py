#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:13:10 2018

@author: exame
"""

def min_path(matrix, a, b, visited=[]):
    #print(a)
    if a == b:
        #print("Found!")
        return 0
    min_p = 999999999
    for i in range(a[0] - 1, a[0] + 2):
        for j in range(a[1] - 1, a[1] + 2):
            if (i != a[0] or j != a[1]) and 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (i, j) not in visited and not matrix[i][j]:
                aux = 1 + min_path(matrix, (i, j), b, visited.copy() + [(i, j)])
                min_p = min((min_p, aux))
    return min_p


mx = [
[False]*4,
[False, True, False, False],
[False, True, False, False],
[False]*4
]

print(min_path(mx, (2, 0), (0, 3)))
print(min_path(mx, (3, 1), (0, 1)))
print(min_path(mx, (0, 0), (3, 3)))
