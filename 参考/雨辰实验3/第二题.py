# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:17:56 2023

@author: 蔡雨辰
"""
for x in range(100,1000):
    m=x//100
    n=x//10%10
    k=x%10
    if x==m**3+n**3+k**3:
        print(x)