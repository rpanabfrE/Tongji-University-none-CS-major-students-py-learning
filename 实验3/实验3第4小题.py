# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:24:55 2023

@author: xieti
"""

ans=0
for i in range(1,51):
    a=2*i-1
    b=1/a
    ans += b
print("所求部分和为：",ans)