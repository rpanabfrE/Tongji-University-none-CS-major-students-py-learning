# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:07:16 2023

@author: xieti
"""

order= 1
for i in range(100,1000):
    a=i//100
    b=i//10%10
    c=i%10
    if a**3+b**3+c**3==i:
        print("我找到的第",order,"个水仙花数是：",i)
        order += 1