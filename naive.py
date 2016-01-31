# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 07:54:41 2016

@author: jcoop
"""

def naive(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z
    
print naive(2, 3)

print naive(3, 2)

print naive(3, 8)

print naive(8, 3)