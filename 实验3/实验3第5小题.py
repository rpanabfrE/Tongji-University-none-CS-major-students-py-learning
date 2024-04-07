# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:28:07 2023

@author: xieti
"""

ans=0
a=1
b=1/a
while b >= 1E-6:
    ans += b
    a += 2
    b = 1/a
print("所求部分和为：",ans)