# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:35:51 2023

@author: xieti

全世界无产者，联合起来
"""

sum=0

for i in range(1,101):
    if i % 5 == 0:
        sum += i
        
print("1至100能被5整除的数据之和为",sum)