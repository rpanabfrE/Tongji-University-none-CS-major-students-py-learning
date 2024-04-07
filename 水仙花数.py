# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:02:11 2024

@author: xieti
"""

sum=1
for i in range (100,1000):
    i=str(i)
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    i=int(i)
    if a**3+b**3+c**3==i:
        print("我找到的第",sum,"个三位数的水仙花数是：",i)
        sum += 1