# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:19:50 2023

@author: 蔡雨辰
"""
s=0	
n=1
while 1/n >= 1E-6:
    s=s+1/n
    n=n+2
print(s)