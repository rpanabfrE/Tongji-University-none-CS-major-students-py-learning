# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:03:21 2023

@author: xieti
"""

order=1
for i in range(100,1000):
    i=str(i)
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    i=int(i)
    if a**3+b**3+c**3==i:
        print("我找到的第",order,"个水仙花数是：",i)
        order += 1